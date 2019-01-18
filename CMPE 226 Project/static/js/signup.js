$(function() {
    var dropdownval = "";
    $('document').ready(function() {
        $(".registrationSuccess").hide();
    });
    $(".roleClass").click(function(e) {
        $(".roleBtnClass").text(e.target.text);
        dropdownval = e.target.text;
    });

    $('#btnSignUp').click(function() {

        $.ajax({
            url: '/signUp?inputRole='+dropdownval+'&inputCaId='+sessionStorage.getItem("ca_id"),
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                $(".registrationSuccess").show();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});