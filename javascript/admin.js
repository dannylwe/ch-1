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
        '<th>Parcel Id</th><th>Destination</th><th>Pickup</th><th>Nickname</th><th>Status</th><th>Actions</th>'
        res.data['item info'].forEach(post => {
            if(post.status==='cancelled' || post.status === 'delivered'){
                output += `<tr>
                <td style = "width: 10%">${post.parcel_id}</td>
                <td style = "width: 20%">${post.destination}</td>
                <td style = "width: 22%">${post.pickup}</td>
                <td style = "width: 15%">${post.nickname}</td>
                <td style = "width: 15%">${post.status}</td>
                <td><i class="fas fa-edit" id="cancel-sign" style="display:none;" title="edit destination"></i></td>    
                </tr>`
            }else{
            output += `<tr>
            <td style = "width: 10%">${post.parcel_id}</td>
            <td style = "width: 20%">${post.destination}</td>
            <td style = "width: 22%">${post.pickup}</td>
            <td style = "width: 15%">${post.nickname}</td>
            <td style = "width: 10%">${post.status}</td>
            <td><i class="fas fa-edit" title="edit destination" id="cancel-sign" onclick=modal(${post.parcel_id});></i></td>
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
    var modal = document.getElementById('myModal');
    var btn = document.getElementById("cancel-sign");
    var span = document.getElementById("close-modal");

    modal.style.display = "block";
    console.log("helping " + id);
    console.log(document.getElementById("admin-status-change").value);

    span.onclick = () => {
    modal.style.display = "none";
    }
    window.onclick = (event) => {
        if (event.target == modal) {
          modal.style.display = "none";
        }
      }
    var submitButton = document.getElementById("admin-submit");   
    submitButton.onclick = () => {
        console.log(id);
        var status = document.getElementById("admin-status-change").value;
        console.log(status);

        const url = "https://challenge3andela.herokuapp.com/api/v1/parcels/"+ id +"/status"
        statusDetails = {
            "status": status
        }

        function runUpadate(){
            axios.put(url, statusDetails, {withCredentials: true})
            .then(res=>{
                console.log(res);
                window.location.replace("admin.html");
            }).catch(err=>console.log(err));
            //
        }

        runUpadate()
        
    } 


}