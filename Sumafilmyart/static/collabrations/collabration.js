let upload_btn = document.querySelector('.choosefile-COL');

function yesnoCheck(checkbox) {
    if(checkbox.checked == true){
        document.getElementById("ifYes").style.display = "block";
        upload_btn.style.bottom ="15%";
       
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