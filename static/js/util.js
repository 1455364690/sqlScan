function logout() {
    post('/logout/', JSON.stringify({})).then(res => {
        console.log(res);
        window.location.href = "/";
    })
}