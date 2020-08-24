INSERT INTO public.address (id, street, zip_code, city) VALUES ('f2932eb5-10af-4eaa-8fcd-a65c24d9dd25', 'Rua de Cima', '3456-234', 'Porto');


INSERT INTO public.person (id, address_id, nif, first_name, last_name, birth_date, telephone_number, email, gender) VALUES ('0bf154c7-95fd-48cc-9b47-d4da5b552f91', 'f2932eb5-10af-4eaa-8fcd-a65c24d9dd25', '323243244', 'Zalberto', 'Silva', '1945-03-10', '223898988', 'alberto@gmail.com', 'm');
INSERT INTO public.person (id, address_id, nif, first_name, last_name, birth_date, telephone_number, email, gender) VALUES ('9e9ae8de-7e5d-483e-8bb4-a84cda4bfa2c', 'f2932eb5-10af-4eaa-8fcd-a65c24d9dd25', '123456789', 'John', 'Doe', '1992-03-13', '987654321', 'email@gmail.com', 'm');
INSERT INTO public.person (id, address_id, nif, first_name, last_name, birth_date, telephone_number, email, gender) VALUES ('2e9de8de-7e5d-683e-8bb4-a84c9a4bfa21', 'f2932eb5-10af-4eaa-8fcd-a65c24d9dd25', '1234533389', 'Namy', 'Doe', '1992-03-13', '907654321', 'a_mail@mail.com', 'f');
INSERT INTO public.person (id, address_id, nif, first_name, last_name, birth_date, telephone_number, email, gender) VALUES ('9e9defde-695d-683e-8bb4-a8666a4bfaa1', 'f2932eb5-10af-4eaa-8fcd-a65c24d9dd25', '9911533389', 'Amy', 'Doe', '1992-03-13', '117654321', 'dd_mail@mail.com', 'f');
INSERT INTO public.person (id, address_id, nif, first_name, last_name, birth_date, telephone_number, email, gender) VALUES ('9e9d28de-7b4e-183e-8bb4-a14ada4bac1f', 'f2932eb5-10af-4eaa-8fcd-a65c24d9dd25', '103450789', 'Joana', 'Due', '1972-03-13', '922533301', 'mymail@hotmail.com', 'f');
INSERT INTO public.person (id, address_id, nif, first_name, last_name, birth_date, telephone_number, email, gender) VALUES ('9e9d28de-7b4e-183e-8bb4-a14ada4bac1d', 'f2932eb5-10af-4eaa-8fcd-a65c24d9dd25', '103451789', 'João', 'Due', '1972-03-13', '922533301', 'admin@gmail.com', 'm');
INSERT INTO public.credential (id, password, email) VALUES ('be5faee9-76a6-40cb-8934-7e8a10c1e960', 'bcrypt_sha256$$2b$12$.3lRCw411HZsJkxZmLkpnuzTmdhs8HByKlrlSkHYX2ShyeZBHAnKW', 'email@gmail.com');
INSERT INTO public.credential (id, password, email) VALUES ('be5faee9-76a6-40cb-8934-7e8a10c1e961', 'bcrypt_sha256$$2b$12$.3lRCw411HZsJkxZmLkpnuzTmdhs8HByKlrlSkHYX2ShyeZBHAnKW', 'email2@email.com');
INSERT INTO public.credential (id, password, email) VALUES ('be5faee9-76a6-40cb-8934-7e8a10c1e962', 'bcrypt_sha256$$2b$12$.3lRCw411HZsJkxZmLkpnuzTmdhs8HByKlrlSkHYX2ShyeZBHAnKW', 'email3@email.com');
INSERT INTO public.credential (id, password, email) VALUES ('be5faee9-76a6-40cb-8934-7e8a10c1e963', 'bcrypt_sha256$$2b$12$.3lRCw411HZsJkxZmLkpnuzTmdhs8HByKlrlSkHYX2ShyeZBHAnKW', 'admin@gmail.com');
INSERT INTO public.state (id, name, description) VALUES ('ff286781-dd58-4b90-9582-95f62d06451c', 'active', 'This is an active state');
INSERT INTO public.state (id, name, description) VALUES ('a0daa51d-396c-4177-a7b1-b9cee382fb7c', 'inactive', 'This is an inactive state');
INSERT INTO public.state (id, name, description) VALUES ('1393de8e-eb0d-4d82-8b0b-b228b0aa7b12', 'blocked', 'This is a blocked state');


