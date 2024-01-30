document.addEventListener('DOMContentLoaded', function () {
const helloElement = document.querySelector('#hello');
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    return response.json();
  })
  .then(data => {
    helloElement.textContent = data.hello;
	console.log(data.hello)
  })
});
