

function login(data) {
    var url = '/login/';
    return post(url, data);
}
function submit() {
    var username = document.getElementById("inputEmail").value;
        var password = document.getElementById("inputPassword").value;//var json = {'username':'username','password':'password'};
        var data = {};
        data['username'] = username;
        data['password'] = password;
        login(JSON.stringify(data)).then(res=>{
            console.log(res)
            if (res.code === 0){
                window.location.href="/test";
            }else{
                toastr.error(res.message)
            }
        })
}