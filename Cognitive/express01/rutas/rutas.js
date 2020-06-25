var express = require('express');
var router  = express.Router(); // El que maneja las rutas

router.get('/',c_inicio);
router.get('/about',c_about);

function c_inicio(req,res){
  res.render('inicio', {
          titulo: "Pagina de inicio",
          nombre: "Raul",
          apellido: "Escandon"
      });

}

function c_about(req,res){
  res.send('Acerca de ... v1.0');
}

module.exports = router;
