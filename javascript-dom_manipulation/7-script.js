const list = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    data.results.forEach((film) => {
      const li = document.createElement('li');
      li.textContent = film.title;
      list.appendChild(li);
    });
  })
  .catch(() => {
    const li = document.createElement('li');
    li.textContent = 'Error loading movies.';
    list.appendChild(li);
  });
