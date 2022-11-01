
$(document).on('submit', '#contact_form', function(event){
    event.preventDefault();
    $('.returnmessage').html(" ")
    $.ajax({
        type:'POST',
        url:'/contact/',
        cache:false,
        enctype:'multipart/form-ata',
        data:{
            name:$('#name').val(),
            email:$('#email').val(),
            phone:$('#phone').val(),
            subject:$('#subject').val(),
            message:$('#message').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },  
           
        success:function(data){
            $('#contact_form')[0].reset();
            $('.returnmessage').append("Your message has been received, We will contact you soon.")
        },
        error:function(data){
            $('.returnmessage').append("Your message has been faild, please try agian.")
        }
    })
})
