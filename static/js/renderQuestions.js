function render() {
	productsPage.render();	
}

spinnerPage.render();

let CATALOG = [];
render();

/* redirect */
fetch('./qu.json')
    .then(res => res.json())
    .then(body => {
		CATALOG = body;

		setTimeout(() => {
			spinnerPage.handleClear();
			render();
		}, 1000);
    })
    .catch(() => {
        spinnerPage.handleClear();
    	errorPage.render();
    })