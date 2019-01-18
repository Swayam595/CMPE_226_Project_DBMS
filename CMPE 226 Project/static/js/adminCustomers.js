$(function() {
    $('document').ready(function() {
        $.ajax({
            url: '/myCustomers?inputCaId='+sessionStorage.getItem("ca_id")+'&inputRole='+sessionStorage.getItem("role"),
            type: 'GET',
            success: function(response) {
                var orderList = JSON.parse(response).results;
                var $ul = $('.currentOrders').append(
                  orderList.map(order =>
                      $("<tr>").append($("<td class='customerId'>").text(order[0]))
                          .append($("<td class='customerEmail'>").text(order[1])).append($("<td class='customerName'>").text(order[2]))
                          .append($("<td>").text(order[4])).append($("<td class='customerBankAccount'>").text(order[5]))
                          .append($("<td>").append($('<button type="button" class="btn-sm btn-danger deletCust">Delete</button>')))
                          .append($("<td class='customerOfferId'>").append(order[6])).append($("<td>").append($('<button type="button" class="btn-sm btn-info assignOffer" data-toggle="modal" data-target="#myModal">Update</button>')))
                  )
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('body').on('click', '.assignOffer', function(e) {
        $("#inputId").val($(this).parent().siblings(".customerId").text());
        $("#inputName").val($(this).parent().siblings(".customerName").text());
        $("#inputEmail").val($(this).parent().siblings(".customerEmail").text());
        $("#inputBankAccount").val($(this).parent().siblings(".customerBankAccount").text());
        $("#inputOfferId").val($(this).parent().siblings(".customerOfferId").text());
    });

    $('body').on('click', '.deletCust', function(e) {
        var x = $(this).parent().siblings(".customerId").text();
        $.ajax({
            url: '/deleteCustomer?inputRole=customer&inputId='+x,
            type: 'DELETE',
            success: function(response) {
                console.log(response);
                location.reload();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('.updateProfile').click(function() {
        console.log($('form').serialize());
        $.ajax({
            url: '/updateCustomerProfile?inputRole=customer&inputId='+$('form').serialize().split("&")[0].split("=")[1],
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                location.reload();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});