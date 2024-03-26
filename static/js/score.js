let score_general = 0;
let score_tech = 0;

function ScoreGeneral(){
	score_general++;
	document.getElementById("score_general").innerHTML = score_general;

}

function ScoreTech(){
	score_tech++;
	document.getElementById("score_tech").innerHTML = score_tech;
}