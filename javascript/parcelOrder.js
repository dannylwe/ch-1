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

       if (parcelDetails.destination == parcelDetails.pickup){
           alert("pickup and destination can not be the same");
        //    process.exit(1);
            return;
        
       }

       function postAxios(){
       
        axios.post(postParcel, parcelDetails, {withCredentials: true})
        .then(res=>{if(res.statusText == "CREATED"){alert("added parcel:  " + parcelDetails.nickname)}})
        .catch(err=>alert("something went wrong."))
       }

       postAxios();
      
    //    fetch(postParcel, {
    //         method: 'POST',
    //         credentials: 'include',
    //         headers:{
    //             Accept: "application/json",
    //             'Content-Type': "application/json; charset=UTF-8",
    //         },
    //         body:JSON.stringify(parcelDetails),
            
    //     }).then(response=>console.log(response.text())).then(gg=>{if(!gg.ok){alert(gg)}}).catch(err=>alert(err))
        };

    getstuff();
    
};