// let more_info_btn = document.querySelector('.apply-btn');
// let my_model = document.querySelector(".more-info-model1");
// let close_btn = document.querySelector('.model-close');

// more_info_btn.addEventListener('click', function(){
//     my_model.classList.add('model-active')
//     // alert('its working!')
// })
// close_btn.addEventListener('click',function(){
//     my_model.classList.remove('model-active')
// })


// $(document).on('submit', '#enquiresform', function(event){
//     event.preventDefault();
  

// your ideas form 
$(document).ready(function(){
    $('#applyjob').click(function(event){
     event.preventDefault();
     let firstname= $('#firstname').val()
     let lastname= $('#lastname').val()
     let email = $('#email').val()
     let phone =$('#phone').val()
     let userexperices =$('#userexperices').val()
   
     csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
     
     let data = new FormData();
     data.append("firstname", firstname);
     data.append("lastname", lastname);
     data.append("email",email);
     data.append("phone",phone);
     data.append("userexperices",userexperices);
     data.append("file",$("input[id^='file']")[0].files[0]);
     data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
     
   
   
     $.ajax({
           url:"/apply/",
           method: 'Post',
           processData:false,
           contentType:false,
           cache:false,
           mimeType:"multipart/form-data",
           data:data,
           
           success:function(data){
               $('#clearform')[0].reset();
               $('.returnmessage').append("Your Application Submited Sucessfully, We will contact you soon.")
           },
           error:function(data){
               $('.returnmessage').append("Your Application Faild to submite , please try agian.")
           }
       })
   
    })
   
   })
   