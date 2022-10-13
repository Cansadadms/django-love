(function ($) {
    "use strict";

    /* Focar caixa e ñ deixar os textos ficarem sobrepostos */
    $('.input100').each(function(){                     /* cadastro */
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })
    })
    $('.input-login').each(function(){                   /* login */
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })
    })

})(jQuery);