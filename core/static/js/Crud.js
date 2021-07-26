$(document).ready(function(){
    //filtrar();
});

function filtrar(){   
    console.log('ESTOY EN FILTRAR, antes del AJAX')
    var cat = $('#idCat').val();
    console.log(cat)
        $.ajax({
            type:'POST',
            url: 'filtro',
            data: {'cat': cat},
            dataType: 'json',
            success: function (data) {
                console.log('RECIBIENDO LOS DATOS PARA UTILIZARLOS EN EL SELECT!!')
                console.log(data)
                $('#idProd ').html('') //Esto es para refrescar el options y evitar que se dupliquen las listas
                $.each(data, function(index, value ){                    
                    $('#idProd ').append(
                        '<option value="'+ value[0] +'">'+ value[1] +'</option>')
                })//parentesis del each                
            }
        });
    }