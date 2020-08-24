import { Treatment, ReceivedTreatmentsAction, RECEIVED, InvalidateTreatmentsAction, INVALIDATE, StartFetchingAction, START_FETCHING, MuscleTest, Perimetry, Goniometry } from "./types";
import { GetTreatmentsResponse } from "../api/types";

export const receivedTreatments = (treatmentResponse: GetTreatmentsResponse): ReceivedTreatmentsAction => {
    const treatments = treatmentResponse.results.map(result => ({
        id: result.id,
        patientName: result.patient_name,
        summary: {
            description: result.summary,
            pain: result.pain_level,
        },
        otherAnnotations: {
            medication: result.medication,
            treatment: result.treatment,
            weeklyEvaluation: result.periodic_evaluation,
        },
        muscleTests: result.muscle_tests.map(test => ({
            id: test.body_zone.id,
            name: test.body_zone.name,
            pain: test.strength, //TODO: verify this with BE guys 
        } as MuscleTest)),
        perimetries: result.perimetries.map(perimetry => ({
            id: perimetry.body_zone.id,
            name: perimetry.body_zone.name,
            measure: perimetry.size,
        } as Perimetry)),
        goniometries: result.goniometries.map(goniometry => ({
            id: goniometry.body_zone.id,
            name: goniometry.body_zone.name,
            abductionRange: [goniometry.min_abduction, goniometry.max_abduction],
            adductionRange: [goniometry.min_adduction, goniometry.max_adduction],
            extentRange: [goniometry.min_extension, goniometry.max_extension],
            flexionRange: [goniometry.min_flexion, goniometry.max_flexion],
            rotationRange: [goniometry.min_rotation, goniometry.max_rotation],
        } as Goniometry)),
        startDate: new Date(result.start_date),
        endDate: new Date(result.end_date),
        isOpen: new Date(new Date(result.end_date).getDate() + 1) > new Date(),
    } as Treatment));
    return {
        type: RECEIVED,
        treatments,
    };
};

export const invalidateTreatments = (): InvalidateTreatmentsAction => (
    {
        type: INVALIDATE,
    }
);

export const startFetchingTreatments = (): StartFetchingAction => (
    {
        type: START_FETCHING,
    }
);
