window.addEventListener("load", e =>{
    axiosUpdate();
});

const divInput = document.getElementById("admin-Table");
divInput.innerHTML = '';

function axiosUpdate(){
    console.log("beginning fetch from source")
    const entry = axios.get("https://challenge3andela.herokuapp.com/api/v1/parcels/all", 
    {withCredentials: true})
    .then(res=> {
        console.log(res); 
        
        let output = '<div>' + 
        '<th>Parcel Id</th><th>Destination</th><th>Pickup</th><th>Nickname</th><th>Status</th>'
        res.data['item info'].forEach(post => {
            if(post.status==='cancelled'){
                output += `<tr>
                <td style = "width: 10%">${post.parcel_id}</td>
                <td style = "width: 20%">${post.destination}</td>
                <td style = "width: 22%">${post.pickup}</td>
                <td style = "width: 15%">${post.nickname}</td>
                <td style = "width: 10%">${post.status}</td>
                <td><i class="fas fa-edit" id="cancel-sign" style="display:none;" title="edit destination"></i></td>    
                </tr>`
            }else{
            output += `<tr>
            <td style = "width: 10%">${post.parcel_id}</td>
            <td style = "width: 20%">${post.destination}</td>
            <td style = "width: 22%">${post.pickup}</td>
            <td style = "width: 15%">${post.nickname}</td>
            <td style = "width: 10%">${post.status}</td>
            <td><i class="fas fa-edit" title="edit destination" id="cancel-sign" onclick=modal();></i></td>
            </tr>`
            }
        });
        output += '</div>';
        divInput.innerHTML = output;
        //divInput.innerHTML = successfulHTML(res);
        
    })
    .catch(err=>console.log(err));
}

function modal(id){
    console.log(id);
    // Get the modal
    var modal = document.getElementById('myModal');

    // Get the button that opens the modal
    var btn = document.getElementById("cancel-sign");

    // Get the <span> element that closes the modal
    var span = document.getElementById("close-modal");

    // When the user clicks the button, open the modal 
    
    modal.style.display = "block";
    console.log("helping" + id);

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
    modal.style.display = "none";
    }    

}