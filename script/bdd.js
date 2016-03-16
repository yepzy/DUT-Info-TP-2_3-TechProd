$(document).ready(function(){

  $("select[id=type]").on('click', function(){
    $s =$(this).getValue();
    if(s == "installations") { $("span[id=toggable]").html(opt4install); }
    if(s == "activites") { $("span[id=toggable]").html(opt4activite); }
    if(s == "equipements") { $("span[id=toggable]").html(opt4equip); }
  });

  $opt4install="
  <span id=\"installations\">
			<label for=\"geo\">localisation</label>
			<input id=\"geo\" type=\"text\" name=\"geo\" value=\"\"/>
			<label for=\"InsCodePostal\">code postal</label>
			<input id=\"InsCodePostal\" type=\"number\" name=\"InsCodePostal\" value=\"\"/>
		</span>";
    $opt4activite="
    <span id=\"activites\">
			<label for=\"ActLib\">nom de l'activit&eacute</label>
			<input id=\"ActLib\" type=\"text\" name=\"ActLib\" value=\"\"/>
			<label for=\"EqActivitePratiquable\">inclure les activit&eacutes pour lesquelles il ne reste plus de place</label>
			<input id=\"EqActivitePratiquable\" type=\"checkbox\" value=\"EqActivitePratiquable\"/>
			<label for=\"EqActivitePratique\">exclure les activit&eacutes auxquelles personne ne participe</label>
			<input id=\"EqActivitePratique\" type=\"checkbox\" value=\"EqActivitePratique\"/>
			<label for=\"EqActiviteSalleSpe\">exclure les activit&eacutes requérant une salle sp&eacutecialis&eacute</label>
			<input id=\"EqActiviteSalleSpe\" type=\"checkbox\" value=\"EqActiviteSalleSpe\"/>
		</span>
    "
    $opt4equip="
    <span id=\"equipements\">
			<label for=\"EqNom\">nom de l'&eacutequipement</label>
			<input id=\"EqNom\" type=\"text\" name=\"EqNom\" value=""/>
			<label for=\"EquipementTypeLib\">type d'&eacutequipement</label>
			<input id=\"EquipementTypeLib\" type=\"number\" name=\"EquipementTypeLib\" value=\"\"/>
			<label for=\"nature\">nature</label>
			<input id=\"nature\" name=\"EquipementFiche\" type=\"radio\" value=\"nature\"/>
			<label for=\"generique\">nature</label>
			<input id=\"generique\" name=\"EquipementFiche\" type=\"radio\" value=\"generique\"/>
		</span>
    "


});
