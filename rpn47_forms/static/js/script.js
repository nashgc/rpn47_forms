$(document).ready(function () {
    $("#inn").autocomplete({
        source: function (request, response) {
            var form = $(this);
            $.ajax({
                url: url,
                processData: true,
                type: 'POST',
                data: {
                    search: request.term,
                    csrfmiddlewaretoken: csrf_token,
                },
                success: function (data) {
                    // console.log(data)
                    response(data);
                },

            });
        },
        select: function (event, ui) {
            // console.log(ui.item)
            $('.org').val(ui.item.org)
        }
    });

    var dash = '-'
    var slash = '/'
    var reg = '78'
    var district_code = '__'
    var department_code = '__'
    var doc_type = '26'
    var adm_number = '____'
    var year = (new Date()).getFullYear()


    $("#district").on('change', function () {
        district_code = this.value.substring(0,2)
        $("#raspr_num").val(reg+dash+district_code+dash+department_code+slash+doc_type+dash+adm_number+year)
    })


    $("#department").on('change', function () {
        department_code = this.value.substring(0,2)
        $("#raspr_num").val(reg+dash+district_code+dash+department_code+slash+doc_type+dash+adm_number+year)
    })


    $("#raspr_num").val(reg+dash+district_code+dash+department_code+slash+doc_type+dash+adm_number+year)
});