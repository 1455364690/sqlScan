function post(url,data) {
    return new Promise((resolve, reject)=>{
        $.ajax({
            method:'POST',
            url: url,
            data: data,
            success: res=>resolve(res),
            error: res=>reject(res)
        })
    })
}
function get(url) {
    return new Promise((resolve, reject)=>{
        $.ajax({
            method:'GET',
            url: url,
            success: res=>resolve(res),
            error: res=>reject(res)
        })
    })
}
// //get请求
// function get(url, data) {
//     var ajax = new XMLHttpRequest() || new ActivexObject("Microsoft,XMLHTTP");
//     if (data) {
//         // 如果有值
//         url += '?';
//         url += data;
//     }
//     ajax.open('get', url);
//     // send即可
//     ajax.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//     ajax.send();
//     ajax.onreadystatechange = function () {
//         // 在事件中 获取数据 并修改界面显示
//         if (ajax.readyState === 4 && ajax.status === 200) {
//             // console.log(ajax.responseText);
//             // 将 数据 让 外面可以使用
//             // return ajax.responseText;
//             // 当 onreadystatechange 调用时 说明 数据回来了
//             // ajax.responseText;
//             // 如果说 外面可以传入一个 function 作为参数 success
//             return ajax.responseText
//             //success(ajax.responseText);
//         }
//     }
// }
//
// //post请求
// function post(url, data) {
//     var ajax = new XMLHttpRequest() || new ActivexObject("Microsoft,XMLHTTP");
//     ajax.open('post', url)
//     ajax.send(data);
//     ajax.onreadystatechange = function () {
//         // 在事件中 获取数据 并修改界面显示
//         if (ajax.readyState === 4 && ajax.status === 200) {
//             // console.log(ajax.responseText);
//
//             // 将 数据 让 外面可以使用
//             // return ajax.responseText;
//
//             // 当 onreadystatechange 调用时 说明 数据回来了
//             // ajax.responseText;
//
//             // 如果说 外面可以传入一个 function 作为参数 success
//             //success(ajax.responseText);
//             return ajax.responseText
//         }
//     }
// }