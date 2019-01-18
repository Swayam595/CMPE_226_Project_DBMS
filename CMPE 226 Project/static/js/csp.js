$(function() {
    $('document').ready(function() {
        $.ajax({
            url: '/currentOrders?inputId='+sessionStorage.getItem("id")+'&inputCaId='+sessionStorage.getItem("ca_id")+'&inputRole='+sessionStorage.getItem("role"),
            type: 'GET',
            success: function(response) {
                var orderList = JSON.parse(response).results;
                var totalCost =0;
                $.each( orderList, function( index, value ){
                    totalCost= totalCost + value[9];
                });
                $(".totalVal").text(totalCost);
                var $ul = $('.currentOrders').append(
                  orderList.map(order =>
                    $("<tr>").append($("<td class='orderId'>").text(order[0]))
                        .append($("<td>").text(order[1])).append($("<td>").text(order[2]))
                        .append($("<td>").text(order[5])).append($("<td>").text(order[6]))
                        .append($("<td>").text(order[7])).append($("<td>").text(order[9]))
                  )
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});