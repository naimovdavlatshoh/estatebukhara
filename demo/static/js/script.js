let btn = document.querySelector('#btn')
let btn2 = document.querySelector('#btn2')
let sidebar = document.querySelector('.sidebar')
let searchBtn = document.querySelector('.bx-search')

let topNavigator = document.querySelector('.top_navigator')

btn.addEventListener('click',  ()=> {
    sidebar.classList.toggle('active')
    topNavigator.classList.toggle('active')
})


btn2.addEventListener('click',  ()=> {
    sidebar.classList.toggle('active')
    topNavigator.classList.toggle('active')
})

// modal

modal_btn = document.querySelector('.modal_btn')
modal_ = document.querySelector('.modal_')
close_btn = document.querySelector('.close_btn')

modal_btn.addEventListener('click', ()=>{
    modal_.classList.remove('d-none')
   
})


close_btn.addEventListener('click', ()=>{
    modal_.classList.add('d-none')
})




