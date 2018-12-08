window.addEventListener("load", e =>{
    //updateParcel();
    axiosUpdate();
});

// async function updateParcel(){
//     console.log("starting");
//     const res = fetch("https://challenge3andela.herokuapp.com/api/v1/parcels", 
//     {credentials: 'include'})
//     .then(rel=>console.log(rel.json()))
//     .catch(err=>console.log(err));
//     const result = res.json();
//     // place.innerText = result;
// }
const table = document.getElementById("f-api");

function axiosUpdate(){
    const entry = axios.get("https://challenge3andela.herokuapp.com/api/v1/parcels", 
    {withCredentials: true})
    .then(res=> {
        let all= res.data['item info'];
        console.log(all);

        let table = document.createElement('table');
        for (one of all){
            let destination = one.destination;
            let nickname = one.nickname;
            let id = one['parcel_id'];
            let pickup = one.pickup;
            let status = one.status;
            let weight = one.weight

            console.log(destination, nickname, id, pickup, status, weight);
        }
        document.body.appendChild(table);
    })
    .catch(err=>console.log(err));
}
