var show = true
$("#input-1a").fileinput({
    language: 'zh', //设置语言

    uploadUrl: "http://127.0.0.1:8000/upload/", //上传的地址
    uploadExtraData: {"id": 1, "fileName": 'check.sql'},
    showRemove: false, //显示移除按钮
    showPreview: show
    //uploadExtraData:{"id": 1, "fileName":'123.mp3'},
}).on("fileuploaded", function (event, data, msg) {
    document.getElementById("check-btn").style.display="inherit"
}).on("fileerror", function (event, data, msg) {
    console.log(data);
});

