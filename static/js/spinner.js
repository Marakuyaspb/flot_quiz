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