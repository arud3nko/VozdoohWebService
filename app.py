from flask import Flask, render_template
from random import randint
from mysql.connector import connect, Error

from settings import get_config

import locale
import datetime

Config = get_config()

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

app = Flask(__name__)


aqi_level = 17
bg_color = 'green'

levels = []
dates = []


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def SQLConnector():
    try:
        sql_connection = connect(
            host=Config.HOST,
            user=Config.USER,
            password=Config.PASSWORD,
            database=Config.DATABASE
        )

    except Error as E:
        sql_connection.commit()
        print(E)

    select_data = "SELECT * FROM `data`"

    rows = execute_read_query(sql_connection, select_data)
    pollution = []
    wind_speed = []
    temperature = []

    for row in rows:
        pollution.append(int(row[2]))
        wind_speed.append(float(row[4]))
        temperature.append(int(row[3]))

    return pollution


pollution = SQLConnector()


for i in range(40):
    levels.append(pollution[i*100])

    today = datetime.date.today() + datetime.timedelta(i)
    today = today.strftime('%d %b')

    dates.append(today)


@app.route('/')
def index():
    return render_template('index.html', aqi_level=aqi_level, bg_color=bg_color, levels=levels, dates=dates)


if __name__ == '__main__':
    app.run()
