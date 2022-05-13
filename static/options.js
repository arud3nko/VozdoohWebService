const options1 = {
    title: 'Уровень загрязнения воздуха на ближайшие 5 дней',
    hAxis: {title: 'Дата', textStyle: { italic: 'true', fontSize: 12}},
    vAxis: {title: 'Air Quality Index', baselineColor: 'black'},
    backgroundColor: 'none',
    animation: {
        duration: 1000,
        startup: true,
        easing: 'out' },

    seriesType: 'bars',
    series: {1: {type: 'area', color: '#00FA9A', curveType: 'function'}},

    bar: {groupWidth: '61.8%'},
    dataOpacity: 0.8,
    legend: 'none',
    orientation: 'vertical',
};

const options2 = {
    title: 'Уровень загрязнения воздуха в ближайшие сутки',
    hAxis: {title: 'Время', textStyle: { italic: 'true', fontSize: 12}},
    vAxis: {title: 'Air Quality Index', baselineColor: 'black'},
    backgroundColor: 'none',
    animation: {
        duration: 1000,
        startup: true,
        easing: 'out' },

    seriesType: 'bars',
    series: {1: {type: 'area', color: '#00FA9A', curveType: 'function'}},

    bar: {groupWidth: '61.8%'},
    dataOpacity: 0.8,
    legend: 'none',
};