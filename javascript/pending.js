window.addEventListener("load", e =>{
    //updateParcel();
    axiosUpdate();
});

// async function updateParcel(){
//     console.log("starting");
//     const res = await fetch("https://challenge3andela.herokuapp.com/api/v1/parcels", 
//     {credentials: 'include'})
//     .then(rel=>console.log(rel.json()))
//     .catch(err=>console.log(err));
//     const result = res.json();
//     // place.innerText = result;
// }


const tablePending = document.getElementById("f-api");
const divInput = document.getElementById("api-table");
//tablePending.innerHTML = '';
divInput.innerHTML = '';

function axiosUpdate(){
    const entry = axios.get("https://challenge3andela.herokuapp.com/api/v1/parcels", 
    {withCredentials: true})
    .then(res=> {
        console.log(res); 
        
        //trying to manipulate the DOM
        let output = '<div>' + 
        '<th>Parcel Id</th><th>Destination</th><th>Pickup</th><th>Nickname</th><th>Status</th>'
        res.data['item info'].forEach(post => {
            
            output += `<tr>
            <td style = "width: 10%">${post.parcel_id}</td>
            <td style = "width: 20%">${post.destination}</td>
            <td style = "width: 22%">${post.pickup}</td>
            <td style = "width: 15%">${post.nickname}</td>
            <td>${post.status}</td>
            <td><i class="far fa-times-circle"></i></td>
            </tr>`
        });
        output += '</div>';
        divInput.innerHTML = output;
        //divInput.innerHTML = successfulHTML(res);
        
    })
    .catch(err=>console.log(err));
}

function successfulHTML(res){

    return '<pre>' + JSON.stringify(res.data['item info'], null, '\t') + '</pre>'; 
    
};
