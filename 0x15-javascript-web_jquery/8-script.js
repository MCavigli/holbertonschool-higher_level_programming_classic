$.getJSON("https://swapi.co/api/films/", function(data) {
    $(data.results).each(function(i, v) {
        $("#list_movies").append("<li>" + v.title + "</li>");
    });
});
