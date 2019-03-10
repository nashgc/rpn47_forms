// CSRF token
$(document).ready(function () {

    $('#dtBasicExample').DataTable({
        language: {
            search: "Сквозной фильтр: "
        },
        "paging": false,
        "bInfo" : false,
        stateSave: true,
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');


// INN autocomplete + set organization when select
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
                    csrfmiddlewaretoken: csrftoken,
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


// KoAP autocomplete + set kbk when select
    $("#koap_article").autocomplete({
    minLength: 1,
    source: function (request, response) {
        var form = $(this);
        $.ajax({
            url: url_koap,
            processData: true,
            type: 'POST',
            data: {
                search: request.term,
                csrfmiddlewaretoken: csrftoken,
            },
            success: function (data) {
                // console.log(data)
                response(data);
            },
        });
    },
    select: function (event, ui) {
        // console.log(ui.item)
        $('#kbk').val(ui.item.kbk)
    }
});


// rasp_num generator

    var dash = '-'
    var slash = '/'
    var reg = '78'
    var district_code = '__'
    var department_code = '__'
    var doc_type = '19'
    var adm_num_calc = parseInt(gdn)
    var adm_number = ("0000" + adm_num_calc).slice(-4)
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


    // get date and add 70 days
    var newdate = new Date();
    newdate.setDate(newdate.getDate()+70)
    var ddd = newdate.getDate();
    var mmm = newdate.getMonth()+1; //January is 0!
    var yyyyy = newdate.getFullYear();

    if (ddd < 10) {
        ddd = '0' + ddd
    }

    if (mmm < 10) {
        mmm = '0' + mmm
    }


    // dates field load here
    // bylaw
    $("#raspr_date, #date_proved, #date_proved_po, #date_proved_c").val(dd + '.' + mm + '.' + yyyy)

    // bylaw datapicker
    $("#raspr_date, #date_proved_po, #date_proved_c, #date_proved").datepicker({
    todayButton: new Date()
    })


    //ordinance
    $("#ordinance_date, #fact_pay_date, #income_receipt_date, #protocol_date").val(dd + '.' + mm + '.' + yyyy)
    $("#pay_date").val(ddd + '.' + mmm + '.' + yyyyy)

    //ordinance datapicker
    $("#ordinance_date, #pay_date, #fact_pay_date, #income_receipt_date, #protocol_date").datepicker({
        todayButton: new Date()
    })

    $("#fine_sum").bind('input', function(){
        $("#debt").val(this.value)
    })




});

