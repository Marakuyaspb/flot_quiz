class Spinner {
    handleClear() {
        ROOT_SPINNER.innerHTML = '';
    }

    render() {
        const html = `
        	<div class="spinner-container">
        		<img class="spinner__img" src="http://temp.decona.ru/wp-content/uploads/2023/03/spinner.svg" />
        	</div>`;
        ROOT_SPINNER.innerHTML = html;
    }
}

const spinnerPage = new Spinner();