var myChart = echarts.init(document.getElementById('pie'));
var myChart2 = echarts.init(document.getElementById('pie2'));

function getColor() {
    // var data = [];
    // for(var i=0;i<6;i++){
    //     data.push("rgba("+Math.ceil(Math.random()*255)+","+Math.ceil(Math.random()*255)+","+Math.ceil(Math.random()*255)+",0.3)")
    // }
    var data = ["rgba(245,143,152,0.6)", "rgba(78,114,184,0.6)", "rgba(127,184,14,0.6)", "rgba(144,215,236,0.6)", "rgba(0,135,146,0.6)", "rgba(250,167,85,0.6)"];
    return data
}

var table_data = [];
var attribute_data = [];

function graph(table, attribute) {
    table_data = table;
    var option = {
        title: {
            text: '数据库表错误信息',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            x: 'left',
            //data: ['高危', '中危', '低危', '普通', '多余']
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
                name: '预警级别',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                data: this.table_data,
            }
        ],
        color: getColor()//['rgba(0,0,34,0.7)', 'rgba(0,34,0,0.3)','rgba(34,0,0,0.6)','rgba(34,34,0,0.2)','rgba(0,0,55,0.6)','rgba(0,0,0,0.5)']
    };
    myChart.setOption(option, true);
    attribute_data = attribute
    var option2 = {
        title: {
            text: '关键属性错误信息',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            x: 'left',
            //data: ['高危', '中危', '低危', '普通', '多余']
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
                name: '预警级别',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                data: attribute
            }
        ],
        color: getColor()
    };


    myChart2.setOption(option2);
}



