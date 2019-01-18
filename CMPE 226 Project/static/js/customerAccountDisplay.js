$(function() {
    $('.placeOrder').click(function() {
        console.log($('.placeOrderForm').serialize());
        $.ajax({
            url: '/placeOrder?customer_id='+sessionStorage.getItem("id")+'&inputCaId='+sessionStorage.getItem("ca_id"),
            data: $('.placeOrderForm').serialize(),
            type: 'POST',
            success: function(response) {
                location.reload();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('document').ready(function() {
        $.ajax({
            url: '/currentOrders?inputId='+sessionStorage.getItem("id")+'&inputCaId='+sessionStorage.getItem("ca_id")+'&inputRole='+sessionStorage.getItem("role"),
            type: 'GET',
            success: function(response) {
                var orderList = JSON.parse(response).results;
                var $ul = $('.currentOrders').append(
                  orderList.map(order =>
                    $("<tr>").append($("<td class='orderId'>").text(order[0]))
                        .append($("<td>").text(order[1])).append($("<td>").text(order[2]))
                        .append($("<td>").text(order[5])).append($("<td>").text(order[6]))
                        .append($("<td>").text(order[7])).append($("<td>").append($('<button type="button" class="btn-sm btn-danger endOrder">Stop</button>')))
                  )
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('body').on('click', '.endOrder', function(e) {
        var x = $(this).parent().siblings(".orderId").text();
        $.ajax({
            url: '/endOrder?orderId='+x,
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