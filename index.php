<?php
	try{
		$connexion = new PDO('mysql:host=localhost;charset=UTF8;dbname=E145773Z','E145773Z','E145773Z');
		$connexion->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
		$query="select * from commentaires;";
		$result=$connexion->query($query)->fetchAll();
	}

	catch(PDOException $e){
		echo "problème avec la Bd";
	}
?>

<!DOCTYPE html>
<head>
	<meta charset="utf-8" />
	<link rel="stylesheet" type="text/css" href="style/bdd.css" media="screen" />
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
	<script type="text/javascript" src="script/bdd.js"></script>
</head>

<body>
  <h1> Recherche d'équipements sportifs </h1>

	<label for="type">type de recherche</label>
	<select id="type" name="type">
		<option value="installations">Installations</option>
		<option value="activites">Activit&eacutes</option>
		<option value="equipements">&Eacutequipements</option>
	</select><br/>

	<span id="toggable">
		<span id="installations">
			<label for="geo">localisation</label>
			<input id="geo" type="text" name="geo" value=""/><br/>
			<label for="InsCodePostal">code postal</label>
			<input id="InsCodePostal" type="number" name="InsCodePostal" value=""/><br/>
		</span>

		<span id="activites">
			<label for="ActLib">nom de l\'activit&eacute</label>
			<input id="ActLib" type="text" name="ActLib" value=""/><br/>
			<label for="EqActivitePratiquable">inclure les activit&eacutes pour lesquelles il ne reste plus de place</label>
			<input id="EqActivitePratiquable" type="checkbox" value="EqActivitePratiquable"/><br/>
			<label for="EqActivitePratique">exclure les activit&eacutes auxquelles personne ne participe</label>
			<input id="EqActivitePratique" type="checkbox" value="EqActivitePratique"/><br/>
			<label for="EqActiviteSalleSpe">exclure les activit&eacutes requérant une salle sp&eacutecialis&eacute</label>
			<input id="EqActiviteSalleSpe" type="checkbox" value="EqActiviteSalleSpe"/><br/>
		</span>

		<span id="equipements">
			<label for="EqNom">nom de l\'&eacutequipement</label>
			<input id="EqNom" type="text" name="EqNom" value=""/><br/>
			<label for="EquipementTypeLib">type d\'&eacutequipement</label>
			<input id="EquipementTypeLib" type="number" name="EquipementTypeLib" value=""/><br/>
			<label for="nature">nature</label>
			<input id="nature" name="EquipementFiche" type="radio" value="nature"/><br/>
			<label for="generique">g&eacutenerique</label>
			<input id="generique" name="EquipementFiche" type="radio" value="generique"/><br/>
		</span>
	</span>

  <label for="recherche">Rechercher</label>
	<input id="recherche" type="text" name="recherche"value=""/> <br/>

  <table>
		<thead>
			<tr><td colspan="4" class="unite"> installations sportives </td></tr>
			<tr>
 				<th class="etendue-colonne" id="YC32">Nom</th>
 				<th class="etendue-colonne" id="YC33">Commentaire</th>
 			</tr>
		</thead>
		<tbody>

			<!--?
			foreach ($result as $adherent){
				echo "<tr>";
				echo "<td>".$adherent['nom']."</td>";
				echo "<td>".$adherent['message']."</td>";
				echo "</tr>";
			}
			?-->

		</tbody>
  </table>
</body>
