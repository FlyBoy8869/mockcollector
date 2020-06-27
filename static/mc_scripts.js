$(document).ready(function() {
	$('.debug_container').addClass("hidden");

	$('.debug_container').click(function() {
		if ($(this).hasClass("hidden")) {
			$(this).removeClass("hidden").addClass("visible");
			$('.debug_hand').text('\u25B2');
		} else {
			$(this).removeClass("visible").addClass("hidden");
			$('.debug_hand').text('\u25BC');
		}
	});

	if ($('#collector_on').prop('checked')) {
			$('.response').prop('disabled', 'true');
	}

	$('#collector_on').click(function() {
		$('.response').prop("disabled", "true");
	});

	$('#collector_off').click(function() {
		$('.response').prop("disabled", "");
	});

    console.log("Contents of Sensor 1: " + $('#serial_1').prop("value"));
});
