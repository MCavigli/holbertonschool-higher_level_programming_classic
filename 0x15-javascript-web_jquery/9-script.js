$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  $('#hello').append(data.hello);
});
