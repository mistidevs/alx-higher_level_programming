$(document).ready(function(){
    $('#btn_translate').click(function(){
        var languageCode = $('#language_code').val();
        fetch(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`)
        .then(response => response.json())
        .then(data => {
            const hello = data.hello;
            $('DIV#hello').text(hello);
        }).catch(error => console.error(error));
    });
});
