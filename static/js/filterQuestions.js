function filterProducts(event){
	let clickedEl = event.currentTarget;
  	let currentCat = clickedEl.id;
  	console.log(currentCat);

    /* filter it */
  	const filteredDivs = document.querySelectorAll(`div.${currentCat}`);
  	const filteredContent = document.getElementById('goods_show');

  	filteredDivs.forEach(div => {
      filteredContent.appendChild(div);
    });




    /* Scroll to top */
        document.body.scrollTop = document.documentElement.scrollTop = 0;
        /*console.log('scroll it!');*/


    /* remove categories cards */
        var goods_categories_desctop = document.getElementById('goods_categories_desctop');
        goods_categories_desctop.remove();
        var goods_categories_phone = document.getElementById('goods_categories_phone');
        goods_categories_phone.remove();

    /* remove slider */
        var mainHeadSlider = document.getElementById('desctop-show');
        mainHeadSlider.remove();
        var mainHeadSlider = document.getElementById('phone-show');
        mainHeadSlider.remove();

    /* change text & icons color in the menu */
        let logo = document.getElementsByClassName('navbar-brand');
        for (var i_1 = 0; i_1 < logo.length; i_1++) {
            logo[i_1].classList.remove('white');
        };
        
        let nl = document.getElementsByClassName('nav-link');
        for (var i_2 = 0; i_2 < nl.length; i_2++) {
            nl[i_2].classList.remove('white');
        };

        let ih = document.getElementsByClassName('icon-header');
        for (var i_3 = 0; i_3 < ih.length; i_3++) {
            ih[i_3].classList.remove('white');
        };

        let ts = document.getElementsByClassName('top-string');
        for (var i_4 = 0; i_4 < ts.length; i_4++) {
            ts[i_4].classList.remove('white');
        };

}
