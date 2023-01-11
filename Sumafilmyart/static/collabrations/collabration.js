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
      enctype:'multipart/form-ata',
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
          // $('#enquiresform')[0].reset();
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


// $(document).on('submit', '#ideaform', function(event){
//   event.preventDefault();
//   $('.returnmessage').html(" ")
//   $.ajax({
//       type:'POST',
//       url:'/ideas/',
//       cache: false,
//       processData: false,
//       contentType: false,
//       enctype:'multipart/form-data',
    
//       data:{
//           name:$('#name').val(),
//           email:$('#email').val(),
//           phone:$('#phone').val(),
//           subject:$('#subject').val(),
//           file:$('#file')[0].files[0],
//           csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
//       },  
         
//       success:function(data){
//           $('#enquiresform')[0].reset();
//           $('.returnmessage').append("Your message has been received, We will contact you soon.")
//       },
//       error:function(data){
//           $('.returnmessage').append("Your message has been faild, please try agian.")
//       }
//   })
// })




// collaboration form 

$(document).on('submit', '#collaborationform', function(event){
  event.preventDefault();
  $('.returnmessage').html(" ")
  // type0f_collaborations = $("input:checkbox[name=check]:checked").each(myfunction ().val()); 
  
    // alert("Id: " + $(this).attr("id") + " Value: " + $(this).val());

  $.ajax({
      type:'POST',
      url:'/collaborations/',
      cache:false,
      enctype:'multipart/form-ata',
      data:{
          firstname:$('#firstname').val(),
          lastname:$('#lastname').val(),
          email:$('#email').val(),
          phone:$('#phone').val(),
          brand:$('#brand').val(),
          industry:$('#industry').val(),
          collaboration_type:$("input:checkbox[name=check]:checked").each(myfunction ().val()),
  
          




          file:$('#file')[0].files[0],
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },  
         
      success:function(data){
          // $('#enquiresform')[0].reset();
          $('.returnmessage').append("Your message has been received, We will contact you soon.")
      },
      error:function(data){
          $('.returnmessage').append("Your message has been faild, please try agian.")
      }
  })
})





// sponcership form 

$(document).on('submit', '#sponsorshipform', function(event){
  event.preventDefault();
  $('.returnmessage').html(" ")

  $.ajax({
      type:'POST',
      url:'/collaborations/',
      cache:false,
      enctype:'multipart/form-ata',
      data:{
          firstname:$('#firstname').val(),
          lastname:$('#lastname').val(),
          email:$('#email').val(),
          phone:$('#phone').val(),
          brand:$('#brand').val(),
          industry:$('#industry').val(),
          Kind_Sponcer:$('#inputState').val(),
          Sponcer_Type:$('#inputDistrict').val(),
          
          collaboration_type:$("input:checkbox[name=check]:checked").each(myfunction ().val()),
  
          




          file:$('#file')[0].files[0],
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },  
         
      success:function(data){
          // $('#enquiresform')[0].reset();
          $('.returnmessage').append("Your message has been received, We will contact you soon.")
      },
      error:function(data){
          $('.returnmessage').append("Your message has been faild, please try agian.")
      }
  })
})
