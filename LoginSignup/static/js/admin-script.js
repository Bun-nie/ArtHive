// FOR SIDEBAR MENU
/*
* click after click responsiveness 
*/
const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');
allSideMenu.forEach(item=>{
    const li = item.parentElement;

    item.addEventListener('click', function(){
        allSideMenu.forEach(i=>{
            i.parentElement.classList.remove('active');
        })
        li.classList.add('active');
    })
});

// FOR SIDEBAR MENU
/*
* toggle sidebar (not functional as of now)
*/
const menubar = document.querySelector('#content nav .bx bx-menu');
const sidebar = document.getElementById('sidebar');

menubar.addEventListener('click', function (){
    sidebar.classList.toggle('hide');
})