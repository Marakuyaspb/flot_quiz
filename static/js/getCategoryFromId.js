function getCategoryFromId(event) {
	const clickedElement = event.currentTarget;
  	const currentCategory = clickedElement.id;
  	console.log(currentCategory);
	return currentCategory;
	}