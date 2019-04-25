function restart(id) {
    console.log("重新测试"+id)
}

function start(id) {
    var data = {};
    data["id"] = id;
    post("/startScan/",JSON.stringify(data)).then(res =>{
        window.location.reload();
    })
}

function report(id) {

    var data = {};
    data["id"] = id;
    window.location.href="../report/"+id;
    console.log("查看报告"+id)
}

function test(task_id) {
    window.open("../fileDetail/"+task_id)
}