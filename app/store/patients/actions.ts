import { InvalidatePatientsAction, INVALIDATE_PATIENTS, RequestPatientsAction, REQUEST_PATIENTS, Patient, ReceivePatientsAction, RECEIVE_PATIENTS, GET_MORE_PATIENTS } from "./types";
import { GetPatientsResponse } from "../api/types";

export const invalidatePatients = (): InvalidatePatientsAction => (
    {
        type: INVALIDATE_PATIENTS,
    }
);

export const startFetchingPatients = (): RequestPatientsAction => (
    {
        type: REQUEST_PATIENTS,
    }
);

export const receivedPatients = (patientResponse: GetPatientsResponse): ReceivePatientsAction => {
    const patients: Patient[] = patientResponse.results.map(result => ({
        id: result.id,
        firstName: result.person.first_name,
        lastName: result.person.last_name,
        numberOfSessions: result.number_completed_sessions[0],
        completedSession: result.number_completed_sessions[1],
        phone: result.person.telephone_number,
        email: result.person.email,
        address: {
            houseNumber: "11", // TODO: Change it
            street: result.person.address.street,
            city: result.person.address.city,
            zipCode: result.person.address.zip_code,
        },
        therapyHistoryURL: result.clinical_history,
        treatmentCycle: result.last_treatmentment_cycle,
    } as Patient));

    return {
        type: RECEIVE_PATIENTS,
        patients,
    };
};

export const getMorePatients = (patients: Patient[]): ReceivePatientsAction => (
    {
        type: GET_MORE_PATIENTS,
        patients,
    }
);