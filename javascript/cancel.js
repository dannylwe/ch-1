function cancelParcel(){
    var cancelItem = document.getElementById("cancel-id").value;
    id = parseInt(cancelItem);
    console.log(id);

    cancelDetails={
        "parcel_id": id
    }


    function axiosUpdate(){
        const entry = "https://challenge3andela.herokuapp.com/api/v1/parcels/"+id+"/cancel";
        axios.put(entry, cancelItem, {withCredentials: true}).then(res=>{
            alert("item of id "+ id + "has been deleted");
        })
    }

    axiosUpdate();
}