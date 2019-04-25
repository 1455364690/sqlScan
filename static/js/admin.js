var myChart = echarts.init(document.getElementById('user-pie'));

function react(userId) {
    var data = {'user_id': userId};
    post('/reactUser/', JSON.stringify(data)).then(res => {
        console.log(res)
        window.location.reload()
    })
}

function freeze(userId) {
    var data = {'user_id': userId};
    post('/freezeUser/', JSON.stringify(data)).then(res => {
        console.log(res)
        window.location.reload()
    })
}

function paintPie(data) {
    var option = {
        title: {
            text: '用户信息',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            x: 'left',
        },
        toolbox: {
            show: true,
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {
                    show: true,
                    type: ['pie', 'funnel'],
                    option: {
                        funnel: {
                            x: '25%',
                            width: '50%',
                            funnelAlign: 'left',
                            max: 1548
                        }
                    }
                },
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        calculable: true,
        series: [
            {
                name: '人数',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                data: data,
            }
        ],
        color: ['rgba(0,0,34,0.7)', 'rgba(0,34,0,0.3)','rgba(34,0,0,0.6)','rgba(34,34,0,0.2)','rgba(0,0,55,0.6)','rgba(0,0,0,0.5)']
    };
    myChart.setOption(option, true);
}
