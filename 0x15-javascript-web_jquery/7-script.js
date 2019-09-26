$.getJSON('https://swapi.co/api/people/5/', function (data) {
  $('#character').append(data.name);
});
