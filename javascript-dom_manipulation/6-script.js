const characterSpan = document.querySelector('#character');
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
	}
      return response.json();
  })
  .then(data => {
    characterSpan.textContent = data.name;
  })
  .catch(error => {
    console.error('Fetch error:', error);
});
