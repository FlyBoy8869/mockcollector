$(document).ready(function() {
    $('#modemstatus').click(function() {
        window.open('/modemstatus');
    });

    $('#configuration').click(function() {
        window.open('/configuration');
    });

    $('#sensordata').click(function() {
        window.open('/sensordata');
    });

    $('#temperaturescale').click(function() {
        window.open('/temperaturescale');
    });

    $('#rawconfiguration').click(function() {
        window.open('/rawconfig');
    });

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
            $('#hide_when_on').hide()
	}

	$('#collector_on').click(function() {
		$('.response').prop("disabled", "true");
        $('#hide_when_on').hide()
	});

	$('#collector_off').click(function() {
		$('.response').prop("disabled", "");
        $('#hide_when_on').show()
	});
});
