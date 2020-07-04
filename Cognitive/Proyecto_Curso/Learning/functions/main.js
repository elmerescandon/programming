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
const loading = document.querySelector("#loading");
const editButton = document.querySelector("#edit");
const deleteButton = document.querySelector("#delete");
const singlePost = document.querySelector("#post");
const editFormContainer = document.querySelector("#editFormContainer");
let editMode = false;

let lastVisible;

let postsArray = [];
let size;
let postsSize;

// Obtener la información de nuestros posts
const getPosts = async() =>{
  // let postsArray = [];
  // let docs = await firebase.firestore().collection("posts").get().catch(err=> console.log(err));
  // docs.forEach(doc => {
  //   postsArray.push({"id":doc.id,"data":doc.data()});
  // });
  // createChildren(postsArray);
  let docs;
  let postsRef = firebase.firestore().collection("posts").orderBy("title").limit(3);


  let _size = await firebase.firestore().collection("posts").get();
  size = _size.size;

  await postsRef.get().then(documentSnapshots =>{
    docs = documentSnapshots;
    console.log(docs);
    lastVisible = documentSnapshots.docs[documentSnapshots.docs.length-1];
    console.log("last",lastVisible);
  });
  docs["docs"].forEach(doc=>{
    postsArray.push({"id":doc.id,"data":doc.data()});
  })

  if(postsArray.length >0){
    pagination.style.display = "block"; // Añadira lo de abaoj
  }else{
    pagination.style.display = "none";
  }
}


const getPost = async() => {
  let postId = getPostIFromURL();
  if (loading != null){

    // Si loading no está existe entonces se le va a dar un valor
    loading.innerHTML = "<div><div class='lds-dual-ring'></div><p>Loading...</p></div>"; // Para escribir mientras esta cargando o no hay nada
  }
  let post = await firebase.firestore().collection("posts").doc(postId).get().catch(err=>console.log(err));
  if (loading != null){ // Luego de que cargó todo y obtuvo la imagen, eliminará la barra de laoding
    loading.innerHTML = "";
  }

  if(post && deleteButton != null){ // Si es que existe un post, entonces no tiene porque mostrarse en la pantalla
    deleteButton.style.display = "block";
  }

  if(post && editButton != null){
    editButton.style.display = "block";
  }

  createChild(post.data()); // Data mantiene los datos del post, todo

}

const createChild = (postData) =>{
  if (singlePost != null){ // Si esxiste la variable post en neustr apágina
    let div = document.createElement("div");

    let img_post = document.createElement("img");
    img_post.setAttribute("src",postData.cover);
    img_post.setAttribute("loading","lazy");

    let title = document.createElement("h3");
    let titleNode = document.createTextNode(postData.title);// Text is an object
    title.appendChild(titleNode);

    let content = document.createElement("div");
    let contentNode = document.createTextNode(postData.content);
    content.appendChild(contentNode);

    div.appendChild(img_post);
    div.appendChild(title);
    div.appendChild(content);
    post.appendChild(div);
  }
}


const getPostIFromURL = ()=>{
  let postLocation = window.location.href; // NOTE: Agarra todo el URL
  let hrefArray = postLocation.split("/");
  let postId = hrefArray.slice(-1).pop(); // Se va a retornar el ID para poder cargar la foto de la base de datos

  return postId;
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


const appendEditForm = async() => {
  let postId = getPostIFromURL();
  let post = await firebase.firestore().collection("posts").doc(postId).get().catch(err=> console.log(err));

  let d;

  let form = document.createElement("form");
  form.setAttribute("method","POST");
  form.setAttribute("id","editForm");

  let titleInput = document.createElement("input");
  titleInput.setAttribute("value",post.data().title);
  titleInput.setAttribute("id","editTitle");

  let contentTextarea = document.createElement("textarea");
  contentTextarea.setAttribute("id","editContent");

  let coverFile = document.createElement("input");
  coverFile.setAttribute("type","file");
  coverFile.setAttribute("id","editCover");

  let oldCover = document.createElement("input");
  oldCover.setAttribute("type","hidden");
  oldCover.setAttribute("id","oldCover");

  let submit = document.createElement("input");
  submit.setAttribute("value","Update Post");
  submit.setAttribute("type","submit");
  submit.setAttribute("id","editSubmit");

  form.appendChild(titleInput);
  form.appendChild(contentTextarea);
  form.appendChild(coverFile);
  form.appendChild(oldCover);
  form.appendChild(submit);
  editFormContainer.appendChild(form);

  document.getElementById("editContent").value = post.data().content;
  document.getElementById("oldCover").value = post.data().fileref;

  document.querySelector("#editForm").addEventListener("submit",async(e)=>{
    e.preventDefault();
  const postId = await getPostIFromURL();

    if(document.getElementById("editTitle").value != "" && document.getElementById("editContent").value != ""){
      if(document.getElementById("editCover").files[0] != undefined ){
        const cover = document.getElementById("editCover").files[0];
        const storageRef = firebase.storage().ref();
        const storageChild = storageRef.child(cover.name);

        console.log("Updating file...");

        const postCover = storageChild.put(cover);
        await new Promise((resolve) =>{
          // Nos permitirá esperar mientras el archivo sube y hacer alguna funcion
          postCover.on("state_changed",(snapshot)=>{
            let progress = (snapshot.bytesTransferred / snapshot.totalBytes * 100);
            console.log(Math.trunc(progress));

            if(progressHandler != null){
              progressHandler.style.display = true;
              console.log("Estoy acá")
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

        await storageRef.child(document.getElementById("oldCover").value).delete().catch(err=>{
          console.log(err);
        });
        console.log("Previous image deleted Successfully");;

        let post = {
          title: document.getElementById("editTitle").value,
          content: document.getElementById("editContent").value,
          cover: d,
          fileref: fileRef.location.path
        }

        await firebase.firestore().collection("posts").doc(postId).set(post,{merge:true});
        location.reload();


      }else{
          await firebase.firestore().collection("posts").doc(postId).set({
            title: document.getElementById("editTitle").value,
            content: document.getElementById("editContent").value
          },{merge:true});

          location.reload();
      }

    }else{
      console.log("You need to fill the inputs")
    }

  })


}

if(editButton !=null){
  editButton.addEventListener("click",()=>{
    if(editMode == false){
      editMode = true;
      console.log("Enabling Edit Mode");

      appendEditForm();
    }
    else{
      editMode = false;
      console.log("Disabling Edit Mode");

      removeEditForm();
    }
  })
}

const removeEditForm = () =>{
  let editForm = document.getElementById("editForm"); // Se llama a la funcióñ anterior
  editFormContainer.removeChild(editForm);
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
            progressHandler.style.display = "block";
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

if(deleteButton != null){
  deleteButton.addEventListener("click", async()=>{
    const postId = getPostIFromURL();
    let post = await firebase.firestore().collection("posts").doc(postId).get().catch(err=>console.log(err));

    const storageRef = firebase.storage().ref();
    await storageRef.child(post.data().fileref).delete().catch(err=> console.log(err));

    await firebase.firestore().collection("posts").doc(postId).delete();

    window.location.replace("index.html");
  })
}



// Check if the dom is not fully loaded - Todo cargó
document.addEventListener("DOMContentLoaded",(e)=>{
  getPosts();
  getPost();
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
