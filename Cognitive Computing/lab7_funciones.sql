-- Ejercicio #1
select nombre_emp "Nombres",salario "Salario", 
round(salario/31,1) "Salario Diario Redondeo 1",
trunc(salario/31,1) "Salario Diario Truncado 1",
round(salario/31,2) "Salario Diario Redondeo 2",
trunc(salario/31,2) "Salario Diario Truncado 2"
from empleados;

-- Ejercicio #2 
select nombre_emp "Nombres",
fecha_ing,
fecha_ing+400 "Inicio vacaciones",
fecha_ing+431 "Fin vacaciones"
from empleados
where round(sysdate - fecha_ing) between 11000 and 14500;


-- Ejercicio #3
select sysdate "Fecha Actual", -- Fecha Actual
last_day(sysdate) "Último día del mes", -- Último día del presente mes
next_day(sysdate,'FRIDAY')"Viernes siguiente",--El próximo viernes
sysdate-extract(day from last_day(sysdate)) "Hace un mes", -- Fecha de hace un mes (número de días del mes) 
12 -extract(month from sysdate) "Meses para Diciembre" -- Meses restantes para Diciembre
from dual;


-- Ejercicio #4
-- Ubicacion de todo departamento
-- Literal, Iniciales (mayus), iNICIALES (minus)
-- Longitud de carateres
-- Posición de la primera letra S
select ubicacion, INITCAP(ubicacion)"Mayúscula Inicial",lower(ubicacion)"Minúscula Inicial",
length(ubicacion) "Tamaño", instr(ubicacion,'S') "Primera S"
from depart;

-- Ejercicio #5
-- CODE/NATION/CAPITAL/AREA/POPULATION
select upper(nation) "Nación",
upper(substr(nation,1,2))"Iniciales",
upper(substr(nation,length(nation)-1,2)) "Finales"
from nation;


-- Ejercicio #6
select nation,area*100 "Area 100 veces" ,population "Población", 
    CASE 
        WHEN area*100>population THEN 'GREATEST'
        ELSE 'LEAST' 
        END COMPARACION
from nation;


-- Ejercicio #7
select * from depart; 
select concat(concat(INITCAP(nombre_dept),' se ubica en '),initcap(ubicacion)) "Oración"
from depart;

-- Ejercicios 8
-- Nombres, Salarios, Comisiones, Sueldos (salario+comision) 
select * from empleados;
select nombre_emp "Nombre",
salario "Salario",
comision "Comisión",
salario+comision,salario+comision"Sueldo"
from empleados
order by salario;


-- Ejercicio 9
select nombre_emp "Nombre",
salario "Salario",
nvl(comision,0) "Comisión",
nvl(salario+comision,salario+nvl(comision,0))"Sueldo"
from empleados
order by salario;

-- Ejercicio 10
select nombre_emp "Nombre",
salario "Salario Mensual",
nvl(comision,0) "Comisión mensual",
nvl(salario+comision,salario+nvl(comision,0))"Sueldo Mensual",
12*(salario + nvl(comision,0)) "Sueldo Anual"
from empleados
order by salario;

-- Ejercicio 11
select nombre_emp,
concat('S./',to_char(salario)) "Sueldo (Soles)"
from empleados;  


-- Ejercicio 12
--Martes, 10 de MAYO del 2013 - 10:10:00
select to_char(sysdate,'Day ","  DD "de" Month "del" YYYY HH:MI:SS AM' ) Fecha from dual;

-- Ejercicio 13
-- Nombre de empleados
-- Longitud si inician con A o terminan con Z
select initcap(nombre_emp),
    CASE 
        WHEN substr(nombre_emp,1,1) = 'A' THEN length(nombre_emp)
        WHEN substr(nombre_emp,-1,1) = 'Z' THEN length(nombre_emp)
        ELSE NULL
    END Condicion
from empleados;

-- Ejercicio 14
select initcap(nombre_emp) || ' gana ' || salario 
|| ', pero su salario anual es ' || 12*salario Reporte
from empleados;


-- Ejercicio 15
select nombre_emp  || '   ' ||
fecha_ing || '   ' ||
to_char(fecha_ing,'DAY') || '   ' ||
to_char(fecha_ing,'MONTH')|| '   ' ||
to_char(fecha_ing,'YYYY') REPORTE
from empleados;


-- Ejercio 16
select nombre_emp || '   ' ||
coalesce(to_char(comision),'SIN COMISIÓN') "COMISION" 
FROM EMPLEADOS;

-- Ejercicio 17
select nombre_emp || '   ' ||salario || '   ' ||
    CASE
        WHEN salario>4000 THEN 'Nivel 1'
        WHEN salario>=3000 and salario<=4000 THEN 'Nivel 2'
        WHEN salario>=2000 and salario<3000 THEN 'Nivel 3'
        WHEN salario<2000 THEN 'Nivel 4'
        ELSE 'Error'
        END "REPORTE"
from empleados;