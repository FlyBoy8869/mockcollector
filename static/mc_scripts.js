$(document).ready(function() {
	$('.debug_container').addClass("hidden");

	$('.debug_container').click(function() {
		var $this = $(this);

		if ($this.hasClass("hidden")) {
			$(this).removeClass("hidden").addClass("visible");
			$('.debug_hand').text('\u25B2');
		} else {
			$(this).removeClass("visible").addClass("hidden");
			$('.debug_hand').text('\u25BC');
		}
	});
});
