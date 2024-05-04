// fonction pour afficher le loader
function showloader(loaderId) {
	console.log('La fonction showloader est appelée avec l\'identifiant :', loaderId);

	// Vérification que l'élément du loader existe dans le document HTML
	var loader = document.getElementById(loaderId);
	if (loader) {
		loader.style.display = 'block';
		// Masquez le tutoriel
		const tutorial = document.getElementById('tuto');
		tutorial.style.display = 'none';
		// Masquez l'erreur
		const erreur = document.getElementById('erreur-input');
		erreur.style.display = 'none';
	} else {
		console.error("L'élément du loader n'existe pas dans le document HTML.");
	}
}

$(document).ready(function(){

	var windowHeight = $(window).height();
	var documentHeight = $(document).height();	
	
	if (documentHeight <= windowHeight) {
		$('footer').css('position', 'fixed');
		$('footer').css('bottom', '0');
		$('footer').css('width', '100%');
	} else {
		$('footer').css('position', 'relative');
		$('footer').css('bottom', 'auto');
		$('footer').css('width', 'auto');
	}
	
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


    // Sélectionne tous les liens d'exemple du tuto
    const exampleLinks = document.querySelectorAll('.example-link');

    // Parcoure tous les liens d'exemple et ajoute un gestionnaire d'événements de clic
    exampleLinks.forEach((link) => {
        link.addEventListener('click', (event) => {
            // Empêche le comportement par défaut du lien
            event.preventDefault();

            // Récupére la valeur du texte du lien
            const searchTerm = event.target.textContent;

            // Sélectionne l'entrée de recherche et définis sa valeur
            const searchInput = document.getElementById('tokens');
            searchInput.value = searchTerm;

            // Soumet le formulaire
            const searchForm = document.querySelector('form');
            searchForm.submit();
        });
    });

});
