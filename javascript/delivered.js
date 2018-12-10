window.addEventListener("load", e =>{
    axiosUpdate();
});

function axiosUpdate(){
    const entry = axios.get("https://challenge3andela.herokuapp.com/api/v1/parcels/delivered", 
    {withCredentials: true})
    .then(res=> {
        if(res.data.error == "unauthorized view access"){
            divInput.innerHTML = '<p>'+"nothing here"+'</p>';
        }else{
            divInput.innerHTML = successfulHTML(res);
        }
    })
    .catch(err=>console.log(err));
}

function successfulHTML(res){

    return '<pre>' + JSON.stringify(res.data['item info'], null, '\t') + '</pre>'; 
    
};