btnOpenNav = document.querySelector('.nav_menu');
btnCloseNav = document.querySelector('.overlay');


btnOpenNav.addEventListener('click', openNav);
btnCloseNav.addEventListener('click', closeNav);


function openNav(){
    this.querySelector('.navigator').style.display = 'block';
    this.parentElement.querySelector('.overlay').style.display = 'block';
}

function closeNav(){
    this.parentElement.querySelector('.navigator').style.display = 'none';
    this.style.display = 'none';
}
