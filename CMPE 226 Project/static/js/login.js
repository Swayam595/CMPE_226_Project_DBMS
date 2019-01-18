$(function() {
    var dropdownval = "";

    $(".roleClass").click(function(e) {
        $(".roleBtnClass").text(e.target.text);
        sessionStorage.setItem("role", dropdownval);
        dropdownval = e.target.text;
    });

    $('#btnLogin').click(function() {
        sessionStorage.setItem("email_id", dropdownval);
        sessionStorage.setItem("passwordOriginal", $('#inputPasswordLogin').val());
        $.ajax({
            url: '/login?inputRole='+dropdownval,
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(JSON.parse(response));
                sessionStorage.setItem("email_id", JSON.parse(response).results[0][1]);
                sessionStorage.setItem("id", JSON.parse(response).results[0][0]);
                sessionStorage.setItem("name", JSON.parse(response).results[0][2]);
                sessionStorage.setItem("password", JSON.parse(response).results[0][3]);
                sessionStorage.setItem("bankAccount", JSON.parse(response).results[0][4]);
                sessionStorage.setItem("role", dropdownval);
                if(dropdownval=="ca"){
                    window.location.replace("http://localhost:5000/showAdmin");
                } else if(dropdownval=="csp") {
                    window.location.replace("http://localhost:5000/showCsp");
                } else {
                    window.location.replace("http://localhost:5000/showCustomerAccountDisplay");
                }
            },
            error: function(error) {
                $(".errorText").text(JSON.parse(error.responseText).error);
                console.log(error);
            }
        });
    });
});