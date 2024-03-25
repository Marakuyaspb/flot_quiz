/* ROOT*/
const ROOT_QUESTIONS = document.getElementById('questions_all');
const ROOT_DETAIL = document.getElementById('the_question');
const ROOT_RESULT = document.getElementById('result');

const ROOT_SPINNER = document.getElementById('spinner');
const ROOT_ERROR = document.getElementById('error');

let currentID;

class Questions {
	render() {
		let htmlPins = '';	
		POOL.forEach(({id, qiestion, answers, icon, category}) => {	
			htmlPins += `
			<img id='${id}' class='q_pin ${category}' src='${icon}' onclick='showDetails(event);'>
			`;
			});

			const html = `
			<div class="questions_container">	
					${htmlPins}
			</div>
		`;
		ROOT_QUESTIONS.innerHTML = html;
	}
}
const questionsPage = new Questions();


class Spinner {
    handleClear() {
        ROOT_SPINNER.innerHTML = '';
    }

    render() {
        const html = `
        	<div class="spinner-container">
        		<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto; background: none; display: block; shape-rendering: auto;" width="211px" height="211px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
                <circle cx="50" cy="50" r="28" stroke-width="4" stroke="#bfbfbf" stroke-dasharray="43.982297150257104 43.982297150257104" fill="none" stroke-linecap="round" transform="rotate(217.184 50 50)">
                  <animateTransform attributeName="transform" type="rotate" repeatCount="indefinite" dur="1.0989010989010988s" keyTimes="0;1" values="0 50 50;360 50 50"></animateTransform>
                </circle>
                </svg>
        	</div>`;
        ROOT_SPINNER.innerHTML = html;
    }
}
const spinnerPage = new Spinner();

class Error {
    render() {
        const html = `
        	<div class="container">
                <div class="error-message">
                    <h3>Технические работы</h3>
                    <p>Извините за неудобства. Скоро всё обновим!</p>
                </div>
        	</div>
        `;

        ROOT_ERROR.innerHTML = html;
    }
}

const errorPage = new Error();

/* RENDER */
function render() {
	questionsPage.render();	
}
spinnerPage.render();
let POOL = [];
render();

fetch('http://zdgalepv.beget.tech/static/qu.json')
	    .then(res => res.json())
	    .then(body => {
			POOL = body;
			setTimeout(() => {
				spinnerPage.handleClear();
				render();
			}, 1000);
	    })
	    .catch(() => {
	        spinnerPage.handleClear();
	    	errorPage.render();
	    })



function showDetails(event){
	
 	const clickedElement = event.currentTarget;
  	const currentID = clickedElement.id;
  	
   	for (let i = 0; i < POOL.length; ++i) {	
		if (POOL[i].id == currentID){

  			let questionAllDetails = POOL[i];

	/* hide current html */
  			ROOT_QUESTIONS.classList.add('hide_it');
  			ROOT_DETAIL.classList.remove('hide_it');

	/* define vars */
			let qiestion = questionAllDetails.qiestion;
			let icon = questionAllDetails.icon;
			let category = questionAllDetails.category;
			
			
	/* render new html about the single product */
  			let questions_details = document.getElementById('questions_details');

  			questions_details.innerHTML = 
			`<h5 class="the_question mb-5 mx-5">${qiestion}</h5>
			</div>
			`; 
  			
			let a = Object.keys(questionAllDetails.answers);
			for (let i = 0; i < a.length; ++i) {
			  let key = a[i];
			  let value = questionAllDetails.answers[key];
			  console.log(value);

			  document.getElementById("add_answers").innerHTML += `<button id='${value}' class='answer_btn mb-3 mx-5' onclick='checkResult(event);'>${key}</button>
			  `;
			}
		} /*else console.log('Check your json!')*/;
	}
	/*return currentID;*/
}

function checkResult(event){
	const clickedAnswer = event.currentTarget;
  	const currentVar = clickedAnswer.id;

  	let yes = document.getElementById("yes");
  	let no = document.getElementById("no");
  	let win = document.getElementById("win");
  	/*console.log(currentVar);*/

  	add_answers = document.getElementById("add_answers");
  	while (add_answers.firstChild) {
    add_answers.removeChild(add_answers.firstChild);
	}
  	
  	console.log(currentID);

  	if (currentVar === 'false') {
  		ROOT_DETAIL.classList.add('hide_it');
  		no.innerHTML += `
  			<h5>Не верно :( </h5>
			<p>Попробуй пока ответить на другие вопросы!
				
				<center>
					<button type="button" class="btn btn-danger" onclick='playNext(event);'>Попробую ещё</button>
				</center>
			  `;
  		no.classList.remove('hide_it');

  		
  	} else if (currentVar === 'true') {
  		ROOT_DETAIL.classList.add('hide_it');

  		yes.innerHTML += `
  			<h5>Отлично!</h5>
  			<p>Это верный ответ.</p>
				<center>
					<button type="button" class="btn btn-success" onclick='playNext(event);'>Дальше</button>
				</center>
			  `;
  		yes.classList.remove('hide_it');
  	}
}

function playNext(event) {
	ROOT_RESULT.classList.add('hide_it');
	ROOT_QUESTIONS.classList.remove('hide_it');
}