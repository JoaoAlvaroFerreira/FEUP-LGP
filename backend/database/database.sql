create table address
(
    id       uuid         not null
        constraint address_pk
            primary key,
    zip_code varchar(16)  not null,
    street   varchar(255) not null,
    city     varchar(127) not null
);

alter table address
    owner to postgres;

create unique index address_id_uindex
    on address (id);

create table body_zone
(
    id   uuid         not null
        constraint body_zone_pk
            primary key,
    name varchar(255) not null
);

alter table body_zone
    owner to postgres;

create unique index body_zone_id_uindex
    on body_zone (id);

create table credential
(
    id       uuid        not null
        constraint credential_pk
            primary key,
    password varchar(128) not null,
    email            varchar(127) not null
        constraint credential_email_uk
            unique
        constraint credential_email_check
            check ((email)::text ~ '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'::text)
);

alter table credential
    owner to postgres;

create unique index credential_id_uindex
    on credential (id);

create table person
(
    id               uuid         not null
        constraint person_pk
            primary key,
    address_id       uuid         not null
        constraint person_address_fk
            references address
            on update cascade on delete set null,
    nif              varchar(32)  not null
        constraint person_nif_uk
            unique,
    first_name       varchar(255) not null,
    last_name        varchar(255) not null,
    birth_date       date         not null,
    telephone_number varchar(16)  not null,
    email            varchar(127) not null
        constraint person_email_uk
            unique
        constraint person_email_check
            check ((email)::text ~ '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'::text),
    gender           char         not null constraint gender_check
            check (((gender)::char = 'm'::text) OR ((gender)::char = 'f'::text))
);

alter table person
    owner to postgres;

create unique index person_id_uindex
    on person (id);

create unique index person_nif_uindex
    on person (nif);

create table candidate
(
    id                       uuid         not null
        constraint candidate_pk
            primary key,
    person_id                uuid         not null
        constraint candidate_person_id_fk
            references person
            on update cascade on delete cascade,
    professional_certificate varchar(11)  not null
        constraint candidate_professional_certificate_uk
            unique,
    curriculum               varchar(255) not null,
    observations             text
);

alter table candidate
    owner to postgres;

create unique index candidate_id_uindex
    on candidate (id);

create table state
(
    id          uuid         not null
        constraint state_pk
            primary key,
    name        varchar(127) not null,
    description text
);

alter table state
    owner to postgres;

create unique index state_id_uindex
    on state (id);

create table administrator
(
    id            uuid not null
        constraint administrator_pk
            primary key,
    person_id     uuid not null
        constraint administrator_person_id_fk
            references person
            on update cascade on delete cascade,
    credential_id uuid not null
        constraint administrator_credential_id_fk
            references credential
            on update cascade on delete restrict,
    state_id      uuid
        constraint administrator_state_id_fk
            references state
            on update cascade on delete set null
);

alter table administrator
    owner to postgres;

create unique index administrator_credential_id_uindex
    on administrator (credential_id);

create unique index administrator_id_uindex
    on administrator (id);

create table doctor
(
    id                       uuid         not null
        constraint doctor_pk
            primary key,
    name                     varchar(255) not null,
    professional_certificate varchar(16)  not null
        constraint doctor_professional_certificate_uk
            unique,
    email                    varchar(127) not null
        constraint doctor_email_uk
            unique,
    state_id                 uuid
        constraint doctor_state_id_fk
            references state
            on update cascade on delete set null
);

alter table doctor
    owner to postgres;

create unique index doctor_doctor_uindex
    on doctor (id);

create table entity
(
    id       uuid         not null
        constraint entity_pk
            primary key,
    name     varchar(255) not null,
    state_id uuid
        constraint entity_state_id_fk
            references state
            on update cascade on delete set null
);

alter table entity
    owner to postgres;

create unique index entity_id_uindex
    on entity (id);

create table patient
(
    id               uuid         not null
        constraint patient_pk
            primary key,
    person_id        uuid         not null
        constraint patient_person_id_fk
            references person
            on update cascade on delete cascade,
    doctor_id        uuid
        constraint patient_doctor_id_fk
            references doctor
            on update cascade on delete set null,
    profession       varchar(127) not null,
    diagnostic       text         not null,
    clinical_history text         not null,
    state_id         uuid
        constraint patient_state_id_fk
            references state
            on update cascade on delete set null
);

alter table patient
    owner to postgres;

create index fki_patient_doctor_id_fk
    on patient (doctor_id);

create unique index patient_id_uindex
    on patient (id);

