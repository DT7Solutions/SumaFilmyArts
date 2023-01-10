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






var AndraPradesh = ["TV Show ","Web Series ","Short Film","Film","Youtube Video"];
var ArunachalPradesh = [""];


$("#inputState").change(function(){
  var StateSelected = $(this).val();
  var optionsList;
  var htmlString = "";

  switch (StateSelected) {
    case "Andra Pradesh":
        optionsList = AndraPradesh;
        break;
    case "Arunachal Pradesh":
        optionsList = ArunachalPradesh;
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
