$(function() {
    $('document').ready(function() {
        $(".ticketSuccess").hide();
        $.ajax({
            url: '/getTickets?inputId='+sessionStorage.getItem("id")+'&inputRole='+sessionStorage.getItem("role"),
            type: 'GET',
            success: function(response) {
                var $ul = $('.orderHistory').append(
                  response.result.map(order =>
                    $("<tr>").append($("<td>").text(order._id))
                        .append($("<td>").text(order.problem_title)).append($("<td>").text(order.problem_description))
                        .append($("<td>").text(order.date)).append($("<td>").text(order.resolved))
                  )
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
     $('.help').click(function() {
        $.ajax({
            url: '/help?inputRole='+sessionStorage.getItem("role")+'&inputId='+sessionStorage.getItem("id"),
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                $(".ticketSuccess").show();
                location.reload();
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});