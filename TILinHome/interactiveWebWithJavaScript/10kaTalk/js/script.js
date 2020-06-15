$('#send').on('click', sendText);

function sendText() {
    var newMessage = $('#new-message').val();

    if (newMessage != '') {
        $('.chatbox').append('<div class="my-bubble bubble">' + newMessage + '</div>')
        $('#new-message').val('');
    }
}