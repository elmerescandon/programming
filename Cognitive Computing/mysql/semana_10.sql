-- 1 Mostrar los casos positivos agrupados por departament, provincia y distrito
select * from positivos group by departamento,provincia,distrito;

-- 2 Mostrar los casos positivos agrupados por sexo
select sexo,count(*) from positivos group by sexo;

-- 3 mostrar la cantidad de pruebas rapidas en la provincia de cusco 
select departamento,provincia,count(metodox) from positivos where departamento='CUSCO' and metodox = 'PR' and provincia = 'CUSCO' group by provincia;

-- 4 mostrar el distrito donde se han hecho mas pruebas rapidas
select departamento, provincia, distrito, count(metodox)
from positivos 
where metodox = 'PR'
group by distrito
order by count(metodox) desc limit 1;

-- 5 mostrar la cantidad de pruebas por meses en la provincia de lima
select departamento, provincia, distrito,count(metodox),substr(fecha_resultado,1,1) as "Mes"
from positivos 
where provincia = 'LIMA' 
group by substr(fecha_resultado,1,1);

-- 6 mostrar la cantidad de pruebas por dia en el distrito de Barranco
select departamento, provincia, distrito,metodox,fecha_resultado
from positivos
where distrito = 'BARRANCO';

select departamento, provincia, distrito,fecha_resultado,str_to_date(fecha_resultado,'%m/%d/%Y') 
from positivos where str_to_date(fecha_resultado,'%m/%d/%Y')  is NULL and provincia ='LIMA';

select extract(month from str_to_date(fecha_resultado,'%m/%d/%Y')) from positivos;

	-- Final de pregunta 6 
select provincia, distrito,fecha_resultado, count(metodox)
from positivos
where distrito = 'BARRANCO'
group by extract(day from str_to_date(fecha_resultado,'%m/%d/%Y'));

-- 7 mostrar el distrito que tiene mas infectados que no sea del departamento de Lima
select departamento,provincia,count(metodox)
from positivos
where provincia != 'LIMA' and substr(provincia,1,3) != 'EN '
group by provincia
order by count(metodox) desc limit 1;

-- 8 mostrar el día donde se infectaron as personas
select fecha_resultado, count(metodox)
from positivos 
group by extract(day from str_to_date(fecha_resultado,'%m/%d/%Y'))
having str_to_date(fecha_resultado,'%m/%d/%Y') is not NULL
order by count(metodox) desc limit 1;

-- 9 mostrar el dia en que se dectectaron mas casos de mujeres
select fecha_resultado, sexo,count(metodox) 
from positivos
where sexo ='FEMENINO' 
group by extract(day from str_to_date(fecha_resultado,'%m/%d/%Y'))
order by count(metodox) desc;

-- 10 mostrar la cantidad de infectados por rangos de edad en multiplos de 10
select floor(cast(edad as unsigned)/10)*10,count(metodox) 
from positivos
group by floor(cast(edad as unsigned)/10)*10;

