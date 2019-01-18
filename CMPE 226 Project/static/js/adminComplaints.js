$(function() {
    $('document').ready(function() {
        $(".ticketSuccess").hide();
        $(".ticketResolveSuccess").hide();
        $.ajax({
            url: '/getTickets?inputId='+sessionStorage.getItem("id")+'&inputRole='+sessionStorage.getItem("role"),
            type: 'GET',
            success: function(response) {
                var $ul = $('.orderHistory').append(
                  response.result.map(order =>
                    $("<tr>").append($("<td class='issueId'>").text(order._id))
                        .append($("<td>").text(order.problem_title)).append($("<td>").text(order.problem_description))
                        .append($("<td>").text(order.date)).append($("<td>").append(order.resolved=="no"?$('<button type="button" class="btn-sm btn-info resolveIssue" data-toggle="modal" data-target="#myModal">Resolve</button>'):order.resolved))
                  )
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
     $('body').on('click', '.resolveIssue', function(e) {
        $.ajax({
            url: '/resolveIssue?inputIssueId='+$(this).parent().siblings(".issueId").text(),
            data: $('form').serialize(),
            type: 'GET',
            success: function(response) {
                $(".ticketResolveSuccess").show();
                location.reload();
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});