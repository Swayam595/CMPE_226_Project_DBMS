$(function() {
    $('document').ready(function() {
        $.ajax({
            url: '/currentOrders?inputId='+sessionStorage.getItem("id")+'&inputCaId='+sessionStorage.getItem("ca_id")+'&inputRole='+sessionStorage.getItem("role"),
            type: 'GET',
            success: function(response) {
                var orderList = JSON.parse(response).results;
                var totalCost =0;
                $.each( orderList, function( index, value ){
                    totalCost= totalCost + value[9]-value[10];
                });
                $(".totalVal").text(totalCost);
                var $ul = $('.currentOrders').append(
                  orderList.map(order =>
                    $("<tr>").append($("<td>").text(order[0]))
                        .append($("<td>").text(order[1])).append($("<td>").text(order[2]))
                        .append($("<td>").text(order[4])).append($("<td>").text(order[5]))
                        .append($("<td>").text(order[6])).append($("<td>").text(order[7]))
                        .append($("<td>").text(order[9])).append($("<td>").text(order[10]))
                        .append($("<td>").text(order[11])).append($("<td>").text(order[13]))
                        .append($("<td>").text(order[14])).append($("<td>").text(order[9]-order[10]))
                  )
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});