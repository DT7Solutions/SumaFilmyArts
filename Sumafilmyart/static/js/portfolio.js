
// lakku kikku slider 
var swiper = new Swiper(".port_video_slider1", {
    slidesPerView:3,
        spaceBetween: 30,
        freeMode: true,
        loop:true,
        autoplay: {
        delay: 5000,
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