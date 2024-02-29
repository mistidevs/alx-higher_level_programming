$(document).ready(function() {
    fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
      .then(response => response.json())
      .then(data => {
          data.results.forEach(movie => {
              let listItem = $('<li></li>').text(movie.title);
              $('#list_movies').append(listItem);
          });
      })
	.catch(error => console.error(error));
});
