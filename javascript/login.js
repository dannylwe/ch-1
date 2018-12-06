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
            },
            body:JSON.stringify(loginDetails)
        }).then(res => res.json())
        .then(response => {if (response.message == "Logged in successfully. Welcome to sendIT"){
            console.log("html_01_success");
            window.location.href = "parcel_order.html"
        } else if (response.error == "invalid credentials"){
            alert(response.error)
        }}).catch(err => console.log(err));
    };

    loginFetch();
    
};