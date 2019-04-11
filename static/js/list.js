function restart(id) {
    console.log("重新测试"+id)
}

function start(id) {
    var data = {};
    data["id"] = id;
    post("/startScan/",JSON.stringify(data)).then(res =>{
        console.log(res)
    })
    console.log("开始测试"+id)
}

function report(id) {

    var data = {};
    data["id"] = id;
    window.location.href="../report/"+id;
    console.log("查看报告"+id)
}