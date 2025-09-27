const header = document.querySelector('header');
const redButton = document.querySelector('#red_header');

redButton.addEventListener('click', () => {
  header.style.color = '#FF0000';
});
