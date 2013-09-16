$(function() {
	var text = $('#text'),
		size = $('#size'),
		format = $('#format')
		identicon = $('#identicon-img');
	var apiBase = 'api/identicon/';

	var changeHandler = function(e) {
		var textVal = text.val();
		var identiconWidth = size.val();
		var url = apiBase + textVal + '?size=' + identiconWidth + '&format=' + format.val();

		if (!$.trim(textVal) == '') {
			identicon.css('left', -identiconWidth/2);
		} else {
			identicon.css('left', -75);
		}

		identicon.prop('src', url);
	};

	text.on('keyup', changeHandler);
	size.on('change', changeHandler);
	format.on('change', changeHandler);
});