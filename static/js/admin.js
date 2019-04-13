function react(userId) {
    var data = {'user_id': userId};
    post('/reactUser/', JSON.stringify(data)).then(res => {
        console.log(res)
        window.location.reload()
    })
}

function freeze(userId) {
    var data = {'user_id': userId};
    post('/freezeUser/', JSON.stringify(data)).then(res => {
        console.log(res)
        window.location.reload()
    })
}