create table contact
(
    id               uuid         not null
        constraint contact_pk
            primary key,
    patient_id       uuid         not null
        constraint contact_patient_id_fk
            references patient
            on update cascade on delete restrict,
    cellphone_number varchar(16)  not null,
    first_name       varchar(127) not null,
    last_name        varchar(127) not null,
    patient_relation varchar(127) not null
);

alter table contact
    owner to postgres;

create unique index contact_id_uindex
    on contact (id);

create table patient_entity
(
    id             uuid        not null
        constraint patient_entity_pk
            primary key,
    patient_id     uuid        not null
        constraint patient_entity_patient_id_fk
            references patient
            on update cascade on delete cascade,
    entity_id      uuid
        constraint patient_entity_entity_id_fk
            references entity
            on update cascade on delete set null,
    process_number varchar(20) not null
        constraint patient_entity_process_number_uk
            unique
);

alter table patient_entity
    owner to postgres;

create unique index patient_entity_id_uindex
    on patient_entity (id);

create table physiotherapist
(
    id                       uuid         not null
        constraint physiotherapist_pk
            primary key,
    person_id                uuid
        constraint physiotherapist_person_id_fk
            references person
            on update cascade on delete set null,
    professional_certificate varchar(11)  not null
        constraint physiotherapist_professional_certificate_uk
            unique,
    candidate_date           date         not null,
    curriculum               varchar(255) not null,
    credential_id            uuid         not null
        constraint physiotherapist_credential_id_fk
            references credential
            on update cascade on delete restrict,
    state_id                 uuid
        constraint physiotherapist_state_id_fk
            references state
            on update cascade on delete set null
);

alter table physiotherapist
    owner to postgres;

create unique index physiotherapist_id_uindex
    on physiotherapist (id);

create table patient_physiotherapist
(
    id                 uuid not null
        constraint patient_physiotherapist_pk
            primary key,
    patient_id         uuid not null
        constraint patient_physiotherapist_patient_id_fk
            references patient
            on update cascade on delete set null,
    physiotherapist_id uuid not null
        constraint patient_physiotherapist_physiotherapist_id_fk
            references physiotherapist
            on update cascade on delete set null
);

alter table patient_physiotherapist
    owner to postgres;

create index fki_patient_physiotherapist_patient_id_fk
    on patient_physiotherapist (patient_id);

create index fki_patient_physiotherapist_physiotherapist_id_fk
    on patient_physiotherapist (physiotherapist_id);

create table treatment_cycle
(
    id                 uuid              not null
        constraint treatment_cycle_pk
            primary key,
    patient_id         uuid              not null
        constraint treatment_cycle_patient_id_fk
            references patient
            on update cascade on delete cascade,
    physiotherapist_id uuid
        constraint treatment_cycle_physiotherapist_id_fk
            references physiotherapist
            on update cascade on delete set null,
    number_of_sessions integer           not null,
    completed_sessions integer default 0 not null,
    constraint treatment_cycle_sessions_check
        check (completed_sessions <= number_of_sessions)
);

alter table treatment_cycle
    owner to postgres;

create unique index treatment_cycle_id_uindex
    on treatment_cycle (id);

create table treatment
(
    id                 uuid      not null
        constraint treatment_pk
            primary key,
    treatment_cycle_id uuid      not null
        constraint treatment_treatment_cycle_id_fk
            references treatment_cycle
            on update cascade on delete cascade,
    start_date         timestamp not null,
    end_date           timestamp,
    summary            text not null,
    pain_level         integer
        constraint pain_level_check
            check ((pain_level >= 0) AND (pain_level <= 10)),
    medication         text,
    treatment          text,
    periodic_evaluation  text,
    constraint treatment_date_check
        check (end_date > start_date)
);

alter table treatment
    owner to postgres;

create unique index treatment_id_uindex
    on treatment (id);

