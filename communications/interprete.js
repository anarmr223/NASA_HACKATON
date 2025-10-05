async function getData() {
  try {
    const response = await fetch('http://127.0.0.1:8000/asteroids/');
    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error(error);
    return null;
  }
}

async function mostrarDatos() {
  const data = await getData();
  const text = document.getElementById('text');

  if (data) {
    const nuevoTexto = document.createTextNode(JSON.stringify(data, null, 2));
    text.appendChild(nuevoTexto);
  } else {
    text.textContent = 'Error al obtener los datos 😢';
  }
}

mostrarDatos();