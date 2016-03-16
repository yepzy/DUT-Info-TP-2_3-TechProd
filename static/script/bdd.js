$(document).ready(function(){

  $("span[id=toggable] > span").hide();
  $("span[id="+$("select[id=type]").value+"]").show();

  $("select[id=type]").on('change', function(){
    //$("body").html("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj");
    var s = this.value;
    $("span[id=toggable] > span").hide();
    $("span[id="+s+"]").show();
  });
});
