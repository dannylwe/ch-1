
function changeDest(){
    const parcel_id = document.getElementById("n-id").value;
    const destination = document.getElementById("n-dest").value;
    console.log(parcel_id, destination);
    id = parseInt(parcel_id);

    updateDetails={
        "destination": destination
    }

    const updateDest = "https://challenge3andela.herokuapp.com/api/v1/parcels/"+id+"/destination"
    function axiosPost(){
        axios.put(updateDest, updateDetails, {withCredentials: true})
        .then(res=> {if(res.status == 201){
            alert("updated destination to "+destination);
        }}).catch(err=>console.log(err))
    }
    axiosPost();

//     function loginFetch(){
//         fetch(updateDes, {
//             method: 'PUT',
//             credentials: 'include',
//             headers:{
//                 Accept: "application/json",
//                 'Content-Type': "application/json; charset=UTF-8",
                
//             },
//             body:JSON.stringify(loginDetails),
            
//         }).then(res => res.json()).catch(err=>console.log(err))
//     }
}

