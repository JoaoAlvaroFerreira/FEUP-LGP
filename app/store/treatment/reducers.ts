import {
    TreatmentsState,
    TreatmentActionTypes,
    INVALIDATE,
    START_FETCHING,
    RECEIVED,
} from "./types";

const initialState: TreatmentsState = {
    treatments: [],
    isFetching: false,
    page: 1,
    size: 10,
};

export function treatmentReducer(state: TreatmentsState = initialState, action: TreatmentActionTypes): TreatmentsState {
    switch (action.type) {
        case RECEIVED:
            return {
                ...state,
                treatments: (state.page === 1) ? action.treatments : [...state.treatments, ...action.treatments],
                isFetching: false,
                page: state.page + 1,
            };
        case INVALIDATE:
            return {
                ...state,
                page: 1,
            };
        case START_FETCHING:
            return {
                ...state,
                isFetching: true,
            };
        default:
            return state;
    }
}