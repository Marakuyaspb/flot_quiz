function makeCurentFabricBig(){
	let allSku = document.getElementsByClassName('sku');
	let currFabric = document.getElementsByClassName('.fabric-var');
	console.log(currFabric);

	for (let ii = 0; ii < allSku.length; ++ii){
		if(allSku[ii] == allSku.id){
			var currSku = allSku[ii];
			console.log(currSku);
			for (let iii = 0; iii < currFabric.length; ++iii){
				console.log(currFabric.id);
			    if(currFabric.id == currSku){
			    currFabric.classList.add("slide-fabric-button-active");
			  }
			}
		}
	}
	
}