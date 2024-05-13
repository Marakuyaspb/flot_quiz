function showDetails(event){
	
 	const clickedElement = event.currentTarget;
  	const currentID = clickedElement.id;
    
    const element = document.getElementById(currentID);
    // Mark it
    element.classList.add('i_was_clicked');;
  	
   	for (let i = 0; i < POOL.length; ++i) {
		if (POOL[i].id == currentID){

  			let questionAllDetails = POOL[i];

		/* hide current html */
  			ROOT_QUESTIONS.classList.add('hide_it');
  			ROOT_DETAIL.classList.remove('hide_it');

  		

		/* define vars */
			let id = questionAllDetails.id;
			let qiestion = questionAllDetails.qiestion;
			let icon = questionAllDetails.icon;
			let category = questionAllDetails.category;
  			let questions_details = document.getElementById('questions_details');

  			questions_details.innerHTML = 
			`<h5 id="${id}" class="the_question mb-4 mx-2">${qiestion}</h5>
			</div>
			`; 
  			
			let a = Object.keys(questionAllDetails.answers);
			for (let i = 0; i < a.length; ++i) {
			  let key = a[i];
			  let value = questionAllDetails.answers[key];

			  document.getElementById("add_answers").innerHTML += `
			  <center>
			  	<button id='${value}' class='${category} answer_btn mb-3 mx-2' onclick='checkResult(event);'>${key}</button>
			  </center>
			  `;
			}
		}
	}
}


function saveQuizInteraction(data) {
  fetch('/save_quiz_interaction/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.message);
  })
  .catch(error => {
    console.error('Error:', error);
  });
}



function isLoose(){
	current_score_heart = document.getElementById("score_heart");
	let score_heart_int = parseInt(current_score_heart.innerHTML);
	
	if (score_heart_int < 1) {
		let no = document.getElementById("no");
		no.remove();

		let loose = document.getElementById("loose");
		loose.classList.remove('hide_it');
	}
}



function isAlredyWin(){
	pins = document.getElementsByClassName("q_pin");

	if (pins.length == 0) {
  		let yes = document.getElementById("yes");
		yes.remove();

		let win = document.getElementById("win");
		win.classList.remove('hide_it');
	}	
}


function checkResult(event){
	const clickedAnswer = event.currentTarget;
  	const currentVar = clickedAnswer.id;

  	let yes = document.getElementById("yes");
  	let no = document.getElementById("no");
  	
  	let clicked_pin = document.querySelector(".i_was_clicked");

  	ROOT_RESULT.classList.remove('hide_it');
  	

  	if (currentVar === 'false') {
  		ScoreHeart();
  		isLoose();

  		ROOT_DETAIL.classList.add('hide_it');
  		no.classList.remove('hide_it');
  		yes.classList.add('hide_it');	
  	} 
  	else if (currentVar === 'true') {
  		/* remove pin */
  		clicked_pin.remove();
  		

  		/* add score*/
  		if (clickedAnswer.classList.contains('tech')) {
  			ScoreTech();  	
		} 
		else if (clickedAnswer.classList.contains('general')) {
			ScoreGeneral();
		}

		isAlredyWin();

  		ROOT_DETAIL.classList.add('hide_it');
  		yes.classList.remove('hide_it');
  		no.classList.add('hide_it');

  	} 
  	else {
  		console.log('check your life!');
  	}

	add_answers = document.getElementById("add_answers");
  	while (add_answers.firstChild) {
    	add_answers.removeChild(add_answers.firstChild);
	}



	const data = {
		play_session_id: /* generate unique session ID */,
		timezone: new Date().getTimezoneOffset(),
		question_id: /* get question ID */,
		category: /* get category */,
		answer: currentVar === 'True' ? true : false
	};

	// Save quiz interaction data
	saveQuizInteraction(data);
}

function playNext(event) {
	ROOT_QUESTIONS.classList.remove('hide_it');
	ROOT_RESULT.classList.add('hide_it');
}