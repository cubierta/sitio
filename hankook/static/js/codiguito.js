$(document).on('ready', init);

function init()
{
	var now = window.location;
	if(now.pathname == '/productos/' ){

		$('body').hide();
		$('body').fadeIn('slow');

	}
	$("#productos").on("click", transicion);
}

function transicion()
 {
		//calcular with antes de animacion para que puedas dejar el contenedor sin moverse al remover el .bio y .slider
			var alto = $('.part1').height();

			$('.bio').animate({

				right: '-1500px',
				

				}, 1000, function () {	
				// $('.bio').css('display','none');

				$('.slider').animate({

							left: '-1500px',

									}, 1000, function () {
										magic();

									});

				var  despues = $('.part1').height();
				$.data(document,"altos",despues)
						// if (alto != despues) {

						// 	$('.part1').css('height', alto+'px');
						// 	//poner altura original o auto cuando se cargen los nuevos datos de los neumaticos
						// 			 		}

											
			});
			


}
function magic(){
$('.bio').remove();
$('.slider').remove();
var now = window.location;
var anda  = $('#productos').attr('id');
if  (now.pathname == '/' ){
	var newdirection = now.origin + now.pathname + anda;
	window.location = newdirection;
	// console.log(newdirection);
}
}