document.getElementById("caps").onclick = function() {
    ExecutePC("ss").then(data => {
        $(document).ready(function() {
            $(".list").append($(`<span>`).html(`<a href="/media/${data['info'].media_id}/123456789" target="_blank"> Screenshot - ${data['info'].stamp}</a>`));
        });
    });
};

document.getElementById("clr").onclick = function(){
    ExecutePC("ss-clear").then(data => {
        console.log(data)
        $(".list").empty()
    });
};

document.getElementById("sdp").onclick = function(){
    ExecutePC("os-shut").then(data => {
        alert(JSON.stringify(data, null, 4))
    });
};

document.getElementById("asdp").onclick = function(){
    ExecutePC("abort-shut").then(data => {
        alert(JSON.stringify(data, null, 4))
    });
};
