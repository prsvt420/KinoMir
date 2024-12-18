$(document).ready(function () {
    $("#search").on("input", function () {
        let search_query = $(this).val();

        $.ajax({
            url: "/serials/",
            method: "GET",
            data: {
                "q": search_query
            },
            success: function (serials) {
                $(".serials-list").empty();
                for (let serial of serials) {
                    let serial_html = `
                        <article class="serial" onclick="location.href='/serials/${serial.slug}/'">
                            <img src="/media/${serial.poster}" alt="${serial.title}">
                            <p>${serial.title}</p>
                        </article>
                    `;
                    $(".serials-list").append(serial_html);
                }

            }
        });
    });
});