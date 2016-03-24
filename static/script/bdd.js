$(document).ready(function(){

  //on cache les menus qui ne sont pas selectionnés au début
  $("span[id=toggable] > span").hide();
  $("span[id="+$("select[id=type]").value+"]").show();

  //si on change de sélection on cache les autres sous-menus
  //et on ré-affiche le bon
  $("select[id=type]").on('change', function(){
    var s = this.value;
    $("span[id=toggable] > span").hide();
    $("span[id="+s+"]").show();
  });

  $("html").keydown(function(event) {
    if (event.which == 13) {
      window.alert($("input[id=geo]").val());
      $.ajax({
        url:'http://localhost:8080/'+$("select[id=type] > option:selected").val()+'/'+$("input[id=geo]").val()+'/'+$("input[id=InsCodePostal]").val(),
        type:'GET',
        jsoncallback:'json',
        datatype:'json',
        data:'',

        success:function(data, statut){
          $.each(data, function(i, item){
            $("table").html("<tr></tr>");
          });
        },

        error:function(resultat, statut, erreur){
          window.alert("Échec de  la réussite");
        },

        complete:function(resultat, statut){
          window.alert("Échec de l'échec: réussite");
        },
      });
    }
  });
});
