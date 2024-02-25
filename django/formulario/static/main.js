const ficha = document.getElementById("ficha");
const nombre = document.getElementById("nombre");
const apellidos = document.getElementById("apellidos");
const correo = document.getElementById("correo");
const telefono = document.getElementById("telefono");

let reFicha = /^[a-zA-Z]{3}_[0-9]{5}$/;
let reNombres = /^[a-zA-Z ]{2,20}$/;
let reCorreo = /^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$/;
let reTelefono = /^[0-9]{10}$/;
let elementoActivo = document.querySelector('input[name="status"]:checked');
if (elementoActivo) {
  alert(elementoActivo.value);
} else {
  alert('No hay ninún elemento activo');
}

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


const validarFicha = function (campo) {
  (reFicha.test(campo.value)) ? bordeVerde(campo) : bordeRojo(campo)
}

const validarSoloLetras = function (campo) {
  (reNombres.test(campo.value)) ? bordeVerde(campo) : bordeRojo(campo)
}

const validarCorreo = function (campo) {
  (reCorreo.test(campo.value)) ? bordeVerde(campo) : bordeRojo(campo)
}

const validarTelefono = function (campo) {
  (reTelefono.test(campo.value)) ? bordeVerde(campo) : bordeRojo(campo)
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

ficha.addEventListener('blur', () => {
  validarFicha(ficha);
})



nombre.addEventListener('keypress', letras)

apellidos.addEventListener('blur', () => {
  validarSoloLetras(apellidos);
})

correo.addEventListener('blur', () => {
  validarCorreo(correo);
})

// telefono.addEventListener('blur', () => {
//   validarTelefono(telefono);
// })
telefono.addEventListener('keypress', numeros)
