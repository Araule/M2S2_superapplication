$(document).ready(function(){
	
	function showloader() {
		var loader = document.getElementById('loader');

		if (loader) {
			$("#loader").css("display", "block");
		} else {
			console.error("Loader element not found.");
		}
	}

	function receiveFA(vars) {
		return vars; // Ajout du point-virgule
	}
	/* Lecture dans une variable res */
	var res = receiveFA({{res|tojson}});
	/* Cacher le loader si des infos ont bien été renvoyées par Python */
	if (Object.keys(res).length > 0){
		$("#loader").css("display", "none");
	}

});
