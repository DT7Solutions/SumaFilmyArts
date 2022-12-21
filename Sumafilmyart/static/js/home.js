
// let nav_item =  document.querySelector(".anchor_nav");
// let btns = nav_item.getElementsByClassName("nav-btn");
// for(let i = 0; i < btns.length; i++){
//   btns[i].addEventListener('click', function(){
//     let current = document.getElementsByClassName('active');
//     current[0].className = current[0].className.replace(' active');
//     this.className += ' active';
//   })
// }



 let homeElement = document.getElementById("home");
 let AboutElement = document.getElementById("about");
let Portfoliolement = document.getElementById("portfolio");
let newsElement = document.getElementById("news");
let carrerElement = document.getElementById("carrer");

function home() {
  homeElement.style.color="#f75203";
   AboutElement.style.color="#000";
   Portfoliolement.style.color="#000";
   newsElement.style.color="#000";
   carrerElement.style.color="#000";
}

function about(){
  homeElement.style.color="#000";
  AboutElement.style.color="#f75203";
  Portfoliolement.style.color="#000";
  newsElement.style.color="#000";
   carrerElement.style.color="#000";

}

function portfolio(){
  homeElement.style.color="#000";
  AboutElement.style.color="#000";
  Portfoliolement.style.color="#f75203";
  newsElement.style.color="#000";
   carrerElement.style.color="#000";

}
 function news(){
  homeElement.style.color="#000";
  AboutElement.style.color="#000";
  Portfoliolement.style.color="#000";
  newsElement.style.color="#f75203";
   carrerElement.style.color="#000";
 }
 function carrer(){
  homeElement.style.color="#000";
  AboutElement.style.color="#000";
  Portfoliolement.style.color="#000";
  newsElement.style.color="#000";
   carrerElement.style.color="#f75203";
 }
    // Portfolio isotope and filter
   

/* main slider */
var swiper = new Swiper(".mySwiper", {
    speed:400,
    loop:true,
    effect:"fade",

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
    effect:"fade",

    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
    autoplay: {
    delay: 5000,
    },
    breakpoints: {
      // when window width is >= 320px
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      // when window width is >= 480px
      480: {
        slidesPerView: 1,
        spaceBetween: 30
      },
      // when window width is >= 640px
      640: {
        slidesPerView: 3,
        spaceBetween: 40
      }
    }
  });

/* owl carsoul */
  $('.owl-carousel').owlCarousel({
    merge:true,
    loop :true,
    margin:10,
    items: 3,
    video:true,
    lazyload:true,
    center:true,
    autoplay:true,
    autoplayTimeout:3000,
    stagePadding:10,
    responsive:{
              0:{
                  items:1
                },
                600:{
                  items:1
                },
                800: {
                  items:2
                },
                1000:{
                  items:2
                },
                1100:{
                  items:3
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

// var owlPlugin = function() {
//   if ( $('.owl-3-slider').length > 0 ) {
//     var owl3 = $('.owl-3-slider').owlCarousel({
//       loop: true,
//       autoHeight: true,
//       margin: 20,
//       autoplay: true,
//       smartSpeed: 700,
//       items:2,
//       nav: true,
//       dots: true,
//       navText: ['<span class="icon-keyboard_backspace"></span>','<span class="icon-keyboard_backspace"></span>'],
//       responsive:{
//         0:{
//           items:1
//         },
//         600:{
//           items:1
//         },
//         800: {
//           items:2
//         },
//         1000:{
//           items:2
//         },
//         1100:{
//           items:3
//         }
//       }
//     });
//   }
// }



