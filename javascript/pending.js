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
        let output = '<div>';
        res.data['item info'].forEach(post => {
            //output += `<p>${post.destination}</p>`
            output += `<tr>
            <td>${post.destination}</td>
            <td>${post.parcel_id}</td>
            <td>${post.pickup}</td>
            <td>${post.nickname}</td>
            <td>${post.status}</td>
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
