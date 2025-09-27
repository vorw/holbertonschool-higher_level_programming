const addItem = document.querySelector('#add_item');
const list = document.querySelector('ul.my_list');

addItem.addEventListener('click', () => {
  const li = document.createElement('li');
  li.textContent = 'Item';
  list.appendChild(li);
});