INSERT INTO public.patient (id, person_id, doctor_id, profession, diagnostic, clinical_history, state_id) VALUES ('79840898-b26f-441f-b8a3-a2642227c77d', '0bf154c7-95fd-48cc-9b47-d4da5b552f91', null, 'Reformado', 'This is a diagnostic', 'This is the clinical history', 'ff286781-dd58-4b90-9582-95f62d06451c');
INSERT INTO public.patient (id, person_id, doctor_id, profession, diagnostic, clinical_history, state_id) VALUES ('33840898-226f-241f-11a3-a2642117c771', '2e9de8de-7e5d-683e-8bb4-a84c9a4bfa21', null, 'Reformado', 'This is a diagnostic', 'This is the clinical history', 'ff286781-dd58-4b90-9582-95f62d06451c');
INSERT INTO public.patient (id, person_id, doctor_id, profession, diagnostic, clinical_history, state_id) VALUES ('a38497b8-226f-af1f-11a3-a2642117c771', '9e9defde-695d-683e-8bb4-a8666a4bfaa1', null, 'Reformado', 'This is a diagnostic', 'This is the clinical history', 'ff286781-dd58-4b90-9582-95f62d06451c');


INSERT INTO public.physiotherapist (id, person_id, professional_certificate, candidate_date, curriculum, credential_id, state_id) VALUES ('bbd29d3a-5977-4d0e-8c8e-987c329e6b7d', '9e9ae8de-7e5d-483e-8bb4-a84cda4bfa2c', 'gyuyg76g76g', '2020-03-13', 'curriculum.pdf', 'be5faee9-76a6-40cb-8934-7e8a10c1e960', 'ff286781-dd58-4b90-9582-95f62d06451c');
INSERT INTO public.physiotherapist (id, person_id, professional_certificate, candidate_date, curriculum, credential_id, state_id) VALUES ('acd1453a-5971-4d0e-1cfe-987c0c9e333d', '9e9d28de-7b4e-183e-8bb4-a14ada4bac1f', 'mklddd', '2020-03-13', 'curriculum.pdf', 'be5faee9-76a6-40cb-8934-7e8a10c1e961', 'ff286781-dd58-4b90-9582-95f62d06451c');
INSERT INTO public.patient_physiotherapist (id, patient_id, physiotherapist_id) VALUES ('4b96a1fe-67e8-4e2a-8bfa-4301f138e694', '79840898-b26f-441f-b8a3-a2642227c77d', 'bbd29d3a-5977-4d0e-8c8e-987c329e6b7d');
INSERT INTO public.patient_physiotherapist (id, patient_id, physiotherapist_id) VALUES ('9996a1fe-67e8-4e2a-8bfa-4301f138e694', '33840898-226f-241f-11a3-a2642117c771', 'bbd29d3a-5977-4d0e-8c8e-987c329e6b7d');
INSERT INTO public.patient_physiotherapist (id, patient_id, physiotherapist_id) VALUES ('9996a1fe-67e8-4e2a-8bfa-4301f138e695', 'a38497b8-226f-af1f-11a3-a2642117c771', 'acd1453a-5971-4d0e-1cfe-987c0c9e333d');

INSERT INTO public.administrator (id, person_id, credential_id, state_id) VALUES ('0929964c-6874-46c8-9022-cab271566f9d', '9e9d28de-7b4e-183e-8bb4-a14ada4bac1d', 'be5faee9-76a6-40cb-8934-7e8a10c1e963', 'ff286781-dd58-4b90-9582-95f62d06451c');

