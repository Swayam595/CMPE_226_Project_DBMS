$(function() {
    $('document').ready(function() {
        $('#inputName').val(sessionStorage.getItem("name"));
        $('#inputEmail').val(sessionStorage.getItem("email_id"));
        $('#inputBankAccount').val(sessionStorage.getItem("bankAccount"));
        $('#inputPassword').val(sessionStorage.getItem("passwordOriginal"));
        $(".updateSuccess").hide();
    });

    $('#updateProfile').click(function() {
        console.log($('form').serialize());
        $.ajax({
            url: '/updateProfile?inputRole='+sessionStorage.getItem("role")+'&inputId='+sessionStorage.getItem("id"),
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                var responseParsed = JSON.parse(response);
                sessionStorage.setItem("name", responseParsed.results._name);
                sessionStorage.setItem("bankAccount", responseParsed.results._bank_account_number);
                sessionStorage.setItem("password", responseParsed.results._hashed_password);
                sessionStorage.setItem("passwordOriginal", responseParsed.results._password);
                $(".updateSuccess").show();
                location.reload();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});