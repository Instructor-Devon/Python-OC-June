$(document).ready(function() {
    fetchPosts();
})
$('form').submit(function(event) {
    var formData = ($(this).serialize());
    this.reset();
    $.ajax({
        url: "/create",
        method: "POST",
        data: formData
    })
    .then(function(response) {
        $("#stuff").html(response);
    })
    event.preventDefault();
    // return false;
})

function fetchPosts() {
    $.ajax({
        url: "/fetch"
    })
    .then(function(response) {
        $("#stuff").html(response);
    })
    .catch(function(error) {
        console.log(error);
    })
}
