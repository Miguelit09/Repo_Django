const ficha = document.getElementById("ficha");
const nombre = document.getElementById("nombre");
const apellidos = document.getElementById("apellidos");
const correo = document.getElementById("correo");
const telefono = document.getElementById("telefono");
const genero = document.getElementsByName("genero");
const ciudad = document.getElementById("ciudad");
const gustos = document.getElementsByName("gustos");
const enviar = document.getElementById("enviar");

let reFicha = /^[a-zA-Z]{3}_[0-9]{5}$/;
let reNombres = /^[a-zA-Z ]{2,20}$/;
let reCorreo = /^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$/;
let reTelefono = /^[0-9]{10}$/;


const bordeVerde = function (campo) {
  if (campo.classList.contains("borde-rojo")) {
    campo.classList.remove("borde-rojo");
  }
  campo.classList.add("borde-verde");
}

const bordeRojo = function (campo) {
  if (campo.classList.contains("borde-verde")) {
    campo.classList.remove("borde-verde");
  }
  campo.classList.add("borde-rojo");
}


const validarFicha = function () {
  if (!reFicha.test(ficha.value)) {
    e.preventDefault()
    alert("Corrija")
    // reworkear las funciones
  }
}

const validarSoloLetras = function (campo) {
  (reNombres.test(campo.value)) ? bordeVerde(campo) : bordeRojo(campo)
}

const validarCorreo = function (campo) {
  (reCorreo.test(campo.value)) ? bordeVerde(campo) : bordeRojo(campo)
}

const validarTelefono = function (e, campo) {
  (reTelefono.test(campo.value)) ? bordeVerde(e, campo) : bordeRojo(e, campo)
}

const letras = function (e) {
  const key = e.keyCode || e.which;
  const tecla = String.fromCharCode(key).toLowerCase();
  const letras = "áéíóúabcdefghijklmnopqrstuvwxyz";
  const especiales = ['8', '32', '37', '39', '46'];
  let tecla_especial = false
  for (const i in especiales) {
    if (key == especiales[i]) {
      tecla_especial = true;
      break;
    }
  }
  if (letras.indexOf(tecla) == -1 && !tecla_especial) {
    e.preventDefault()
  }
}



const numeros = (e) => {
  //Validamos que el keyCode corresponda a las teclas de los números
  if ((e.keyCode < 48 || e.keyCode > 57) && e.keyCode) {
    e.preventDefault()
  }
}

const validarGenero = function (e) {
  let genero_valido = 0
  for (const boton of genero) {
    if (boton.checked) {
      genero_valido = boton.value
      break
    }
  }
  if (genero_valido === 0) {
    e.preventDefault()
    alert("Indique un género")
  }
}

const validarCiudad = function (e) {
  if (ciudad.value === "") {
    e.preventDefault()
    alert("Indique una ciudad")
  }
}

const validarGustos = function (e) {
  let checkbox_activos = 0
  for (const box of gustos) {
    if (box.checked) {
      checkbox_activos += 1
    }
  }
  if (checkbox_activos < 3) {
    e.preventDefault()
    alert("Seleccione mínimo 3 gustos")
  }
}

ficha.addEventListener('blur', () => {
  validarFicha(ficha);
})



apellidos.addEventListener('blur', () => {
  validarSoloLetras(apellidos);
})

correo.addEventListener('blur', () => {
  validarCorreo(correo);
})

nombre.addEventListener('keypress', letras)
telefono.addEventListener('keypress', numeros)


enviar.addEventListener('click', () => {
  validarFicha(ficha);
})
enviar.addEventListener("click", validarGenero)
enviar.addEventListener("click", validarCiudad)
enviar.addEventListener("click", validarGustos)



