$(function() {
    $('document').ready(function() {
        $.ajax({
            url: '/getMachines?inputId='+sessionStorage.getItem("id")+'&inputCaId='+sessionStorage.getItem("ca_id")+'&inputRole='+sessionStorage.getItem("role"),
            type: 'GET',
            success: function(response) {
                var machineList = JSON.parse(response).results;
                var $ul = $('.currentOrders').append(
                  machineList.map(machine =>
                    $("<tr>").append($("<td class='macId'>").text(machine[0]))
                        .append($("<td>").text(machine[1])).append($("<td>").text(machine[2]))
                        .append($("<td>").text(machine[3])).append($("<td>").text(machine[4]))
                        .append($("<td>").text(machine[5])).append($("<td>").text(machine[6]))
                        .append($("<td>").append(machine[7]?machine[7]:$('<button type="button" class="btn-sm btn-info deleteMachine">Delete</button>')))
                  )
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('.orderMachine').click(function() {
        $.ajax({
            url: '/addMachine?inputId='+sessionStorage.getItem("id"),
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
    $('body').on('click', '.deleteMachine', function(e) {
        $.ajax({
            url: '/deleteMachine?inputId='+$(this).parent().siblings(".macId").text(),
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
});