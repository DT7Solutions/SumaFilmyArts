let upload_btn = document.querySelector('.choosefile');

function yesnoCheck(checkbox) {
    if(checkbox.checked == true){
        document.getElementById("ifYes").style.display = "block";
    
       
        // document.getElementById("submit").removeAttribute("disabled");
    }else{
        // document.getElementById("submit").setAttribute("disabled", "disabled");
        document.getElementById("ifYes").style.display = "none";
   }
}






var sponcer = ["TV Show ","Web Series ","Short Film","Film","Youtube Video"];
var BrandAmbassador = [""];


$("#inputState").change(function(){
  var StateSelected = $(this).val();
  var optionsList;
  var htmlString = "";

  switch (StateSelected) {
    case "sponcer":
        optionsList = sponcer;
        break;
    case "BrandAmbassador":
        optionsList = BrandAmbassador;
        break;
    
}

  for(var i = 0; i < optionsList.length; i++){
    htmlString = htmlString+"<option value='"+ optionsList[i] +"'>"+ optionsList[i] +"</option>";
  }
  $("#inputDistrict").html(htmlString);

});



// enquiries form 
$(document).on('submit', '#enquiresform', function(event){
  event.preventDefault();
  $('.returnmessage').html(" ")
  $.ajax({
      type:'POST',
      url:'/enquiries/',
      cache:false,
      enctype:'multipart/form-data',
      data:{
          firstname:$('#firstname').val(),
          lastname:$('#lastname').val(),
          email:$('#email').val(),
          phone:$('#phone').val(),
          subject:$('#subject').val(),
          message:$('#message').val(),
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },  
         
      success:function(data){
          $('#enquiresform')[0].reset();
          $('.returnmessage').append("Your message has been received, We will contact you soon.")
      },
      error:function(data){
          $('.returnmessage').append("Your message has been faild, please try agian.")
      }
  })
})



// your ideas form 
$(document).ready(function(){
 $('.submit').click(function(){
  let fname= $('#fname').val()
  let email = $('#email').val()
  let phone =$('#phone').val()
  let subject = $('#subject').val()
  csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
  
  let data = new FormData();
  data.append("fname", fname);
  data.append("email",email);
  data.append("phone",phone);
  data.append("subject",subject);
  data.append("file",$("input[id^='file']")[0].files[0]);
  data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
  


  $.ajax({
        url:"/ideas/",
        method: 'Post',
        processData:false,
        contentType:false,
        cache:false,
        mimeType:"multipart/form-data",
        data:data,
        
        success:function(data){
            $('#ideaform')[0].reset();
            $('.returnmessage').append("Your message has been received, We will contact you soon.")
        },
        error:function(data){
            $('.returnmessage').append("Your message has been faild, please try agian.")
        }
    })

 })

})




// sponcership form 
$(document).ready(function(){
    $('#sponcerid').click(function(){
        let firstname = $('#firstname').val()
        let lastname = $('#lastname').val()
        let email = $('#email').val()
        let phone = $('#phone').val()
        let brand = $('#brand').val()
        let industry = $('#industry').val()
        let Kind_Sponcer = $('#inputState').val()
        let Sponcer_Type = $('#inputDistrict').val()
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
    
     
     let data = new FormData();
     data.append("firstname", firstname);
     data.append("lastname", lastname);
     data.append("email",email);
     data.append("phone",phone);
     data.append("brand",brand);
     data.append("industry",industry);
     data.append("Kind_Sponcer",Kind_Sponcer);
     data.append("Sponcer_Type",Sponcer_Type);
     data.append("file",$("input[id^='file']")[0].files[0]);
     data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
     
   
   
     $.ajax({
           url:"/sponsorship/",
           method: 'Post',
           processData:false,
           contentType:false,
           cache:false,
           mimeType:"multipart/form-data",
           data:data,
           
           success:function(data){
               $('#sponsorshipform')[0].reset();
               $('.returnmessage').append("Your message has been received, We will contact you soon.")
           },
           error:function(data){
               $('.returnmessage').append("Your message has been faild, please try agian.")
           }
       })
   
    })
   
   })
   



// collaboration form 
$(document).ready(function(){
    $('#collaboration-submit').click(function(){
        let firstname = $('#firstname').val()
        let lastname = $('#lastname').val()
        let email = $('#email').val()
        let phone = $('#phone').val()
        let brand = $('#brand').val()
        let industry = $('#industry').val()
        let Collaboration_Type = $('input[name="check"]:checked').val();
        let colbtype = ''
        if (Collaboration_Type == 'Other'){
            colbtype = $('#ifYes').val()
        }
        else{
            colbtype = $('input[name="check"]:checked').val();
        }
        // let Sponcer_Type = $('#inputDistrict').val()
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
      
     
     let data = new FormData();
     data.append("firstname", firstname);
     data.append("lastname", lastname);
     data.append("email",email);
     data.append("phone",phone);
     data.append("brand",brand);
     data.append("industry",industry);
     data.append("Collaboration_Type",colbtype);
    //  data.append("Sponcer_Type",Sponcer_Type);
     data.append("file",$("input[id^='file']")[0].files[0]);
     data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
     
   
   
     $.ajax({
           url:"/collaborations/",
           method: 'Post',
           processData:false,
           contentType:false,
           cache:false,
           mimeType:"multipart/form-data",
           data:data,
           
           success:function(data){
               $('#collaborationform')[0].reset();
               $('.returnmessage').append("Your message has been received, We will contact you soon.")
           },
           error:function(data){
               $('.returnmessage').append("Your message has been faild, please try agian.")
           }
       })
   
    })
   
   })
   

 
  
  
