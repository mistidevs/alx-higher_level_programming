$(document).ready(function() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(repsonse => response.json())
      .then(data => {
          const hello = data.hello;
          $('DIV#hello').text(hello);
      })
	.catch(error => console.error(error));
});
