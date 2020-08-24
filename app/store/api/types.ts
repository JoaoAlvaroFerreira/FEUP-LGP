import { BodyPart } from "../body_parts/types";

export type TokenStore = {
    access: Token;
    refresh: Token;
};

export type Token = {
    token: string;
    expiredTime: Date;
};

export type LoginResponse = {
    first_name: string;
    last_name: string;
    is_admin: boolean;
    email: string;
    id: string;
} & TokenStore;

// TODO: This should be rewrited by normalizr library
export type GetPatientsResponse = {
    total_pages: number,
    total_results: number,
    results: {
        id: string,
        name: string,
        person: {
            id: string,
            address: {
                id: string,
                street: string,
                zip_code: string,
                city: string,
            },
            nif: string,
            first_name: string,
            last_name: string,
            birth_date: string,
            telephone_number: string,
            email: string,
            gender: string,
        },
        state: string,
        last_treatmentment_cycle: string,
        number_completed_sessions: number[],
        diagnostic: string,
        clinical_history: string,
    }[],
};


export type PostCreatePatientData = {
    nif: string,
    first_name: string,
    last_name: string,
    birth_date: string, // TODO: add format validation "YYYY-MM-DD"
    telephone_number: string,
    email: string, // TODO: add email validation
    gender: string,
    profession: string;
    diagnostic: string;
    clinical_history: string;
    address: {
        street: string;
        city: string;
        zip_code: string;
    }
};

export type GetBodyPartsResponse = {
    results: BodyPart[],
};

export type GetTreatmentsResponse = {
    total_pages: number,
    total_results: number,
    results: {
        id: string,
        patient_name: string,
        perimetries: {
            id: string,
            body_zone: BodyPart,
            size: number,
            treatment: string,
        }[],
        goniometries: {
            id: string,
            body_zone: BodyPart,
            min_abduction: number,
            max_abduction: number,
            min_adduction: number,
            max_adduction: number,
            min_flexion: number,
            max_flexion: number,
            min_rotation: number,
            max_rotation: number,
            min_extension: number,
            max_extension: number,
            treatment: string,
        }[],
        muscle_tests: {
            id: string,
            body_zone: BodyPart,
            strength: number,
            treatment: string,
        }[],
        start_date: string,
        end_date: string,
        summary: string,
        pain_level: number,
        medication: string,
        treatment: string,
        periodic_evaluation: string,
        treatment_cycle: string,
    }[],
};

///PHYSIOTHERAPIST


export type GetPhysiotherapistsResponse = {
    total_pages: number,
    total_results: number,
    results: {
        id: string,
        name: string,
        person: {
            id: string,
            address: {
                id: string,
                street: string,
                zip_code: string,
                city: string,
            },
            nif: string,
            first_name: string,
            last_name: string,
            birth_date: string,
            telephone_number: string,
            email: string,
            gender: string,
        },
        professional_certificate: string,
        state: string,
    }[],
};

export type PostCreatePhysiotherapistData = {
    nif: string,
    first_name: string,
    last_name: string,
    birth_date: string, // TODO: add format validation "YYYY-MM-DD"
    telephone_number: string,
    email: string, // TODO: add email validation
    gender: string,
    professional_certificate: string,
    clinical_history: string;
    address: {
        street: string;
        city: string;
        zip_code: string;
    }
};