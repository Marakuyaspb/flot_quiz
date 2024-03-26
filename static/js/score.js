function ScoreGeneral(answer){
	if (answer == true){ 
		score_general++;
		document.getElementById("score_general").innerHTML = score_general;
	}
}

function ScoreTech(answer){
	if (answer == true){ 
		score_tech++;
		document.getElementById("score_tech").innerHTML = score_tech;
	}
}