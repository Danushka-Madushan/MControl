document.getElementById("caps").onclick = function() {
    $.ajax({
        url: '/execute',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({command:"ss"}),
        success: function(data) {
            $(document).ready(function() {
                $(".list").append($(`<span>`).html(`<a href="/media/${data['info'].media_id}/123456789" target="_blank"> Screenshot - ${data['info'].stamp}</a>`));
            });
        },
        error: function(xhr, textStatus, errorThrown) {
            //called when there is an error
        }
    });
}

document.getElementById("clr").onclick = function(){
    $.ajax({
        url: '/execute',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({command:"ss-clear"}),
        success: function(data) {
            console.log(data)
            $(".list").empty()
        },
        error: function(xhr, textStatus, errorThrown) {
            //called when there is an error
        }
    });
};
