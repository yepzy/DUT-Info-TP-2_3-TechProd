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
});
