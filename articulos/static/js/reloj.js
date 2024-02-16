function mueveReloj(){
    momentoActual = new Date()
    hora = momentoActual.getHours()
    minuto = momentoActual.getMinutes()
    segundo = momentoActual.getSeconds()

    str_hora = new String (hora)
    if(str_hora.length == 1)
    hora = "0" + hora;
        
    str_minuto = new String (minuto)
    if(str_minuto.length == 1)
    minuto = "0" + minuto;

    str_segundo = new String (segundo)
    if(str_segundo.length == 1)
    segundo = "0" + segundo;
    
   
    horaImprimible = hora + ":" + minuto + ":" + segundo
    document.form_reloj.reloj.value = horaImprimible

    setTimeout("mueveReloj()",1000)
}

function mostrarPopup() {
    window.open("api.html", "RazasCaninos", "width=1200,height=700");
  }

function togglePopup() {
    const popup = document.getElementById("popup");
    popup.classList.toggle("active");
}

