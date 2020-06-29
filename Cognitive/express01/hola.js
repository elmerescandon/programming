var express = require('express');
var app = express();

app.get('/',c_inicio);
app.get('/saludo',c_saludo)
app.get('/despedida',c_despedida)

function c_inicio(request,response){
  response.send('<h1>Bienvenido Express-UTEC</h1>');
}

function c_saludo(request,response){
  response.send('<h1>Bienvenido Raul </h1>');
}

function c_despedida(request,response){
  response.send('<h1>Adió Raul </h1>');
}

function c_server(){
  var host = server.address().address;
  var port = server.address().port;
  console.log('Escuchando en puerto http:%s:%s',host,port);
}

var server = app.listen(3000,c_server);
