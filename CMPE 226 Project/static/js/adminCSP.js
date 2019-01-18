$(function() {
    $('document').ready(function() {
        $.ajax({
            url: '/myCSPs?inputCaId='+sessionStorage.getItem("ca_id")+'&inputRole='+sessionStorage.getItem("role"),
            type: 'GET',
            success: function(response) {
                var orderList = JSON.parse(response).resultsAvailable;
                var $ul = $('.currentOrders').append(
                  orderList.map(order =>
                      $("<tr>").append($("<td>").text(order[0]))
                          .append($("<td>").text(order[1])).append($("<td>").text(order[2]))
                          .append($("<td>").text(order[4])).append($("<td>").text(order[5]))
                          .append($("<td>").append($('<button type="button" class="btn-sm btn-danger">Delete</button>')))
                  )
                );
                orderList = JSON.parse(response).resultsOccupied;
                $ul = $('.currentOrders').append(
                  orderList.map(order =>
                      $("<tr>").append($("<td>").text(order[0]))
                          .append($("<td>").text(order[1])).append($("<td>").text(order[2]))
                          .append($("<td>").text(order[4])).append($("<td>").text(order[5]))
                          .append($("<td>").text("Order in Progress!"))
                  )
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});