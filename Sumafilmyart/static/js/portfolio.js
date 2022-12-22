
// lakku kikku slider 
var swiper = new Swiper(".port_video_slider1", {
    slidesPerView:3,
        spaceBetween: 30,
        freeMode: true,
        loop:true,
        
        autoplay: {
        delay: 5000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
        },
        breakpoints: {
          // when window width is >= 320px
          320: {
            slidesPerView: 1,
            
          },
          // when window width is >= 480px
          480: {
            slidesPerView: 2,
          
          },
          // when window width is >= 640px
          640: {
            slidesPerView: 3,
            
          }
        }
  });

// lakku kikku slider 


// lakku kikku slider 


// lakku kikku slider 


// lakku kikku slider 


// lakku kikku slider 

    // Project carousel
    $(".project-carousel").owlCarousel({
      
      smartSpeed: 1000,
      margin: 0,
      loop: true,
      responsive:	true,
      center: true,
      dots: false,
      nav: false,
      navText : [
          '<i class="bi bi-chevron-left"></i>',
          '<i class="bi bi-chevron-right"></i>'
      ],
      
      responsive: {
    0:{
              items:1
          },
          576:{
              items:1
          },
          768:{
              items:2
          },
          992:{
              items:3
          }
      }
  });




  (function ($) {
    "use strict";

  var portfolioIsotope = $('.portfolio-container').isotope({
    itemSelector: '.portfolio-item',
    layoutMode: 'fitRows'
});
$('#portfolio-flters li').on('click', function () {
    $("#portfolio-flters li").removeClass('active');
    $(this).addClass('active');

    portfolioIsotope.isotope({filter: $(this).data('filter')});
});



})(jQuery);