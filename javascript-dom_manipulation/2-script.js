const buttonElement = document.querySelector('#red_header');
const headerElement = document.querySelector('header');

buttonElement.addEventListener('click', function(){
  headerElement.classList.add('red');
});
