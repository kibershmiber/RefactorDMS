$(document).ready(function(){

$('#searchvalue').keypress(function (e) {
  if (e.which == 13) {
        csrf = $("input[name='csrfmiddlewaretoken']").val();
        int = 0;


      if($.isNumeric($(this).val())){
          int = 1;
      }


      $.ajax({
         method: "POST",
          url: "/search",
          data: {'value': $(this).val(),'csrfmiddlewaretoken': csrf,'int': int },
          beforeSend: function(){
              $("#searchvalue").attr("placeholder", "Шукаємо... Зачекайте, будь ласка").val("").focus().blur().prop('disabled', true);
          },
          complete: function(){
              $("#searchvalue").attr("placeholder", "Введіть назву документу, шифр або його інвентарний номер. ").prop('disabled', false);
          },
          success : function(datasuccess) {
               $('.content').html(datasuccess);
          }
      });


    $('#searchvalue').submit();
    return false;

  }
});
    });
