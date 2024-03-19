function pushSKUinForm(event){
	let element = document.getElementsByClassName("sku");
	class_sku = element[0];
	let product_sku = class_sku.getAttribute('id');
	/*console.log(product_sku);*/
	document.querySelector('input#ordered_sku').setAttribute('value', product_sku);
};