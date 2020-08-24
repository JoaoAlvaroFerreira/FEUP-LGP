import { BodyPart } from "../body_parts/types";

// Entities
export type Treatment = {
    id?: string;
    summary: Summary;
    otherAnnotations: OtherAnnotations;
    muscleTests: MuscleTest[];
    perimetries: Perimetry[];
    goniometries: Goniometry[];
    startDate: Date;
    endDate: Date;
    isOpen: boolean;
    checkBoxes: boolean[];
    patientName: string;
};

export type Summary = {
    description: string;
    pain: number;
};

export type MuscleTest = {
    pain: number;
} & BodyPart;

export type Perimetry = {
    measure: number;
} & BodyPart;

export type Goniometry = {
    abductionRange: number[];
    adductionRange: number[];
    extentRange: number[];
    flexionRange: number[];
    rotationRange: number[];
} & BodyPart;

export type OtherAnnotations = {
    treatment: string
    medication: string
    weeklyEvaluation: string
};

export type TreatmentsState = {
    treatments: Treatment[];
    isFetching: boolean;
    page: number;
    size: number;
};

// Actions types
export type ReceivedTreatmentsAction = {
    type: typeof RECEIVED;
    treatments: Treatment[];
};

export type InvalidateTreatmentsAction = {
    type: typeof INVALIDATE;
};

export type StartFetchingAction = {
    type: typeof START_FETCHING;
};

export type TreatmentActionTypes = ReceivedTreatmentsAction | InvalidateTreatmentsAction | StartFetchingAction;

// Actions constants
export const RECEIVED = "store/treatment/types/RECEIVED";
export const INVALIDATE = "store/treatment/types/INVALIDATE";
export const START_FETCHING = "store/treatment/types/START_FETCHING";