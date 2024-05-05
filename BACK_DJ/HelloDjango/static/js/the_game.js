function showDetails(event){
	let clicked_el = event.target;
    clicked_el.classList.add('i_was_clicked');;
  	
  	let q_pin = document.getElementsByClassName('q_pin');
  	let the_question = document.getElementsByClassName('the_question');
  	let questions_all = document.getElementById('questions_all');


  	questions_all.classList.add('hide_it');

  	for (let i = 0; i < the_question.length; i++) {
    if (the_question[i].id === clicked_el.id) {
      the_question[i].classList.remove('hide_it');
    } 
  }
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

  	let yes = document.getElementById("True");
  	let no = document.getElementById("False");
  	
  	let clicked_pin = document.querySelector(".i_was_clicked");

  	//ROOT_RESULT.classList.remove('hide_it');
  	

  	if (currentVar === 'False') {
  		ScoreHeart();
  		isLoose();

  		//ROOT_DETAIL.classList.add('hide_it');
  		no.classList.remove('hide_it');
  		yes.classList.add('hide_it');	
  	} 
  	else if (currentVar === 'True') {
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

  		//ROOT_DETAIL.classList.add('hide_it');
  		yes.classList.remove('hide_it');
  		no.classList.add('hide_it');

  	} 
  	else {
  		console.log('check json!');
  	}

	add_answers = document.getElementById("add_answers");
  	while (add_answers.firstChild) {
    	add_answers.removeChild(add_answers.firstChild);
	}
}

function playNext(event) {
	//ROOT_QUESTIONS.classList.remove('hide_it');
	//ROOT_RESULT.classList.add('hide_it');
}