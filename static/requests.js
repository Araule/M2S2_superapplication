// Définir la fonction showloader() en dehors de la fonction $(document).ready()
function showloader(loaderId) {
	console.log('La fonction showloader est appelée avec l\'identifiant :', loaderId);

	// Vérifier que l'élément du loader existe dans le document HTML
	var loader = document.getElementById(loaderId);
	if (loader) {
		loader.style.display = 'block';

	} else {
		console.error("L'élément du loader n'existe pas dans le document HTML.");
	}
}

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
});
