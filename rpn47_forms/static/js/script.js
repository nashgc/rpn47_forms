// INN AJAX request

$(document).ready(function () {
    $("#inn").autocomplete({
        minLength: 3,
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

// rasp_num generator

    var dash = '-'
    var slash = '/'
    var reg = '78'
    var district_code = '__'
    var department_code = '__'
    var doc_type = '26'
    var adm_num_calc = parseInt(gdn) + 1
    var adm_number = ("00000" + adm_num_calc).slice(-5)
    var year = (new Date()).getFullYear()


    $("#district").on('change', function () {
        district_code = this.value.substring(0,2)
        $("#raspr_num").val(reg+dash+district_code+dash+department_code+slash+doc_type+dash+adm_number+dash+year)
    })


    $("#department").on('change', function () {
        department_code = this.value.substring(0,2)
        $("#raspr_num").val(reg+dash+district_code+dash+department_code+slash+doc_type+dash+adm_number+dash+year)
    })


    $("#raspr_num").val(reg+dash+district_code+dash+department_code+slash+doc_type+dash+adm_number+dash+year)


    // get and set current date
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();

    if(dd<10) {
    dd = '0'+dd
    }

    if(mm<10) {
        mm = '0'+mm
    }

    $("#raspr_date").val(yyyy + '-' + mm + '-' + dd)

    $("#date_proved").val(yyyy + '-' + mm + '-' + dd)

    // datePicker loads here

    $("#raspr_date").datepicker({
    dateFormat: 'yyyy-mm-dd',
    todayButton: new Date()
    })

    $("#date_proved").datepicker({
        dateFormat: 'yyyy-mm-dd',
        todayButton: new Date()
    })

});

