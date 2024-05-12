let score_general = 0;
let score_technical = 0;
let score_heart = 5;

function ScoreGeneral(){
	score_general++;
	document.getElementById("score_general").innerHTML = score_general;
}

function ScoreTech(){
	score_technical++;
	document.getElementById("score_technical").innerHTML = score_technical;
}

function ScoreHeart(){
	score_heart--;
	document.getElementById("score_heart").innerHTML = score_heart;
}