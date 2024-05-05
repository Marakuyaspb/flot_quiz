/* ROOT*/
const ROOT_QUESTIONS = document.getElementById('questions_all');
const ROOT_DETAIL = document.getElementById('the_question');
const ROOT_RESULT = document.getElementById('result');

const ROOT_SPINNER = document.getElementById('spinner');
const ROOT_ERROR = document.getElementById('error');

let currentID;


class Questions {
	render() {
		let generalCount = 0;
		let techCount = 0;
		let selectedItems = [];

	// Shuffle the POOL array
		const shuffledPool = POOL.sort(() => Math.random() - 0.5);
		const uniqueIds = new Set();

		shuffledPool.forEach( ({ id, question, answers, icon, category }) => {

			if (uniqueIds.has(id)) {
			    return; // Skip this item if the ID is already in the set
			  }


			if (category === 'general' && generalCount < 7) {
				selectedItems.push({ id, question, answers, icon, category });
				generalCount++;
			} 
			else if (category === 'tech' && techCount < 8) {
				selectedItems.push({ id, question, answers, icon, category });
				techCount++;
			}

			if (selectedItems.length === 15) {
				return;
			}
		});



		let htmlPins = '';	
		selectedItems.forEach(({id, qiestion, answers, icon, category}) => {	
			htmlPins += `
			<img id='${id}' class='q_pin ${category}' src="${icon}" onclick='showDetails(event);'>
			`;
			});

			const html = `
			<div class="questions_container pt-5">	
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

	fetch('https://%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B2%D0%BE%D0%BB%D1%88%D0%B5%D0%B1%D0%BD%D1%8B%D1%85%D0%BA%D0%BE%D1%80%D0%B0%D0%B1%D0%BB%D0%B5%D0%B9.%D1%80%D1%84/static/qu.json')
	
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