$(document).ready(function(){
    function translate() {
        var languageCode = $('#language_code').val();
        fetch(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`)
        .then(response => response.json())
        .then(data => {
            const hello = data.hello;
            $('#hello').text(hello);
        }).catch(error => console.error(error));
    }

    $('#btn_translate').click(translate);
    $('#language_code').keypress(function(e){
        if(e.which == 13) { // Enter key pressed
            translate();
        }
    });
});
