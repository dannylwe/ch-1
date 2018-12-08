function parcel(){
    console.log("from parcel");
    const postParcel = "https://challenge3andela.herokuapp.com/api/v1/parcels"

    function getstuff(){
       
       var height = document.getElementById("p-height").value;
       var weight = document.getElementById("p-widith").value;
       var nickname = document.getElementById("p-nic").value;
       var destination = document.getElementById("p-destination").value;
       var pickup = document.getElementById("p-pickup").value;

       const parcelDetails = {
           "height": parseInt(height),
           "weight": parseInt(weight),
           "nickname": nickname,
           "destination": destination,
           "pickup": pickup
       }
       console.log(parcelDetails.height, weight, nickname);

       function postAxios(){
        //document.cookie="access_token_cookie=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDQyNDc4NjgsIm5iZiI6MTU0NDI0Nzg2OCwianRpIjoiNDNiODhiZmEtYjQzYy00NjVmLWEzOTQtODM3NDNjYzE5MDE5IiwiZXhwIjoxNTQ0MjU2NTA4LCJpZGVudGl0eSI6ImRhbm55MSIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.0cBvn5ScZZdYxBIkGLC5JuwqcHaddANzrzW1Be42XTs"
        axios.post(postParcel, parcelDetails, {withCredentials: true}).then(res=>console.log(res)).catch(err=>console.log(err));
       }

       postAxios();
      
       fetch(postParcel, {
            method: 'POST',
            headers:{
                Accept: "application/json",
                'Content-Type': "application/json; charset=UTF-8",
                credentials: 'include'
            },
            body:JSON.stringify(parcelDetails),
            
        }).then(response=>console.log(response.json())).catch(err=>console.log(err))
        };

        

    getstuff();
    
};