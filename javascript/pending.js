window.addEventListener("load", e =>{
    //updateParcel();
    axiosUpdate();
});
const place = document.getElementById("api");

// async function updateParcel(){
//     console.log("starting");
//     const res = fetch("https://challenge3andela.herokuapp.com/api/v1/parcels", {credentials: 'include'})
//     .then(rel=>console.log(rel.json()))
//     .catch(err=>console.log(err));
//     const result = res.json();
//     // place.innerText = result;
// }

function axiosUpdate(){
    const entry = axios.get("https://challenge3andela.herokuapp.com/api/v1/parcels", 
    {withCredentials: true})
    .then(res=>console.log(res))
    .catch(err=>console.log(err));
     place.innerText = entry.then(res=>res.data);
}
