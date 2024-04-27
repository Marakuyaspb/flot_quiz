let score_general = 0;
let score_tech = 0;
let score_heart = 5;

function ScoreGeneral(){
	score_general++;
	document.getElementById("score_general").innerHTML = score_general;
}

function ScoreTech(){
	score_tech++;
	document.getElementById("score_tech").innerHTML = score_tech;
}

function ScoreHeart(){
	score_heart--;
	document.getElementById("score_heart").innerHTML = score_heart;
}