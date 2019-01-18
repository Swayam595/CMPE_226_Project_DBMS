$(function() {
    $('document').ready(function() {
        $.ajax({
            url: '/getMachines?inputId='+sessionStorage.getItem("id")+'&inputCaId='+sessionStorage.getItem("ca_id")+'&inputRole='+sessionStorage.getItem("role"),
            type: 'GET',
            success: function(response) {
                var machineList = JSON.parse(response).results;
                var $ul = $('.currentOrders').append(
                  machineList.map(machine =>
                    $("<tr>").append($("<td>").text(machine[0]))
                        .append($("<td>").text(machine[1])).append($("<td>").text(machine[2]))
                        .append($("<td>").text(machine[3])).append($("<td>").text(machine[4]))
                        .append($("<td>").text(machine[5])).append($("<td>").text(machine[7])).append($("<td>").text(machine[8]))
                  )
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});