$("#caps").click(function() {
    ExecutePC("ss").then(data => {
        if (!$('.hidable-1').is(':visible')) {
            //$(".hidable-1").show();
            $(".hidable-1").fadeIn(400);
        };
        $(document).ready(function() {
            $(".list").append($(`<span>`).html(`<a href="/media/${data['info'].media_id}/123456789" target="_blank"> Screenshot - ${data['info'].stamp}</a>`));
        });
    });
});

$("#clr").click(function() {
    ExecutePC("ss-clear").then(data => {
        $(".list").empty()
        if ($(".hidable-1").is(':visible')) {
            //$(".hidable-1").hide();
            $(".hidable-1").fadeOut(400);
        };
    });
});

$("#sdp").click(function() {
    ExecutePC("os-shut").then(data => {
        if (data['status'] == 'success') {
            if (!$('.hidable-2').is(':visible')) {
                $('.hidable-2').fadeIn(400);
            };
            //alert(JSON.stringify(data, null, 4))
        };
    });
});

$("#asdp").click(function() {
    ExecutePC("abort-shut").then(data => {
        if (data['status'] == 'success') {
            if ($('.hidable-2').is(':visible')) {
                $('.hidable-2').fadeOut(400);
            };
            //alert(JSON.stringify(data, null, 4))
        };
    });
});
