
let nav_item =  document.querySelector(".anchor_nav");
let btns = nav_item.getElementsByClassName("nav-btn");
for(let i = 0; i < btns.length; i++){
  btns[i].addEventListener('click', function(){
    let current = document.getElementsByClassName('active');
    current[0].className = current[0].className.replace(' active');
    this.className += ' active';
  })
}


/* main slider */
var swiper = new Swiper(".mySwiper", {
    speed:400,
    loop:true,

    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
    autoplay: {
    delay: 5000,
    },
  });
/* ending main slider */

var swiper = new Swiper(".mySwiper2", {
    speed:400,
    loop:true,

    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
    autoplay: {
    delay: 5000,
    },
  });

/* owl carsoul */
  $('.owl-carousel').owlCarousel({
    merge:true,
    loop :true,
    margin:10,
    video:true,
    lazyload:true,
    center:true,
    autoplay:true,
    autoplayTimeout:3000,
    stagePadding:70,
    responsive:{
      0:{
        item:1
      },
      600:{
        item:0
      },
      1000:{
        item:1
      }

    }
})

/* swiper image carsoul */

var swiper = new Swiper(".imgSwiper", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  coverflowEffect: {
    rotate: 0,
    stretch: 0,
    depth: 100,
    modifier: 1,
    slideShadows: true,
  },
  loop:true,
  // pagination: {
  //   el: ".swiper-pagination",
  // },
//     autoplay: {
//     delay: 1000,
// },
});


