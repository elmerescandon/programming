const config = {
  apiKey: "AIzaSyD3NTSE7TrVVrqt5nAsTrxaGhPcznJ5jvU",
  authDomain: "cognitive-crowdie.firebaseapp.com",
  databaseURL: "https://cognitive-crowdie.firebaseio.com",
  projectId: "cognitive-crowdie",
  storageBucket: "cognitive-crowdie.appspot.com",
  messagingSenderId: "1059415121522",
  appId: "1:1059415121522:web:87926ef38dc97db9642ceb",
  measurementId: "G-G68548KL01"
}

firebase.initializeApp(config); // NOTE: Incializar la app
const firestore = firebase.firestore();

// NOTE: Crear los valores constantes para que nuestro programa pueda
// detectar las acciones realizadas por los botones
const posts = document.querySelector("#posts");
const createForm = document.querySelector("#createForm");
const progressBar = document.querySelector("#progressBar");
const progressHandler = document.querySelector("#progressHandler");
const postSubmit = document.querySelector("#postSubmit");
const openNav = document.querySelector("#openNav");
const closeNav = document.querySelector("#closeNav");

// Obtener la información de nuestros posts
const getPosts = async() =>{
  let postsArray = [];
  let docs = await firebase.firestore().collection("posts").get().catch(err=> console.log(err));
  docs.forEach(doc => {
    postsArray.push({"id":doc.id,"data":doc.data()});
  });
  createChildren(postsArray);
}

const createChildren = async (arr) => {
  if (posts != null){ // Verificar si es HTML
    arr.map(post=>{
      let div = document.createElement("div");
      let cover = document.createElement("div");
      let anchor = document.createElement("a");
      let anchorNode = document.createTextNode(post.data.title);
      anchor.setAttribute("href","post.html#/"+post.id); // Crear una página que tenga el post y el id
      anchor.appendChild(anchorNode);
      cover.style.backgroundImage = "url(" + post.data.cover + ")";
      div.classList.add("post");
      div.appendChild(cover);
      div.appendChild(anchor);
      posts.appendChild(div);
    })
    }
  }


// Asegurarse de que funcione nuestros ID de crear form
// en ambas páginas, en caso no dar cuenta de ello al programa
if (createForm != null){
  let d; // NOTE: Hacer la función global dentro del statement
  createForm.addEventListener("submit",async(e)=>{
    e.preventDefault();
    if(document.getElementById("title").value != "" && document.getElementById("content").value != "" &&
    document.getElementById("cover").files[0] != ""){
      let title = document.getElementById("title").value;
      let content = document.getElementById("content").value;
      let cover = document.getElementById("cover").files[0];
      console.log(cover);

      const storageRef = firebase.storage().ref();
      // NOTE: Bucket guarda todos los valores que se guardan
      const storageChild = storageRef.child(cover.name); // Para crear el path

      console.log("Uploading file....");
      const postCover = storageChild.put(cover); // Upload de file

      // Esperar  a que el proceso termine, lee línea por línea. Pero tiene que esperar a postear el postCover
      await new Promise((resolve) =>{
        // Nos permitirá esperar mientras el archivo sube y hacer alguna funcion
        postCover.on("state_changed",(snapshot)=>{
          let progress = (snapshot.bytesTransferred / snapshot.totalBytes * 100);
          console.log(Math.trunc(progress));

          if(progressHandler != null){
            progressHandler.style.display = true;
          }
          if (postSubmit != null){
            postSubmit.disabled = true;
          }
          if (progressBar != null){
            progressBar.value = progress;
          }
        },(error) =>{
          // Callback functions cada que ocurre esto, para poder manejar los erores
          console.log(error);
        },async()=>{
          const downloadURL = await storageChild.getDownloadURL();
          d = downloadURL;
          console.log(d);
          resolve(); // Ya acabo, entonces puede terminar con la función de waitint
        });
      });
      const fileRef = await firebase.storage().refFromURL(d);

      let post = {
        title, // Los valores que tiene nuestra imagen, son Keys quese han puesto de la imagen
        content,
        cover:d, // https:firebase:my-page...
        fileref: fileRef.location.path // nos dará el path de la imagen image.jpg
      }

      await firebase.firestore().collection("posts").add(post); // Collections es una tabla de las imagen, sino se crea uno "posts"
      // add hace un push hacia la base de datos -> Se puede hacer un handler, que maneje ese envío
      console.log("Post Added Successfully");

      if (postSubmit != null){
        window.location.replace("index.html");
        postSubmit.disabled = false;
      }

    } else{
      console.log("must fill all the inputs")
    }
  });
}


// Check if the dom is not fully loaded - Todo cargó
document.addEventListener("DOMContentLoaded",(e)=>{
  getPosts();
});



// Funciones del navegador
openNav.addEventListener("click",(e)=>{
  document.getElementById("nav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}); // Click event, cada que se hace click

closeNav.addEventListener("click",(e)=>{
  e.preventDefault(); // Vuelva a su estado normal
  document.getElementById("nav").style.width = "0px";
  document.getElementById("main").style.marginLeft = "";
})
