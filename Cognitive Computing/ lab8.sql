-- Ejercicio 2
select max(salario) "Salario Max", min(salario) "Salario Min", 
sum(salario) "Salario Suma" ,
avg(salario) "Salario Promedio"
from empleados;


-- Ejercicio 3
select max(salario) "Salario Max", min(salario) "Salario Min", 
sum(salario) "Salario Suma" ,
avg(salario) "Salario Promedio"
from empleados
group by puesto;

-- Ejercicio 4
select count(nombre_emp), puesto
from empleados
group by puesto;

-- Ejercicio 5
select max(salario) "Salario Max",
min(salario) "Salario Min",
max(salario)- min(salario) "Diferencia"
from empleados;


-- Ejercicio 6
select count(nombre_emp)"Numero de Empleados", puesto
from empleados
group by puesto
having count(puesto) > 3; 

-- Ejercicio 7
select * from empleados group by cod_dept having count(nombre_emp)<=3;
select cod_dept"Departamento",count(cod_dept) "Número de empleados"
from empleados
group by cod_dept
having count(nombre_emp)<= 3 and max(salario)<3000;

-- Ejercicio 8
select e.NOMBRE_EMP, E.cod_dept
from empleados e 
CROSS JOIN depart;

-- Ejercicio 9
select e.NOMBRE_EMP, d.ubicacion
from empleados e NATURAL JOIN depart d;


-- Ejercicio 10
select e.NOMBRE_EMP, d.ubicacion
from empleados e JOIN depart d
on (e.cod_dept = d.cod_dept);

-- Ejercicio 11
select inv.inventor, n.nation
from invention inv join nation n
on (inv.nation_code = n.code);


-- Ejercicio 12 
select e.nombre_emp, e.salario, sal.grade
from empleados e join salgrade sal
on (e. salario between sal.losal and sal.hisal);

-- Ej 13
select nombre_emp, salario, sal.grade
from empleados e join salgrade sal 
on (e. salario between sal.losal and sal.hisal) 
where sal.grade >= 4;

-- Ejercicio 14
select e.NOMBRE_EMP, e.cod_dept, d.ubicacion
from empleados e LEFT OUTER JOIN depart d
on (e.cod_dept = d.cod_dept) 
order by cod_dept;

-- Ejercicio 15


-- Ejercicio 16
select * from empleados;
select * from empleados;
select Jefe.nombre_emp "Jefe", emp.nombre_emp "Empleado"
from empleados Jefe join empleados emp
on (emp.JEFE = Jefe.cod_emp);

-- Ejercicio 17
select Jefe.nombre_emp "Jefe",
emp.nombre_emp "Empleado",
Jefe.salario "Salario Jefe",
emp.salario "Salario Empleado", 
Jefe.salario - emp.salario "Diferencia Salario"
from empleados Jefe join empleados emp
on (emp.JEFE = Jefe.cod_emp);

-- Ejercicio 18
select nombre_emp, fecha_ing 
from empleados
where cod_dept = (select cod_dept from empleados where nombre_emp = '&nombre_emp') ;

-- Ejercicio 19
select cod_emp, nombre_emp, salario 
from empleados
where salario  > (select avg(salario) from empleados);


-- Ejercicio 20
select * from empleados; 
select cod_emp, nombre_emp 
from empleados 
where nombre_emp = ( select nombre_emp 
                     from empleados 
                     where (instr(nombre_emp,'U'))!= 0) ;
-- Ejemplo 21
select e.nombre_emp, d.cod_dept, e.puesto
from empleados e join depart d
on (e.cod_dept = d.cod_dept)
where d.ubicacion = 'SAN MIGUEL';

-- Ejemplo 22
select emp.nombre_emp "Empleado",
emp. salario "Salario",
Jefe.nombre_emp "Jefe"
from empleados Jefe join empleados emp
on (emp.JEFE = Jefe.cod_emp)
where Jefe.puesto = 'PRESIDENTE';


-- Ejemplo 23 
select d.cod_dept,emp.nombre_emp, emp.puesto, d.nombre_dept
from empleados emp join depart d
on (emp.cod_dept = d.cod_dept)
where nombre_dept = 'VENTAS';




-----------------------------
-- Ejercicio 1 
-- Mostrar puestos que tengan mas empleados
select puesto,count(*)
from empleados
group by puesto
 -- Having son condiciones para group
having count(*) >= 3;

-- Ejercicio 2 -- Filtrar con having mas de 2 condiciones
select cod_dept, puesto, count(*) , sum(salario), max(salario), min(salario)
from empleados
group by cod_dept,puesto
having count(*) = 1 and max(salario) > 2500
order by cod_dept,puesto;

-- Ejercicio 3 
-- Las anidadas de grupo no se puede poner con formas fila 
select puesto, round(avg(salario),2)
from empleados 
group by puesto;

-- Ejercicio 4 - Uniones
-- Uniones naturales: Une las tablas según correspondencia
-- Buscara en cada una de las tablas ( si tienen muismo nombre ejectura la primera)
select e.nombre_emp, e.salario, d.nombre_dept,cod_dept
from empleados e NATURAL JOIN depart d;
 
-- Unir el campo en común
select e.nombre_emp, e.salario, d.nombre_dept,cod_dept
from empleados e JOIN depart d
using (cod_dept);

-- Uso del comando ON para unir tablas 
-- Hacer unión de columnas que significan lo mismo pero tienen 
-- diferentes programas 
select e.NOMBRE_EMP, e.salario, d.NOMBRE_DEPT, d.cod_dept, d.ubicacion
from empleados e JOIN depart d
on (e.cod_dept = d.cod_dept) ;

-- Ejercicio 5 
-- Mostrar el nombre de empleado, salario, donde el departament esta
-- ubicando en San Miguel
select e.nombre_emp, e.salario, d.ubicacion
from empleados e join depart d
on (e.cod_dept = d.cod_dept)
where d.ubicacion = 'SAN MIGUEL';
--group by d.ubicacion;

-- Visualizar
select * from depart; 
select * from empleados; 
select * from nation; 
select * from invention;
select * from cat; 

select * from nation;
-- Ejercicio 6
-- Mostrar las invenciones (invention, inventor) 
select inv.invention, inv.invention, n.nation
from invention inv join nation n
on (inv.nation_code = n.code)
where n.nation in ('United States of America','India');


-- Ejercicio 7
select * from empleados;
select e.nombre_emp jefe, j.nombre_emp empleado
from empleados e join empleados j
on (j.JEFE = e.cod_emp);