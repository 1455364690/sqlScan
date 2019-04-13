var show = true
$("#input-1a").fileinput({
    language: 'zh', //设置语言

    uploadUrl: "/upload/", //上传的地址
    allowedFileExtensions: ['sql','txt'],
    showRemove: false, //显示移除按钮
    showPreview: show
    //uploadExtraData:{"id": 1, "fileName":'123.mp3'},
}).on("fileuploaded", function (event, data, msg) {
    console.log(data)
}).on("fileerror", function (event, data, msg) {
    console.log(data);
});

