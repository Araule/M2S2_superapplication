$(document).ready(function(){

	/* pour permettre de revenir en haut de la page avec un boutton */
	/* en tout honnêteté, le code a été trouvé sur internet */
	// get the button
	let mybutton = document.getElementById("btn-back-to-top");

	// when the user scrolls down 20px from the top of the document, show the button
	function scrollFunction() {
		if (
			document.body.scrollTop > 20 ||
			document.documentElement.scrollTop > 20
		) {
			mybutton.style.display = "block";
		} else {
			mybutton.style.display = "none";
		}
		}

	window.onscroll = function () { scrollFunction(); };


	// when the user clicks on the button, scroll to the top of the document
	mybutton.addEventListener("click", backToTop);

	function backToTop() {
		document.body.scrollTop = 0;
		document.documentElement.scrollTop = 0;
	}
	
	// function showloader() {
	// 	var loader = document.getElementById('loader');

	// 	if (loader) {
	// 		$("#loader").css("display", "block");
	// 	} else {
	// 		console.error("Loader element not found.");
	// 	}
	// }

	// function receiveFA(vars) {
	// 	return vars; // Ajout du point-virgule
	// }

	// /* Lecture dans une variable res */
	// var res = receiveFA({results});
	// /* Cacher le loader si des infos ont bien été renvoyées par Python */
	// if (Object.keys(res).length > 0){
	// 	$("#loader").css("display", "none");
	// }

});
