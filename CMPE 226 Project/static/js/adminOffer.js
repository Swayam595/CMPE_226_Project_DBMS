$(function() {
    $('document').ready(function() {
        $.ajax({
            url: '/getOffer?inputId='+sessionStorage.getItem("id")+'&inputCaId='+sessionStorage.getItem("ca_id")+'&inputRole='+sessionStorage.getItem("role"),
            type: 'GET',
            success: function(response) {
                var orderList = JSON.parse(response).results;
                var $ul = $('.currentOrders').append(
                  orderList.map(order=>
                      $("<tr>").append($("<td class='offerId'>").text(order[0]))
                          .append($("<td>").text(order[1])).append($("<td>").text(order[2]))
                          .append($("<td>").append($('<button type="button" class="btn-sm btn-danger deleteOffer">Delete</button>')))
                      //$('.deleteOffer:last-child').data('offerId', order[0]);
                  )
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('.newOffer').click(function() {
        $.ajax({
            url: '/createOffer?inputId='+sessionStorage.getItem("id")+'&inputCaId='+sessionStorage.getItem("ca_id"),
            data: $('.newOfferForm').serialize(),
            type: 'POST',
            success: function(response) {
                location.reload();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('body').on('click', '.deleteOffer', function(e) {
        console.log(e);
        var x = $(this).parent().siblings(".offerId").text();
        $.ajax({
            url: '/deleteOffer?offerId='+ x,
            type: 'DELETE',
            success: function(response) {
                location.reload();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});