document.addEventListener('DOMContentLoaded',function(){
    let change = document.querySelector('#change')
    setInterval(function(){
        if(change.innerHTML == '🖐 Hello User Welcome !'){
            change.innerHTML = 'New Product to Explore 😍';
        }
        else if(change.innerHTML == 'New Product to Explore 😍'){
            change.innerHTML = '30% off of Products 😎'
        }
        else{
            change.innerHTML = '🖐 Hello User Welcome !'
        }
    },10000)
})