function send(){
		
    const signUp = "https://challenge3andela.herokuapp.com/api/v1/auth/user"

    var email = document.getElementById("Email").value;
    var username = document.getElementById("username").value;
    var password = document.getElementById("psw").value;
    var cpassword = document.getElementById("c-psw").value;
    var phone = document.getElementById("handphone").value;
    var name = document.getElementById("Name").value;

    const signDetails = {
        "email": email,
        "password": password,
        "handphone": parseInt(phone),
        "username": username,
    };
    
    signupFetch();
    console.log(signDetails.username);

    function signupFetch(){
    fetch(signUp, {
        method: 'POST',
        headers:{
            Accept: "application/json",
            'Content-Type': "application/json; charset=UTF-8",
        },
        body:JSON.stringify(signDetails)
    }).then(res => res.text())
    .then(response => {if (!response.ok)
        {console.log("gg2", response); alert(response)} else{
            window.location.href = "login.html"
        }
    })
    .catch(err => console.log(err));
    }


};