$(document).ready(function () {
    $("#inn").autocomplete({
        source: function (request, response) {
            var form = $(this);
            $.ajax({
                url: "{% url 'get_inn' %}",
                processData: true,
                type: 'POST',
                data: {
                    search: request.term,
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                },
                success: function (data) {
                    console.log(data)
                    response(data);
                },

            });
        },
        select: function (event, ui) {
            console.log(ui.item)
            $('.org').val(ui.item.name)
        }
    });
});
