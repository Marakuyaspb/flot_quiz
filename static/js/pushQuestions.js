class Questions {
	render() {
		let htmlPins = '';	
		POOL.forEach(({id, qiestion, answers, icon, category}) => {	
			htmlPins += `
			<img id='${id}' class='${category}' src='${icon}' onclick='showDetails();'>
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