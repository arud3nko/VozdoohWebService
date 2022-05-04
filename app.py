from flask import Flask, render_template
from random import randint
from mysql.connector import connect, Error
from multiprocessing import Process
from settings import get_config

import threading
import time
import locale
import datetime

Config = get_config()

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

app = Flask(__name__)


aqi_level = 17
bg_color = '#FAEBD7'


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def SQLConnector(database):
    try:
        sql_connection = connect(
            host=Config.HOST,
            user=Config.USER,
            password=Config.PASSWORD,
            database=database
        )

    except Error as E:
        sql_connection.commit()
        print(E)

    select_data = "SELECT * FROM `pollution`"

    rows = execute_read_query(sql_connection, select_data)

    pollution = []
    timestamp = []

    for row in rows:
        pollution.append(int(row[2]))
        timestamp.append(int(row[1]))

    return pollution, timestamp


@app.route('/')
def index():
    levelsHourly = []
    levelsDaily = []
    dates = []
    hours = []

    pollutionDaily, timestampDaily = SQLConnector('forecast_daily')
    db_rows = len(pollutionDaily) - 1

    for i in range(40):
        levelsDaily.append(pollutionDaily[db_rows - i])
        ts = datetime.datetime.fromtimestamp(timestampDaily[db_rows - i])
        dates.append(ts.strftime("%d %b"))

    pollutionHourly, timestampHourly = SQLConnector('forecast_hourly')
    db_rows = len(pollutionHourly) - 1

    for i in range(48):
        levelsHourly.append(pollutionHourly[db_rows - 24 - i])
        ts = datetime.datetime.fromtimestamp(timestampHourly[db_rows - i])
        hours.append(ts.strftime("%H"))

    return render_template('index.html', aqi_level=aqi_level, bg_color=bg_color, levelsDaily=levelsDaily, levelsHourly=levelsHourly,
                           dates=dates, hours=hours)


if __name__ == '__main__':
    app.run()
