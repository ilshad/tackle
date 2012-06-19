/**
*
* 2010 Ilshad Khabibullin, <astoon@spacta.com>
*
**/

// Loading...
$(function () {
    $("#spinner").ajaxStart(
	function () {$(this).show();}
    ).ajaxStop(
	function () {$(this).hide();});

    $(".loadme").each(function(i) {
	$(this).load($(this).text());
    });
});
