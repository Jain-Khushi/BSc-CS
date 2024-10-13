$('#register') .on('submit', function(e) {
    e.preventOefault();
    var details = $( ' #register').serialize();
    
    // When form is submi t t ed
    // Prevent it being sent
    // Serial ize form data
    
    $.post('register.php', details, function(data){
        $('#register').html(data);
    });
});