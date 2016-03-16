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

			<?
			foreach ($result as $adherent){
				echo "<tr>";
				echo "<td>".$adherent['nom']."</td>";
				echo "<td>".$adherent['message']."</td>";
				echo "</tr>";
			}
			?>

		</tbody>
  </table>
</body>