INSERT INTO public.body_zone (id, name) VALUES ('fcf1a46e-352a-468d-ada2-358464154b76', 'Ombro Esquerdo');
INSERT INTO public.body_zone (id, name) VALUES ('1b11c024-880a-4636-ba9b-978b1c38f1a2', 'Ombro Direito');
INSERT INTO public.body_zone (id, name) VALUES ('3c340418-74f9-4f6f-aec4-6c85c31e82a9', 'Cabeça');
INSERT INTO public.body_zone (id, name) VALUES ('62ff55d9-b4fc-43a4-bdbc-1ca5103cd83a', 'Braço Direito');
INSERT INTO public.body_zone (id, name) VALUES ('bde41122-1261-450b-a13a-8bd64d007b04', 'Braço Esquerdo');
INSERT INTO public.body_zone (id, name) VALUES ('f7915eda-9e2e-4a3c-a774-825496b9655e', 'Pescoço');
INSERT INTO public.body_zone (id, name) VALUES ('6eeb99de-c833-4630-b4af-11e7d7fa15af', 'Cotovelo Esquerdo');
INSERT INTO public.body_zone (id, name) VALUES ('f28c3265-cb79-47f7-a815-810a4b71d73f', 'Cotovelo Direito');
INSERT INTO public.body_zone (id, name) VALUES ('8cc7f0cb-435e-4bd6-b372-5f56dddcd582', 'Antebraço Direito');
INSERT INTO public.body_zone (id, name) VALUES ('11d532fd-b50b-404c-8fa0-305069410320', 'Antebraço Esquerdo');
INSERT INTO public.body_zone (id, name) VALUES ('c3e13a13-a9c0-41c9-8acf-63de22592a8e', 'Pulso Esquerdo');
INSERT INTO public.body_zone (id, name) VALUES ('79fc2f48-3970-4c67-b0de-4badaac38211', 'Pulso Direito');
INSERT INTO public.body_zone (id, name) VALUES ('f05277ef-7d08-4c1c-b0f4-17157cdefcb8', 'Mão Esquerda');
INSERT INTO public.body_zone (id, name) VALUES ('c737bf63-aa72-4772-917f-b5d43696fe90', 'Mão Direita');
INSERT INTO public.body_zone (id, name) VALUES ('d00100c0-1663-4443-b6b1-a234f43d5390', 'Tórax');
INSERT INTO public.body_zone (id, name) VALUES ('bb1fe6df-1fe0-4b82-9e11-1f08346601fc', 'Abdominal');
INSERT INTO public.body_zone (id, name) VALUES ('1776db1b-89c1-4b86-b5db-1300ec6c5089', 'Pélvis');
INSERT INTO public.body_zone (id, name) VALUES ('e264bb5b-c281-4845-82f5-57c5be0a3209', 'Coxa Esquerda');
INSERT INTO public.body_zone (id, name) VALUES ('9ac3c4b3-5b43-4c56-865c-7bccbd1c6857', 'Coxa Direita');
INSERT INTO public.body_zone (id, name) VALUES ('d33f4500-df89-455a-8970-01b4877156d8', 'Joelho Esquerdo');
INSERT INTO public.body_zone (id, name) VALUES ('547851b3-3277-4aad-8f59-64efc9614b91', 'Joelho Direito');
INSERT INTO public.body_zone (id, name) VALUES ('36705339-ead6-48c2-ad8f-7a0feb4545f7', 'Perna Esquerdo');
INSERT INTO public.body_zone (id, name) VALUES ('5713ccce-fbbb-4e60-ae3b-a06420d5057e', 'Perna Esquerdo');
INSERT INTO public.body_zone (id, name) VALUES ('35a16645-2393-43bf-a4ff-330a1ec26d9c', 'Tornozelo Esquerdo');
INSERT INTO public.body_zone (id, name) VALUES ('e3727983-37c5-49d5-b012-107a06d56cc1', 'Tornozelo Esquerdo');
INSERT INTO public.body_zone (id, name) VALUES ('fe13e6ce-d6e3-40b2-b033-a96f5302f2b6', 'Pé Esquerdo');
INSERT INTO public.body_zone (id, name) VALUES ('593cdb0d-ffa5-4453-9420-2d5f9655e7d6', 'Pé Esquerdo');

