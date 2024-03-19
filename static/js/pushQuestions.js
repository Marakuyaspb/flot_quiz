/* PRODUCTS */


class Products {

	render() {

		
		let htmlProducts = '';
		
		CATALOG.forEach(({sku, category, model, filter_it, fabric_type, fabric_name, product_name, product_img, product_img_mob, pdf, is_new,available_in_showroom, available_for_delivery_2,available_for_delivery_28, width, depth, height, price, price_sale}) => {
			
			htmlProducts += `
			
			<div class = "product_card p-3 sku ${category} ${filter_it}" id='${sku}' onClick='showDetails(event);'>


			<!-- HEAD OF THE CARD -->
				<!-- DESCTOP -->
				<div class = 'd-none d-md-block d-lg-block d-xl-block d-xxl-block'>
					<div class = 'd-flex justify-content-between'>
						<div>
							<h3 class='product_card_header'>${product_name}</h3>
						</div>
				
						<div>
							<img class = 'is_new_icon' src='${is_new}'>
							<img class = 'available_icon' src='${available_in_showroom}'> 
							<img class = 'available_icon'src='${available_for_delivery_2}'>
						</div>
					</div>
				</div>

					
				<!-- PHONE -->
				<div class='d-flex justify-content-between d-block d-md-none'>
					<h3 class='product_card_header product_card_name_mob '>${product_name}</h3>
					<div>
						<img class = 'is_new_icon_mobile' src='${is_new}'>
						<img class = 'available_icon_mobile' src='${available_in_showroom}'> 
						<img class = 'available_icon_mobile'src='${available_for_delivery_2}'>
					</div>
				</div>

			<!-- END OF THE HEAD OF THE CARD -->


				
				<center class='mt-4 d-none d-md-block d-lg-block d-xl-block d-xxl-block'>
					<img src="${product_img}" class="img-fluid product_img_under">
				</center>
				
				<div class = 'card-bottom-info'>
					<center class='mt-5 d-block d-md-none'>
						<img src="${product_img_mob}" class="img-fluid product_img_under">
					</center>

					<div class = 'd-flex justify-content-between'>
						<div class='cacao'>В наличии</div>
						<div class='old-price_cat_page'>${price} ₽</div>
					</div>

					<div class = 'd-flex justify-content-between'>
						<div class='cacao'>${width}×${depth}×${height}</div>
						<div class='cacao price_cat_page'>${price_sale} ₽</div>
					</div>
				</div>
			</div>
			`;
			});

			const html = `
			<!-- div class='thin ms-5'><a href='http://temp.decona.ru'>Главная</a> / <a href='http://temp.decona.ru'>Продукция</a>
			</div -->
			
			<div class="products_container">	
					${htmlProducts}
			</div>
		`;
		ROOT_PRODUCTS.innerHTML = html;
		
		}
	}
console.log('goods rendered');
const productsPage = new Products();