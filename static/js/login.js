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
    login(JSON.stringify(data)).then(res => {
        console.log(res)
        if (res.code === 0 && res['role'] === 1) {
            window.location.href = "/test";
        } else if (res.code === 0 && res['role'] === 0) {
            window.location.href = "/admin";
        } else {
            toastr.error(res.message)
        }
    })
}

function toReg() {
    window.location.href = "/regView";
}

function reg() {
    var username = document.getElementById("inputEmail").value;
    var password = document.getElementById("inputPassword").value;//var json = {'username':'username','password':'password'};
    var data = {};
    data['username'] = username;
    data['password'] = password;
    post(/reg/, JSON.stringify(data)).then(res => {
        if (res.code === 0) {
            //
            toastr.success('注册成功,请联系管理员激活账号');
        } else {
            toastr.error(res.message)
        }
    })
}
