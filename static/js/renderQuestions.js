function render() {
	questionsPage.render();	
}

spinnerPage.render();

let POOL = [];
render();


/* redirect */
fetch('qu.json')
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