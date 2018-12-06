function parcel(){
    console.log("from parcel");

    function getstuff(){
       const url = "https://challenge3andela.herokuapp.com/api/v1/parcels"
       var height = document.getElementById("p-height").value;
       var weight = document.getElementById("p-widith").value;
       var nickname = document.getElementById("p-nic").value;
       var destination = document.getElementById("p-destination").value;
       var pickup = document.getElementById("p-pickup").value;

       console.log(height, weight, nickname)
    }

    getstuff();
    
}