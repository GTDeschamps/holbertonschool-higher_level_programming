const moviesList = document.querySelector('#list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      moviesList.appendChild(listItem);
  });
})
  .catch(error => {
    console.error('Fetch error:', error);
  })

