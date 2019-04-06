

function login(data) {
    var url = 'http://127.0.0.1:8000/login/';
    return post(url, data);
}
function submit() {
    var username = document.getElementById("inputEmail").value;
        var password = document.getElementById("inputPassword").value;//var json = {'username':'username','password':'password'};
        var data = {};
        data['username'] = username;
        data['password'] = password;
        login(JSON.stringify(data)).then(res=>{
            if (res.code === 0){
                window.location.href="http://127.0.0.1:8000/test";
            }else{
                toastr.error(res.message)
            }
        })
}