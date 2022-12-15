function ExecutePC(CommandName) {
	return $.ajax({
        url: '/execute',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({command:CommandName}),
    });
};
