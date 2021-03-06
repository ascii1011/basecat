jQuery(document).ready(function () {
    var lines = ["out0", "out1", "out2", "out3", "out4", 
                 "out5", "out6", "out7", "out8", "out9",
                 "out10", "out11", "out12", "out13", "out14"];

    var ui = {
        'lines': 14
        }

    function display_handler(r) {
        //console.log('r: ');
        console.log( r.output );
        var o = r['output']['data'];
        console.log('o: '+o);
        if (o.constructor == Array) {
            console.log('ary');
            $.each(o, function(index, val) {
                com_update( val, r.output.klass );
                });
        } else if (o.constructor == Object) {
            console.log('obj');
            $.each(o, function(key, val) {
                com_update( key+': '+val, r.output.klass );
                });
        } else {
            console.log('other: '+o.constructor);
            com_update( o, r.output.klass );
        }
    };
    
    function comm_handler(i) {    
        console.log('commencing ajax cleaning');
        $.ajax({
            "type": "POST", "dataType": "json",
            "url": "/brain/", "data": {i:i,},
            "success": function(o) { 
                console.log('ajax injected.');
                display_handler(o);
            },
        });
    };

    function com_update( data, klass ) {
        var $s = '';
        var $d = '';    
        var lin = 14;
        console.log('com_update with '+data);

        for (i = ui.lines; i > 0; i--) {
            $s = $('#out'+(i-1));
            $d = $('#out'+i);
            
            console.log($s.html()+' -> '+$d.html());

            $d.removeClass().addClass( $s.attr('class') );
            $d.html( $s.html() );
        }

        if (klass == '') {
            klass = 'white'
        }
        console.log('klass found');
        $('#out0').removeClass().addClass( klass );

        console.log('data: '+data);
        $('#out0').html( data );
    };
      
    function com_update2( line0 ) {
        $('#out14').html( $('#out13').html() );
        $('#out13').html( $('#out12').html() );
        $('#out12').html( $('#out11').html() );
        $('#out11').html( $('#out10').html() );
        $('#out10').html( $('#out9').html() );
        $('#out9').html( $('#out8').html() );
        $('#out8').html( $('#out7').html() );
        $('#out7').html( $('#out6').html() );
        $('#out6').html( $('#out5').html() );
        $('#out5').html( $('#out4').html() );
        $('#out4').html( $('#out3').html() );
        $('#out3').html( $('#out2').html() );
        $('#out2').html( $('#out1').html() );
        $('#out1').html( $('#out0').html() );                
        $('#out0').html( line0 );
    };
    
    function create_display() {
        
        for (i=0; i < ui.lines; i++) {
            $("#com").prepend('<div id="'+value+'" class="white">&nbsp;</div>');
        }
    }


    $.each( lines, function(index, value){
        $("#com").prepend('<div id="'+value+'" class="white">&nbsp;</div>');
    });

    comm_handler(0);

    $('#textinput').keydown( function(e) {
        var key = e.charCode ? e.charCode : e.keyCode ? e.keyCode : 0;
        if(key == 13) {            
            var $i = $(this).val();
            $(this).val('');            
            comm_handler($i);
        }   
        
    });
});
