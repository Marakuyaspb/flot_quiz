function showGame(event){
	ROOT_GAME.classList.remove('hide_it');
	ROOT_START.classList.add('hide_it');
}

// Very first JSON skeleton
let gameSession = {
  game_session_id: "0",
  end_game_time: "",
  how_it_was: {
    answered_questions: []
  }
};

// Unique ID for the game session
function startGame(event) {
  gameSession.game_session_id = Date.now().toString(); 
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
		ROOT_NO.remove();
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
	ROOT_PINS.classList.remove('hide_it');
	ROOT_RESULT.classList.add('hide_it');
}


function checkResult(event){
	if (gameSession.game_session_id === "0") {
	    startGame();
	  }

	const question = event.target.parentNode.innerText.trim();
  const category = event.target.className;
  const value = event.target.id;

  const answeredQuestion = {
    question: question,
    category: category,
    value: value
  };

	gameSession.how_it_was.answered_questions.push(answeredQuestion);



	const clickedAnswer = event.currentTarget;
	const currentVar = clickedAnswer.id;
	let clicked_pin = document.querySelector(".i_was_clicked");
	let currQ = document.querySelector(".currQ");



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


// Save the game session data to JSON before the page is closed or reloaded
/*window.addEventListener('beforeunload', function() {
  gameSession.end_game_time = new Date().toLocaleString();
  const jsonData = JSON.stringify(gameSession, null, 2);

  // Send the JSON data to the server using AJAX
  fetch('/save_game_session/', {
    method: 'POST',
    body: JSON.stringify({ data: jsonData }),
    headers: {
      'Content-Type': 'application/json'
    }
  });
});*/