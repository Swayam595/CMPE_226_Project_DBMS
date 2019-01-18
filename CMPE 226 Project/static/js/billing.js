$(function() {
    $('document').ready(function() {
        $.ajax({
            url: '/bill/current?inputId='+sessionStorage.getItem("id")+'&inputCaId='+sessionStorage.getItem("ca_id")+'&inputRole='+sessionStorage.getItem("role"),
            data: $('form').serialize(),
            type: 'GET',
            success: function(response) {
                console.log(response);
                var bills = JSON.parse(response).results;
                var $ul = $('.bills').append(
                  bills.map(bill =>
                    $("<tr>").append($("<td class='inputBillid'>").text(bill[0])).append($("<td>").text(bill[2])).append($("<td>").text(bill[3]))
                        .append($("<td>").text(bill[4])).append($("<td>").text(bill[5])).append($("<td>").append($('<button type="button" class="btn-sm btn-info payBill">Pay</button>')))
                  )
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
        $.ajax({
            url: '/bill/history?inputId='+sessionStorage.getItem("id")+'&inputCaId='+sessionStorage.getItem("ca_id")+'&inputRole='+sessionStorage.getItem("role"),
            data: $('form').serialize(),
            type: 'GET',
            success: function(response) {
                console.log(response);
                var bills = JSON.parse(response).results;
                var $ul = $('.bills').append(
                  bills.map(bill =>
                    $("<tr>").append($("<td>").text(bill[0])).append($("<td>").text(bill[2])).append($("<td>").text(bill[3]))
                        .append($("<td>").text(bill[4])).append($("<td>").text(bill[5])).append($("<td>").text(bill[6]==0?"NO":"YES"))
                  )
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('body').on('click', '.payBill', function(e) {
        var x = $(this).parent().siblings(".inputBillid").text();
        $.ajax({
            url: '/bill/pay?inputId='+sessionStorage.getItem("id")+'&inputRole='+sessionStorage.getItem("role")+'&inputBillId='+x,
            type: 'GET',
            success: function(response) {
                location.reload();
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});