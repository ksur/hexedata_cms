-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.8.2
-- PostgreSQL version: 9.5
-- Project Site: pgmodeler.com.br
-- Model Author: ---


-- Database creation must be done outside an multicommand file.
-- These commands were put in this file only for convenience.
-- -- object: new_database | type: DATABASE --
-- -- DROP DATABASE IF EXISTS new_database;
-- CREATE DATABASE new_database
-- ;
-- -- ddl-end --
-- 

-- object: public.artykuly | type: TABLE --
-- DROP TABLE IF EXISTS public.artykuly CASCADE;
CREATE TABLE public.artykuly(
	id integer NOT NULL,
	kategoria_id integer NOT NULL,
	tytul varchar(255) NOT NULL,
	wersja_krotka text,
	wersja_dluga text,
	autor varchar(200),
	data timestamp,
	slot1 varchar(255),
	slot2 varchar(255),
	slot3 varchar(255),
	slot4 varchar(255),
	meta_title varchar(255),
	meta_keywords varchar(255),
	meta_description varchar(255),
	CONSTRAINT id PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON TABLE public.artykuly IS 'tabela z tekstami na strone';
-- ddl-end --
ALTER TABLE public.artykuly OWNER TO postgres;
-- ddl-end --

-- object: public.kategorie | type: TABLE --
-- DROP TABLE IF EXISTS public.kategorie CASCADE;
CREATE TABLE public.kategorie(
	id integer NOT NULL,
	nazwa varchar(250),
	opis text,
	slot1 varchar(255),
	CONSTRAINT id_1 PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.kategorie OWNER TO postgres;
-- ddl-end --

-- object: kategoria_id | type: CONSTRAINT --
-- ALTER TABLE public.artykuly DROP CONSTRAINT IF EXISTS kategoria_id CASCADE;
ALTER TABLE public.artykuly ADD CONSTRAINT kategoria_id FOREIGN KEY (kategoria_id)
REFERENCES public.kategorie (id) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --


