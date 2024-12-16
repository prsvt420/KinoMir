$(document).ready(function () {
    $("#search").on("input", function () {
        let search_query = $(this).val();

        $.ajax({
            url: "/movies/",
            method: "GET",
            data: {
                "q": search_query
            },
            success: function (movies) {
                $(".movies-list").empty();
                for (let movie of movies) {
                    let movie_html = `
                        <article class="movie" onclick="location.href='/movies/${movie.slug}/'">
                            <img src="/media/${movie.poster}" alt="${movie.title}">
                            <p>${movie.title}</p>
                        </article>
                    `;
                    $(".movies-list").append(movie_html);
                }

            }
        });
    });
});