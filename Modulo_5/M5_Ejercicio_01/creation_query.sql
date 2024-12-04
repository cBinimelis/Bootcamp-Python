-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://github.com/pgadmin-org/pgadmin4/issues/new/choose if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.invernadero
(
    invernadero_id serial,
    nombre character varying(80),
    direccion character varying(120),
    comuna character varying(50),
    longitud double precision,
    latitud double precision,
    PRIMARY KEY (invernadero_id)
);

CREATE TABLE IF NOT EXISTS public.sector
(
    sector_id serial,
    nombre character varying(80),
    invernadero_id integer,
    PRIMARY KEY (sector_id)
);

CREATE TABLE IF NOT EXISTS public.planta
(
    planta_id bigserial,
    fecha_plantacion date,
    temporada_cultivo character varying(30),
    especie_id integer,
    PRIMARY KEY (planta_id)
);

CREATE TABLE IF NOT EXISTS public.sensor
(
    sensor_id bigserial,
    nombre character varying(50),
    fecha_instalacion date,
    PRIMARY KEY (sensor_id)
);

CREATE TABLE IF NOT EXISTS public.medicion_sensor
(
    tiempo_medicion timestamp without time zone NOT NULL,
    temperatura integer,
    humedad integer,
    luminosidad integer,
    altura numeric,
    sensor_id integer,
    PRIMARY KEY (tiempo_medicion, sensor_id)
);

CREATE TABLE IF NOT EXISTS public.especie
(
    especie_id serial,
    nombre character varying(50)[],
    PRIMARY KEY (especie_id)
);

CREATE TABLE IF NOT EXISTS public.tratamiento
(
    tratamiento_id serial,
    cantidad_aplicada integer,
    fecha_tratamiento date,
    tipo_tratamiento_id integer,
    planta_id integer,
    PRIMARY KEY (tratamiento_id)
);

CREATE TABLE IF NOT EXISTS public.tipo_tratamiento
(
    tipo_tratamiento_id serial,
    nombre character varying(100),
    unidad_medida character varying(20),
    PRIMARY KEY (tipo_tratamiento_id)
);

CREATE TABLE IF NOT EXISTS public.actuador
(
    actuador_id serial,
    temperatura_objetivo integer,
    humedad_objetivo integer,
    PRIMARY KEY (actuador_id)
);

CREATE TABLE IF NOT EXISTS public.trabajador
(
    trabajador_id serial,
    "RUT" character varying(10),
    nombre character varying(50),
    apellidos character varying(100),
    PRIMARY KEY (trabajador_id)
);

CREATE TABLE IF NOT EXISTS public.turno
(
    turno_id serial,
    nombre character varying(15),
    horario_entrada time without time zone,
    horario_salida time without time zone,
    PRIMARY KEY (turno_id)
);

CREATE TABLE IF NOT EXISTS public.turno_trabajador
(
    trabajador_id integer NOT NULL,
    turno_id integer NOT NULL,
    PRIMARY KEY (trabajador_id, turno_id)
);

CREATE TABLE IF NOT EXISTS public.trabajador_invernadero
(
    invernadero_id integer NOT NULL,
    trabajador_id integer NOT NULL,
    PRIMARY KEY (invernadero_id, trabajador_id)
);

CREATE TABLE IF NOT EXISTS public.sensor_planta
(
    planta_id integer NOT NULL,
    sensor_id integer NOT NULL,
    PRIMARY KEY (planta_id, sensor_id)
);

CREATE TABLE IF NOT EXISTS public.sector_sensor
(
    sensor_id integer NOT NULL,
    sector_id integer NOT NULL,
    PRIMARY KEY (sensor_id, sector_id)
);

CREATE TABLE IF NOT EXISTS public.sector_invernadero
(
    invernadero_id integer NOT NULL,
    sector_id integer NOT NULL,
    PRIMARY KEY (invernadero_id, sector_id)
);

CREATE TABLE IF NOT EXISTS public.empresa
(
    empresa_id serial,
    nombre character varying(80),
    direccion character varying(120),
    correo character varying(50),
    web character varying(50),
    PRIMARY KEY (empresa_id)
);

CREATE TABLE IF NOT EXISTS public.invernadero_empresa
(
    empresa_id integer NOT NULL,
    invernadero_id integer NOT NULL,
    PRIMARY KEY (empresa_id, invernadero_id)
);

CREATE TABLE IF NOT EXISTS public.actuador_sector
(
    sector_id integer NOT NULL,
    actuador_id integer NOT NULL,
    PRIMARY KEY (sector_id, actuador_id)
);

ALTER TABLE IF EXISTS public.planta
    ADD CONSTRAINT planta_espercie FOREIGN KEY (especie_id)
    REFERENCES public.especie (especie_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.medicion_sensor
    ADD CONSTRAINT sensor_medicion FOREIGN KEY (sensor_id)
    REFERENCES public.sensor (sensor_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.tratamiento
    ADD CONSTRAINT planta_tratamiennto FOREIGN KEY (planta_id)
    REFERENCES public.planta (planta_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.tratamiento
    ADD CONSTRAINT tratamiento_tipo FOREIGN KEY (tipo_tratamiento_id)
    REFERENCES public.tipo_tratamiento (tipo_tratamiento_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.turno_trabajador
    ADD CONSTRAINT turno FOREIGN KEY (turno_id)
    REFERENCES public.turno (turno_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.turno_trabajador
    ADD CONSTRAINT trabajador FOREIGN KEY (trabajador_id)
    REFERENCES public.trabajador (trabajador_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.trabajador_invernadero
    ADD CONSTRAINT invernadero FOREIGN KEY (invernadero_id)
    REFERENCES public.invernadero (invernadero_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.trabajador_invernadero
    ADD CONSTRAINT trabajador FOREIGN KEY (trabajador_id)
    REFERENCES public.trabajador (trabajador_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.sensor_planta
    ADD CONSTRAINT sensor FOREIGN KEY (sensor_id)
    REFERENCES public.sensor (sensor_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.sensor_planta
    ADD CONSTRAINT planta FOREIGN KEY (planta_id)
    REFERENCES public.planta (planta_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.sector_sensor
    ADD CONSTRAINT sensor FOREIGN KEY (sensor_id)
    REFERENCES public.sensor (sensor_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.sector_sensor
    ADD CONSTRAINT sector FOREIGN KEY (sector_id)
    REFERENCES public.sector (sector_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.sector_invernadero
    ADD CONSTRAINT invernadero FOREIGN KEY (invernadero_id)
    REFERENCES public.invernadero (invernadero_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.sector_invernadero
    ADD CONSTRAINT sector FOREIGN KEY (sector_id)
    REFERENCES public.sector (sector_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.invernadero_empresa
    ADD CONSTRAINT invernadero FOREIGN KEY (invernadero_id)
    REFERENCES public.invernadero (invernadero_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.invernadero_empresa
    ADD CONSTRAINT empresa FOREIGN KEY (empresa_id)
    REFERENCES public.empresa (empresa_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.actuador_sector
    ADD CONSTRAINT sector FOREIGN KEY (sector_id)
    REFERENCES public.sector (sector_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.actuador_sector
    ADD CONSTRAINT actuador FOREIGN KEY (actuador_id)
    REFERENCES public.actuador (actuador_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;