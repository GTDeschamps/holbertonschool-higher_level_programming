const buttonElement = document.querySelector('#red_header');
const headerElement = document.querySelector('header');

buttonElement.addEventListener('click', function(){
  headerElement.style.color = '#FF0000';
});

