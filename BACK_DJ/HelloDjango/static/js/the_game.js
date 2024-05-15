let gameSessionData = {
    session_id: 'unique_session_id', 
    timezone: new Date().getTimezoneOffset(),
    questions: []
};


function startGame(event){
	ROOT_GAME.classList.remove('hide_it');
	ROOT_START.classList.add('hide_it');
}


function showDetails(event){
	let clicked_el = event.target;
    clicked_el.classList.add('i_was_clicked');;
  	
  	let q_pin = document.getElementsByClassName('q_pin');
  	let the_question = document.getElementsByClassName('the_question');
  	let questions_all = document.getElementById('questions_all');


  	ROOT_PINS.classList.add('hide_it');

  	for (let i = 0; i < the_question.length; i++) {
    if (the_question[i].id === clicked_el.id) {
      the_question[i].classList.remove('hide_it');
      the_question[i].classList.add('currQ');
    } 
  }
}


function isLoose(){
	current_score_heart = document.getElementById("score_heart");
	let score_heart_int = parseInt(current_score_heart.innerHTML);
	
	if (score_heart_int < 1) {
		/*let no = document.getElementById("no");*/
		ROOT_NO.remove();

		/*let loose = document.getElementById("loose");*/
		ROOT_LOOSE.classList.remove('hide_it');
	}
}


function isAlredyWin(){
	let q_pin = document.getElementsByClassName("q_pin");

	if (q_pin.length == 0) {
		ROOT_YES.remove();
		ROOT_WIN.classList.remove('hide_it');
	}	
}


function playNext(event) {
	console.log('next!');
	ROOT_PINS.classList.remove('hide_it');
	ROOT_RESULT.classList.add('hide_it');
}

/*function getCurrQuestion(event) {
	const clickedEl = event.currentTarget;
	const currQuestion = clickedEl.classList;
}*/

function checkResult(event){
	const clickedAnswer = event.currentTarget;
	const currentVar = clickedAnswer.id;
	let clicked_pin = document.querySelector(".i_was_clicked");
	let currQ = document.querySelector(".currQ");


	const questionData = {
        question: currQ,
        category: clickedAnswer.classList[0],
        value: currentVar
    };
    gameSessionData.questions.push(questionData);


	
	currQ.classList.remove('hide_it');
	ROOT_PINS.classList.add('hide_it');

	if (currentVar === 'True') {
		clicked_pin.remove();
		console.log(currentVar);
	/* add score */
		if (clickedAnswer.classList.contains('technical')) {
			ScoreTech();  	
		} 
		else if (clickedAnswer.classList.contains('general')) {
			ScoreGeneral();
	}

	isAlredyWin();

	currQ.classList.add('hide_it');
	currQ.classList.remove('currQ');
	ROOT_RESULT.classList.remove('hide_it');
	ROOT_YES.classList.remove('hide_it');
	ROOT_NO.classList.add('hide_it');

} 
else if (currentVar === 'False') {
		ScoreHeart();
		isLoose();

		currQ.classList.add('hide_it');
		currQ.classList.remove('currQ');
		ROOT_RESULT.classList.remove('hide_it');
		ROOT_NO.classList.remove('hide_it');
		ROOT_YES.classList.add('hide_it');

	} else {
	console.log('check your life!');
	}	
}



window.addEventListener('beforeunload', function() {
    // Send the gameSessionData to Django view using AJAX before the page is closed or reloaded
    fetch('/save_game_session_data/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(gameSessionData)
    });
});