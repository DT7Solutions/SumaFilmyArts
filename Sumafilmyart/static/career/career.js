let more_info_btn = document.querySelector('#more-info');
let my_model = document.querySelector(".more-info-model");
let close_btn = document.querySelector('.model-close');

more_info_btn.addEventListener('click', function(){
    my_model.classList.add('model-active')
    // alert('its working!')
})
close_btn.addEventListener('click',function(){
    my_model.classList.remove('model-active')
})