create table goniometry
(
    id            uuid         not null
        constraint goniometry_pk
            primary key,
    min_abduction integer      not null,
    max_abduction integer      not null,
    min_adduction integer      not null,
    max_adduction integer      not null,
    min_flexion   integer      not null,
    max_flexion   integer      not null,
    min_rotation  integer      not null,
    max_rotation  integer      not null,
    min_extension integer      not null,
    max_extension integer      not null,
    treatment_id  uuid         not null
        constraint goniometry_treatment_id_fk
            references treatment
            on update cascade on delete cascade,
    body_zone_id  uuid         not null
        constraint goniometry_body_zone_id_fk
            references body_zone
            on update cascade on delete restrict,
    constraint goniometry_abduction_check
        check ((min_abduction >= 0) AND (min_abduction <= 180) AND (max_abduction >= 0) AND (max_abduction <= 180) AND
               (max_abduction > min_abduction)),
    constraint goniometry_adduction_check
        check ((min_adduction >= 0) AND (min_adduction <= 180) AND (max_adduction >= 0) AND (max_adduction <= 180) AND
               (max_adduction > min_adduction)),
    constraint goniometry_extension_check
        check ((min_extension >= 0) AND (min_extension <= 180) AND (max_extension >= 0) AND (max_extension <= 180) AND
               (max_extension > min_extension)),
    constraint goniometry_flexion_check
        check ((min_flexion >= 0) AND (min_flexion <= 180) AND (max_flexion >= 0) AND (max_flexion <= 180) AND
               (max_flexion > min_flexion)),
    constraint goniometry_rotation_check
        check ((min_rotation >= 0) AND (min_rotation <= 180) AND (max_rotation >= 0) AND (max_rotation <= 180) AND
               (max_rotation > min_rotation))
);

alter table goniometry
    owner to postgres;

create unique index table_name_id_uindex
    on goniometry (id);

create table muscle_test
(
    id           uuid         not null
        constraint muscle_test_pk
            primary key,
    strength     integer      not null
        constraint muscle_test_strength_check
            check ((strength >= 1) AND (strength <= 5)),
    body_zone_id uuid         not null
        constraint muscle_test_body_zone_id_fk
            references body_zone
            on update cascade on delete restrict,
    treatment_id uuid         not null
        constraint muscle_test_treatment_id_fk
            references treatment
            on update cascade on delete cascade
);

alter table muscle_test
    owner to postgres;

create unique index muscle_test_id_uindex
    on muscle_test (id);

create table perimetry
(
    id           uuid         not null
        constraint perimetry_pk
            primary key,
    size         integer      not null
        constraint perimetry_size_check
            check ((size >= 0) AND (size <= 200)),
    treatment_id uuid         not null
        constraint perimetry_treatment_id_fk
            references treatment
            on update cascade on delete cascade,
    body_zone_id uuid         not null
        constraint perimetry_body_zone_id_fk
            references body_zone
            on update cascade on delete restrict
);

alter table perimetry
    owner to postgres;

create unique index perimetry_id_uindex
    on perimetry (id);

create function limit_contacts_function() returns trigger
    language plpgsql
as
$$
BEGIN
    IF (
           SELECT count(*)
           FROM contact,
                (
                    SELECT id AS pid
                    FROM patient
                    WHERE id = NEW.patient_id
                ) as pp
           WHERE contact.patient_id = pp.pid
       ) = 2 THEN
        RAISE EXCEPTION 'Cant have more than 2 contacts';
    end if;
    return NEW;
END
$$;

alter function limit_contacts_function() owner to postgres;

create trigger limit_contacts
    before insert
    on contact
    for each row
execute procedure limit_contacts_function();

create function increment_sessions_function() returns trigger
    language plpgsql
as
$$
BEGIN
    UPDATE treatment_cycle
    SET completed_sessions = completed_sessions + 1
    WHERE (NEW.treatment_cycle_id = id);
    RETURN NEW;
END;
$$;

alter function increment_sessions_function() owner to postgres;

create trigger increment_sessions
    before insert
    on treatment
    for each row
execute procedure increment_sessions_function();


-- GIN -> Faster to search, slower to update and more storage needed compared to GIST
-- GIN for small fields

-- GIST -> Slower to seacrh, faster updates and lower storage needed compared to GIN
-- GIST for fields that use more memory

CREATE INDEX person_first_name_idx ON person USING GIN (to_tsvector('portuguese', "first_name"));
CREATE INDEX person_last_name_idx ON person USING GIN (to_tsvector('portuguese',"last_name"));
CREATE INDEX person_telephone_number_idx ON person USING GIN (to_tsvector('portuguese',"telephone_number"));
CREATE INDEX person_email_idx ON person USING GIN (to_tsvector('portuguese',"email"));

CREATE INDEX patient_profession_idx ON patient USING GIN (to_tsvector('portuguese',"profession"));
CREATE INDEX patient_diagnostic_idx ON patient USING GIST (to_tsvector('portuguese', "diagnostic"));
CREATE INDEX patient_clinical_history_idx ON patient USING GIST (to_tsvector('portuguese',"clinical_history"));

CREATE INDEX doctor_name_idx ON doctor USING GIN (to_tsvector('portuguese',"name"));

CREATE EXTENSION pg_trgm;
