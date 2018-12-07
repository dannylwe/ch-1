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

       axios.post(postParcel, parcelDetails).then(res=>console.log(res)).catch(err=>console.log(err))
    }

    getstuff();
    
}