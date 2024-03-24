function showDetails(event){
	
 	const clickedElement = event.currentTarget;
  	const currentID = clickedElement.id;
  	console.log(clickedElement, currentID);
  	
/* compare the clicked id with all ids in [] */
   	for (let i = 0; i < POOL.length; ++i) {	
		if (POOL[i].id == currentID){

/* create a new var with all info about the match id */
  			let questionAllDetails = POOL[i];
  			console.log(questionAllDetails);

/* remove current html */
  			var allProducts = document.getElementById('questions_show');
  			allProducts.remove();


/* define vars */
			let qiestion = questionAllDetails.qiestion;
			let icon = questionAllDetails.icon;
			let category = questionAllDetails.category;
			
  			console.log(category);
			
/* render new html about the single product */
  			document.getElementById('questions_details').innerHTML = 
			`
				<div class="modal" tabindex="-1">
				  	<div class="modal-dialog">
				   		<div class="modal-content">
				      		<div class="modal-header">
				        		<h5 class="modal-title">${qiestion}</h5>
				      		</div>
				      		<div id='add_answers' class="modal-body">
						        <p></p>
						      </div>
				      	</div>
				    </div>
				</div>

			`; 

			let a = Object.keys(POOL.answers);
			for (let i = 0; i < a.length; ++i) {
			  let key = a[i];
			  document.getElementById("add_answers").innerHTML += "<button class='answers'>" + POOL.answers[key] + "</button>";
			}
		} else console.log('Check your json!');
	}


}





/*

function showDetails(event){
	alert('Я вопрос викторины');

	for (let i = 0; i < POOL.length; ++i) {		
		let questionAllDetails = POOL[i];
		let qiestion = questionAllDetails.qiestion;
		let icon = questionAllDetails.icon;
		let category = questionAllDetails.category;
		const answersContainer = document.getElementById("answersContainer");

		answers = ['1941', '1524', '1614', '1921'];

  			document.getElementById('questions_details').innerHTML = 
			`
				<div class="modal" tabindex="-1">
				  	<div class="modal-dialog">
				   		<div class="modal-content">
				      		<div class="modal-header">
				        		<h5 class="modal-title">${qiestion}</h5>
				      		</div>
				      		<div class="modal-body">
						        <p>${answers}</p>
						      </div>
				      	</div>
				    </div>
				</div>

			`; 
		}

}*/