INSERT INTO public.treatment_cycle (id, patient_id, physiotherapist_id, number_of_sessions, completed_sessions) VALUES ('acf7bd28-3ea2-4491-9ad5-89a9ea8204bc', '79840898-b26f-441f-b8a3-a2642227c77d', 'bbd29d3a-5977-4d0e-8c8e-987c329e6b7d', 4, 0);
INSERT INTO public.treatment_cycle (id, patient_id, physiotherapist_id, number_of_sessions, completed_sessions) VALUES ('acf7bd28-3ea2-4491-9ad5-89a9ea8204bd', '79840898-b26f-441f-b8a3-a2642227c77d', 'bbd29d3a-5977-4d0e-8c8e-987c329e6b7d', 3, 0);
INSERT INTO public.treatment (id, treatment_cycle_id, start_date, end_date, summary, pain_level, medication, treatment, periodic_evaluation) VALUES ('98f0e26c-f59f-43a9-9500-594550b13174', 'acf7bd28-3ea2-4491-9ad5-89a9ea8204bc', '2020-03-21 18:47:15.000000', '2020-03-21 19:47:15.000000', 'This is a summary', 4, 'This is the medication', 'This is the treatment', 'This is the weekly evaluation');
INSERT INTO public.treatment (id, treatment_cycle_id, start_date, end_date, summary, pain_level, medication, treatment, periodic_evaluation) VALUES ('98f0e26c-f59f-43a9-9500-594550b13175', 'acf7bd28-3ea2-4491-9ad5-89a9ea8204bd', '2020-04-21 18:47:15.000000', '2020-04-21 19:47:15.000000', 'This is a summary', 4, 'This is the medication', 'This is the treatment', 'This is the weekly evaluation');
INSERT INTO public.treatment (id, treatment_cycle_id, start_date, end_date, summary, pain_level, medication, treatment, periodic_evaluation) VALUES ('98f0e26c-f59f-43a9-9500-594550b13176', 'acf7bd28-3ea2-4491-9ad5-89a9ea8204bc', '2020-05-21 18:47:15.000000', '2020-05-21 19:47:15.000000', 'This is a summary', 4, 'This is the medication', 'This is the treatment', 'This is the weekly evaluation');


INSERT INTO public.goniometry (id, min_abduction, max_abduction, min_adduction, max_adduction, min_flexion, max_flexion, min_rotation, max_rotation, min_extension, max_extension, treatment_id, body_zone_id) VALUES ('c6f72e94-7298-4b8d-a6af-ac618c08dd1a', 55, 78, 125, 140, 124, 180, 135, 176, 23, 45, '98f0e26c-f59f-43a9-9500-594550b13174', 'fcf1a46e-352a-468d-ada2-358464154b76');
INSERT INTO public.goniometry (id, min_abduction, max_abduction, min_adduction, max_adduction, min_flexion, max_flexion, min_rotation, max_rotation, min_extension, max_extension, treatment_id, body_zone_id) VALUES ('743a8b0c-8abf-42a2-86cf-1461e88b1792', 35, 98, 35, 170, 80, 180, 35, 66, 43, 79, '98f0e26c-f59f-43a9-9500-594550b13174', 'fcf1a46e-352a-468d-ada2-358464154b76');


INSERT INTO public.perimetry (id, size, treatment_id, body_zone_id) VALUES ('470b3586-86c1-4f3d-94be-a475bccf125b', 100, '98f0e26c-f59f-43a9-9500-594550b13174', 'fcf1a46e-352a-468d-ada2-358464154b76');
INSERT INTO public.perimetry (id, size, treatment_id, body_zone_id) VALUES ('470b3586-86c1-4f3d-94be-a475bccf125c', 100, '98f0e26c-f59f-43a9-9500-594550b13175', '593cdb0d-ffa5-4453-9420-2d5f9655e7d6');
INSERT INTO public.perimetry (id, size, treatment_id, body_zone_id) VALUES ('d6d4a999-3244-43c8-8056-350ed5528283', 45, '98f0e26c-f59f-43a9-9500-594550b13174', 'fcf1a46e-352a-468d-ada2-358464154b76');


INSERT INTO public.muscle_test (id, strength, body_zone_id, treatment_id) VALUES ('adebe2f4-c2d1-4d73-bb04-cd7ac30437a5', 5, 'fcf1a46e-352a-468d-ada2-358464154b76', '98f0e26c-f59f-43a9-9500-594550b13174');
INSERT INTO public.muscle_test (id, strength, body_zone_id, treatment_id) VALUES ('ea365f11-6174-41fe-8108-62a4422d6070', 3, 'fcf1a46e-352a-468d-ada2-358464154b76', '98f0e26c-f59f-43a9-9500-594550b13174');
