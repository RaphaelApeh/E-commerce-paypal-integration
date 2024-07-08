document.addEventListener('DOMContentLoaded',function(){
    let login = document.querySelector('#example');
    setInterval(function(){
        if(login.innerHTML === 'Login'){
            login.innerHTML = 'Welcome Back 😘'
        }else{
            login.innerHTML = 'Login'
        }
    },10000)
    });