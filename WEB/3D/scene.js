import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.153.0/build/three.module.js';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.153.0/examples/jsm/controls/OrbitControls.js';


const scene = new THREE.Scene(); //crear la escena 3D
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
//75 → campo de visión en grados (qué tan abierto es el ángulo de visión).
//2º → relación de aspecto para que no se deforme al ajustar a la ventana.
//los ultimos datos lo mas cercano y lejano que se puede ver
const renderer = new THREE.WebGLRenderer();

const controls = new OrbitControls( camera, renderer.domElement );

renderer.setSize( window.innerWidth, window.innerHeight ); //el tam de lo que queremos renderizar
//setSize(window.innerWidth/2, window.innerHeight/2, false) will render your app at half
document.body.appendChild( renderer.domElement );

const geometry = new THREE.BoxGeometry( 1, 1, 1 );
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
const cube = new THREE.Mesh( geometry, material );
scene.add(cube);
camera.position.set(0, 20, 100);
controls.update();

renderer.render(scene, camera);

function animate() {
    controls.update();
    renderer.render( scene, camera );
    
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
}

renderer.setAnimationLoop( animate );