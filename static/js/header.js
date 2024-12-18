$(document).ready(function () {
    let activeLink = window.location.pathname
    
    if (activeLink == '/movies/') {
        $('nav a').eq(0).addClass('active')
    } else if (activeLink == '/serials/') {
        $('nav a').eq(1).addClass('active')
    }
});