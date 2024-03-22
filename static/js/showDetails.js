/* Change it! */

function showDetails(event){
	
/* get SKU of product by the CLICK */
 	const clickedElement = event.currentTarget;
  	const currentSKU = clickedElement.id;
  	
/* compare the clicked SKU with all SKUs in [] */
   	for (let i = 0; i < POOL.length; ++i) {		
		if (POOL[i].sku == currentSKU){

/* create a new var with all info about the match sku */
		let questionAllDetails = POOL[i];


/* remove current html */
		var allQuestions = document.getElementById('questions_show');
		allProducts.remove();


/* define vars  */
		let qiestion = questionAllDetails.qiestion;
		let icon = questionAllDetails.icon;
		let category = questionAllDetails.category;
		const answersContainer = document.getElementById("answersContainer");

		for (const key in data.answers) {
	  const button = document.createElement("button");
	  button.id = answer_${key};
	  button.textContent = key;
	  answersContainer.appendChild(button);
}

/* render new html about the single product */
  			document.getElementById('goods_details').innerHTML = 
			`
	<div class=''>
		<h4 class='p-3'>${qiestion}</h4>
		<div id='answersContainer' class="d-flex flex-column bd-highlight mb-3 px-2">
		</div>
	</div>
			`; 
		} else console.log('Check your json!');
	}


}