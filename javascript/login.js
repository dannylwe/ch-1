function validation() {
    var username = document.getElementById("eml").value;
    var password = document.getElementById("pass").value;

    const loginSend = "https://challenge3andela.herokuapp.com/api/v1/auth/login"
    const signUp = "https://challenge3andela.herokuapp.com/api/v1/auth/user"

    const loginDetails = {
        "username": username,
        "password": password
    };
    
    console.log(username, password);

    function loginFetch(){
        fetch(loginSend, {
            method: 'POST',
            headers:{
                Accept: "application/json",
                'Content-Type': "application/json; charset=UTF-8",
                credentials: 'include'
            },
            body:JSON.stringify(loginDetails),
            
        }).then(res => res.json())
        .then(response => {if (response.message == "Logged in successfully. Welcome to sendIT"){
            console.log(response);
            window.location.replace("parcel_order.html")
        } else if (response.error == "invalid credentials"){
            alert(response.error)
        }}).catch(err => console.log(err));
        
    };

  
    console.log("from fetch");
    //document.cookie="access_token_cookie=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDQyMTY3NjIsIm5iZiI6MTU0NDIxNjc2MiwianRpIjoiYTVkMmIzN2MtZWFjNC00MWQwLWIzMDYtZjNmMWJkM2ZhZGZmIiwiZXhwIjoxNTQ0MjI1NDAyLCJpZGVudGl0eSI6ImRhbm55MiIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.hJIjxY6FL-QAC90ii-OBBgiczariPZ2zedPIKOasGVk"
    
    //axios.post(loginSend, loginDetails).then(res=>console.log(res)).catch(err=>console.log(err));
    loginFetch();
    
    //alert(document.cookie);
    
};