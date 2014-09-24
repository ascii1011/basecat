jQuery(document).ready(function () {
    var lines = ["out0", "out1", "out2", "out3", "out4", "out5", "out6", "out7", "out8", "out9"];

    $.each( lines, function(index, value){
        $("#com").prepend('<div id="'+value+'" class="line">&nbsp;</div>');
    });
/*
    $("#com").append('<div class="line" id="out9">&nbsp;</div>');
    $("#com").append('<div class="line" id="out8">&nbsp;</div>');
    $("#com").append('<div class="line" id="out7">&nbsp;</div>');
    $("#com").append('<div class="line" id="out6">&nbsp;</div>');
    $("#com").append('<div class="line" id="out5">&nbsp;</div>');
    $("#com").append('<div class="line" id="out4">&nbsp;</div>');
    $("#com").append('<div class="line" id="out3">&nbsp;</div>');
    $("#com").append('<div class="line" id="out2">&nbsp;</div>');
    $("#com").append('<div class="line" id="out1">&nbsp;</div>');
    $("#com").append('<div class="line" id="out0">&nbsp;</div>');
  */  
    $('#textinput').keydown( function(e) {
        var key = e.charCode ? e.charCode : e.keyCode ? e.keyCode : 0;
        if(key == 13) {
            //e.defaultPrevented();
            
            var $uinput = $(this).val();
            $(this).val('');
            
            $.ajax({
                "type": "POST",
                "dataType": "json",
                "url": "/brain/",
                "data": { uinput: $uinput, },
                "success": function(result) {
                    $('#out9').html( $('#out8').html() );
                    $('#out8').html( $('#out7').html() );
                    $('#out7').html( $('#out6').html() );
                    $('#out6').html( $('#out5').html() );
                    $('#out5').html( $('#out4').html() );
                    $('#out4').html( $('#out3').html() );
                    $('#out3').html( $('#out2').html() );
                    $('#out2').html( $('#out1').html() );
                    $('#out1').html( $('#out0').html() );                
                    $('#out0').html( result['uinput'] );
                },
            });           
        }   
        
    });
});
