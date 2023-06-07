-- Database: fake_gaspar

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

-- DROP DATABASE IF EXISTS fake_gaspar;

-- CREATE DATABASE fake_gaspar
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'en_US.utf8'
--     LC_CTYPE = 'en_US.utf8'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- SCHEMA: public

-- DROP SCHEMA IF EXISTS public ;

ALTER TABLE IF EXISTS public.tb_default_reponses OWNER TO postgres;


CREATE TABLE IF NOT EXISTS public.tb_default_reponses
(
    default_reponses_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    default_reponses_route character varying(2083) COLLATE pg_catalog."default" NOT NULL,
    default_reponses_tag character varying(100) COLLATE pg_catalog."default" NOT NULL,
    default_reponses_content text COLLATE pg_catalog."default" NOT NULL,
    default_reponses_is_active boolean NOT NULL,
    CONSTRAINT tb_default_reponses_pkey PRIMARY KEY (default_reponses_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;


-- Table: public.tb_default_reponses

-- DROP TABLE IF EXISTS public.tb_default_reponses;

-- GRANT ALL ON SCHEMA public TO PUBLIC;

-- GRANT ALL ON SCHEMA public TO postgres;

ALTER TABLE IF EXISTS public.tb_default_reponses
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.tb_requests_recived
(
    requests_recived_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    requests_recived_route character varying(2083) COLLATE pg_catalog."default" NOT NULL,
    requests_recived_content text COLLATE pg_catalog."default" NOT NULL,
    requests_recived_timestamp timestamp without time zone NOT NULL,
    CONSTRAINT tb_requests_recived_pkey PRIMARY KEY (requests_recived_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

-- Table: public.tb_requests_recived

