function ExecutePC(CommandName) {
	return $.ajax({
        url: '/execute',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({command:CommandName}),
    });
};

function DeviceID(uaString) {
    return $.ajax({
        url:'/device',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({userAgent:uaString})
    });
};
