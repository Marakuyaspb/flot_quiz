class Questions {

	render() {

		
		let htmlPins = '';
		
		POOL.forEach(({category, icon}) => {
			
			htmlPins += `
			
			<img class='${category}' src='${icon}' onclick=''>
			`;
			});
			console.log(htmlPins);


			const html = `
			
			<div class="questions_container">	
					${htmlPins}
			</div>
		`;
		ROOT_QUESTIONS.innerHTML = html;
		
		}
	}
console.log('Questions rendered!');
const questionsPage = new Questions();