// Entities
export type Patient = {
    id: string;
    firstName: string;
    lastName: string;
    numberOfSessions: number;
    completedSession: number;
    phone: string;
    email: string;
    address: Address;
    therapyHistoryURL: string;
    treatmentCycle: string;
};

export type Address = {
    city: string;
    street: string;
    houseNumber: string;
    zipCode: string;
};

export type PatientsState = {
    patients: Patient[];
    isFetching: boolean;
    isValid: boolean;
} & Pagination;

export type Pagination = {
    page: number;
    size: number;
};

// Actions types
export type InvalidatePatientsAction = {
    type: typeof INVALIDATE_PATIENTS;
};

export type RequestPatientsAction = {
    type: typeof REQUEST_PATIENTS;
};

export type ReceivePatientsAction = {
    type: typeof RECEIVE_PATIENTS | typeof GET_MORE_PATIENTS;
    patients: Patient[];
};

export type PatientsActionTypes = InvalidatePatientsAction | RequestPatientsAction | ReceivePatientsAction;

// Actions constants
export const INVALIDATE_PATIENTS = '/store/patients/action/INVALIDATE_PATIENTS';
export const REQUEST_PATIENTS = '/store/patients/action/REQUEST_PATIENTS';
export const RECEIVE_PATIENTS = '/store/patients/action/RECEIVE_PATIENTS';
export const GET_MORE_PATIENTS = '/store/patients/action/GET_MORE_PATIENTS';
