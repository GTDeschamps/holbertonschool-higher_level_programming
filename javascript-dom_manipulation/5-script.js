const updateButton = document.querySelector('#update_header');
const headerElement = document.querySelector('header');
updateButton.addEventListener('click', function () {
  headerElement.textContent = 'New Header!!!';
});
