function login() {
    var uname=$('#stu_name').val();
    var pwd=$('#stu_pwd').val();
    $.post('https://xn--jrx586dglk.eu.org/login.php', JSON.stringify({ uname: uname, pwd: pwd}))
        .done(function (resp) {
            console.log(resp.code);
            console.log(resp.message);
            if (resp.code == 200) {
                $('.m-auto').html(resp.message);
                $('.m-auto').removeClass('d-none');
                $.cookie('uname',uname, { expires: 1 });
                setTimeout('window.location.reload();', 500);
            } else {
                $('.m-auto').html(resp.message);
                $('.m-auto').removeClass('d-none');
                            }
        })
        .fail(function (err) {
            $('.m-auto').html(err.responseText);
            $('.m-auto').removeClass('d-none');
                     
        });
 return false;  
}
$(document).ready(function () {
    //modihu 3-20
    if($.cookie('uname')==undefined){
        $('#modal-493752').click();
    }
    
}
)