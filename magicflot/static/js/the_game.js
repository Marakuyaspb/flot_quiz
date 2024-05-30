function showGame(event){
	ROOT_GAME.classList.remove('hide_it');
	ROOT_START.classList.add('hide_it');
	console.log('showGame');
}

// Very first JSON skeleton
let gameSession = {
  game_session_id: "0",
  time: "",
  how_it_was: {
    answered_questions: []
  }
};

// Unique ID for the game session
function startGame(event) {
  gameSession.game_session_id = Date.now().toString();
  gameSession.time = new Date(Date.now()).toLocaleString();
}


window.addEventListener('beforeunload', async (event) => {
  event.preventDefault();
  
  try {
    await saveGameSession();
  } catch (error) {
    console.error("Error saving game session data:", error);
  }

});



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



function saveGameSession() {
  return new Promise((resolve, reject) => {
    const gameSessionData = JSON.stringify(gameSession);
    const csrftoken = getCookie('csrftoken');

    fetch("/save_game_session/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken
      },
      body: gameSessionData,
    })
    .then(response => resolve(response))
    .catch(error => reject(error));
  });
}


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}



async function checkResult(event){
	if (gameSession.game_session_id === "0") {
	    startGame();
	  }


	const full_category = event.target.className;
	const category = full_category.charAt(0);

	const question = event.target.parentNode.classList.value;
	const value = event.target.id;
console.log(question);
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
