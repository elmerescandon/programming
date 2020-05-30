-- Clase 30/05 - Sabado S8
-- Ejercicio 1
select * from empleados
where salario > (select salario from empleados where nombre_emp='ALVAREZ');


-- Ejercicio 2
select * from empleados;
select nombre_emp,cod_emp, salario from empleados
where puesto = (select puesto
                    from empleados
                    where nombre_emp = 'MARTINEZ')
AND    salario > (select salario
                  from empleados
                  where nombre_emp = 'MARTINEZ');
                  
-- Ejercicio 3 
select min(salario) from empleados;
select cod_emp, min(salario) 
from empleados 
group by cod_emp -- Salario mínimo por departamento
having min(salario) > (select min(salario)
                       from empleados
                       where cod_emp = 7521);
    
-- Ejericico 4
select * from empleados 
where cod_dept IN (
                    select cod_dept from empleados
                    where salario >= 3000);
-- Ej 5
select nombre_emp, salario
from empleados 
where EXISTS ( select * from empleados where salario >= 6000);