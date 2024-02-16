//Funcion que valida un formulario
$(function(){
    $("#formulario").validate({
        rules:{
            nom:{
                required:true,
                minlength: 3},
            email:{
                required:true,
                email:true},
            fono:{
                required:true,
                number: true,
                minlength: 9},
            com:{
                required:true,
                minlength: 25},
            dir:{
                required:true,
                minlength: 3
                },
            
        },//rules

        messages:{
            nom:{
                required:'*Ingrese nombre',
                minlength:'Caracteres insuficientes (3)'},

            email:{
                required:'*Ingrese correo electronico',
                email:'Formato de correo no valido'},

            fono:{
                required:'*Ingrese numero de telefono',   
                minlength:'Digitos Insuficientes (9)'},

            com:{
                required:'*Cuentenos sobre su experiencia',
                minlength:'Caracteres insuficientes (25)'},
            dir:{
                required:'*Ingrese su dirección',
                minlength:'Caracteres insuficientes (3)'}
        
        },
    })
}),

    //función que cambia el color de fondo a orange
    function colorNav(obj){
        obj.style.backgroundColor='rgba(179, 157, 207, 0.507)';
    }

    function transparenteNav(obj){
        obj.style.backgroundColor='transparent';
    }
