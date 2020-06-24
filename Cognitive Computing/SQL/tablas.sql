ALTER SESSION SET NLS_LANGUAGE = SPANISH;
ALTER SESSION SET NLS_TERRITORY = SPAIN;

DROP TABLE EMPLEADOS;
DROP TABLE DEPART;
DROP TABLE SALGRADE;
DROP TABLE INVENTION;
DROP TABLE NATION;


--Tabla Depart
CREATE TABLE DEPART
       (COD_DEPT NUMBER(2) not null	CONSTRAINT pk_dept PRIMARY KEY,
        NOMBRE_DEPT VARCHAR2(14),
        UBICACION VARCHAR2(13) );

INSERT INTO DEPART VALUES
        (10,'CONTABILIDAD','COMAS');
INSERT INTO DEPART VALUES
        (20,'INVESTIGACION','SAN MIGUEL');
INSERT INTO DEPART VALUES
        (30,'VENTAS','MIRAFLORES');
INSERT INTO DEPART VALUES
        (40,'OPERACIONES','LIMA');

--Tabla Empleados
CREATE TABLE EMPLEADOS
       (COD_EMP NUMBER(4) NOT NULL	CONSTRAINT pk_emp PRIMARY KEY,
        NOMBRE_EMP VARCHAR2(10) CONSTRAINT nn_nombemp NOT NULL,
        PUESTO VARCHAR2(15),
        JEFE NUMBER(4) CONSTRAINT fk_jefe REFERENCES empleados(cod_emp),
        FECHA_ING DATE DEFAULT SYSDATE,
        SALARIO NUMBER(7,2) CONSTRAINT ch_sal CHECK(salario>500),
        COMISION NUMBER(7,2) DEFAULT NULL,
        COD_DEPT NUMBER(2) CONSTRAINT fk_coddept REFERENCES depart(cod_dept) );

INSERT INTO EMPLEADOS VALUES
        (7839,'LOPEZ','PRESIDENTE',NULL,'17-NOV-81',5000,NULL,10);
INSERT INTO EMPLEADOS VALUES
        (7698,'BENAVIDES','GERENTE',7839,'1-MAY-81',2850,NULL,30);
INSERT INTO EMPLEADOS VALUES
        (7844,'TORRES','VENDEDOR',7698,'8-SEP-81',1500,0,30);
INSERT INTO EMPLEADOS VALUES
        (7566,'JARA','GERENTE',7839,'2-ABR-81',2975,NULL,20);
INSERT INTO EMPLEADOS VALUES
        (7654,'MARTINEZ','VENDEDOR',7698,'28-SEP-81',1250,1400,30);
INSERT INTO EMPLEADOS VALUES
        (7902,'FARFAN','ANALISTA',7566,'3-DIC-81',3000,NULL,20);
INSERT INTO EMPLEADOS VALUES
        (7499,'ALVAREZ','VENDEDOR',7698,'20-FEB-81',1600,300,30);
INSERT INTO EMPLEADOS VALUES
        (7782,'CASTRO','GERENTE',7839,'9-JUN-81',2450,NULL,10);
INSERT INTO EMPLEADOS VALUES
        (7369,'PEREZ','ADMINISTRATIVO',7902,'17-DIC-80',800,NULL,20);
INSERT INTO EMPLEADOS VALUES
        (7788,'SANCHEZ','ANALISTA',7566,'09-DIC-82',3000,NULL,20);
INSERT INTO EMPLEADOS VALUES
        (7934,'MENDOZA','ADMINISTRATIVO',7782,'23-ENE-82',1300,NULL,10);
INSERT INTO EMPLEADOS VALUES
        (7521,'WONG','VENDEDOR',7698,'22-FEB-81',1250,500,30);
INSERT INTO EMPLEADOS VALUES
        (7900,'JIMENEZ','ADMINISTRATIVO',7698,'3-DIC-81',950,NULL,30);
INSERT INTO EMPLEADOS VALUES
        (7876,'AMPUERO','ADMINISTRATIVO',7788,'12-ENE-83',1100,NULL,20);

--Tabla Salgrade
CREATE TABLE SALGRADE
      ( GRADE NUMBER,
        LOSAL NUMBER,
        HISAL NUMBER );

INSERT INTO SALGRADE VALUES (1,700,1200);
INSERT INTO SALGRADE VALUES (2,1201,1400);
INSERT INTO SALGRADE VALUES (3,1401,2000);
INSERT INTO SALGRADE VALUES (4,2001,3000);
INSERT INTO SALGRADE VALUES (5,3001,9999);


--Tabla Nation
create table nation
(code number(4) constraint nn_code NOT NULL
                constraint pk_code primary key,
nation varchar2(28) constraint nn_nation NOT NULL,
capital varchar2(20),
area number(22),
population number(22));

insert into nation values(56,'West Germany','Bonn',96011,6.1E+07);
insert into nation values(57,'Ghana','Accra',92098,1.3E+07);
insert into nation values(60,'Guatemala','Guatemala City',42042,7714000);
insert into nation values(61,'Guinea','Conakry',94925,5430000);
insert into nation values(66,'Hungary','Budapest',35919,1.1E+07);
insert into nation values(68,'India','New Delhi',1259420,7.3E+08);
insert into nation values(69,'Indonesia','Jakarta',741101,1.7E+08);
insert into nation values(70,'Iran','Teheran',636363,4.2E+07);
insert into nation values(71,'Iraq','Bagdad',163923,1.5E+07);
insert into nation values(73,'Israel','Jerusalen',8219,3958000);
insert into nation values(74,'Italy','Rome',116303,5.7E+07);
insert into nation values(63,'Guyana','Georgetown',83000,833000);
insert into nation values(107,'New Zealand','Wellington',103833,3203000);
insert into nation values(28,'Cape Verde','Praia',1557,297000);
insert into nation values(11,'Bahrain','Manama',258,393000);
insert into nation values(135,'Somalia','Mogadishu',246300,6248000);
insert into nation values(141,'Swaziland','Mbabane',6704,632000);
insert into nation values(77,'Japan','Tokyo',147470,1.2E+07);
insert into nation values(157,'United States of America','Washington',3717813,278000000);
insert into nation values(156,'United Kingdom','London',94526,59000000);
insert into nation values(52,'France','Paris',211209,61100000);

--Tabla Invention
create table invention
(invention varchar2(30) CONSTRAINT nn_inv NOT NULL
			CONSTRAINT pk_inv PRIMARY KEY,
inventor varchar2(30),
year number(4),
nation_code number(4) constraint fk_nat_code REFERENCES NATION(CODE));

insert into invention values('Record Wax.Cylinder','Edison',1888,157);
insert into invention values('Stock Ticker','Edison',1870,157);
insert into invention values('Camera Polaroid Land','Land',1943,157);
insert into invention values('Antiseptic Surgery','Lister',1867,156);
insert into invention values('Pen.Ballpoint','Loud',1888,157);
insert into invention values('Cotton Gin', 'Whitney', 1793,157);
insert into invention values('Machine Gun', 'Gatting', 1851,157);
insert into invention values('Bottle Machine', 'Owens', 1903,157);
insert into invention values('Calculating Machine', 'Babbage', 1823,156);
insert into invention values('Sewing Machine', 'Howe', 1846,157);
insert into invention values('Ice-Making Machine', 'Gorrie', 1851,157);
insert into invention values('Adding Machine', 'Pascal', 1642,52);

COMMIT;
/
