import { PatientsState, PatientsActionTypes, INVALIDATE_PATIENTS, RECEIVE_PATIENTS, REQUEST_PATIENTS, GET_MORE_PATIENTS } from "./types";

const initialState: PatientsState = {
    patients: [],
    isFetching: false,
    isValid: true,
    page: 1,
    size: 10,
};

export const patientsReducer = (state: PatientsState = initialState, action: PatientsActionTypes): PatientsState => {
    switch (action.type) {
        case INVALIDATE_PATIENTS:
            return {
                ...state,
                isValid: true,
            };
        case RECEIVE_PATIENTS:
            return {
                ...state,
                patients: action.patients.sort((a, b) => {
                    if (a.firstName > b.firstName)
                        return 1;
                    else if (b.firstName > a.firstName)
                        return -1;
                    else return 0;

                }),
                isFetching: false,
                isValid: true,
                page: state.page + 1,
            };
        case REQUEST_PATIENTS:
            return {
                ...state,
                isFetching: true,
                page: 1,
            };
        case GET_MORE_PATIENTS:
            return {
                ...state,
                patients: [...state.patients, ...action.patients.sort((a, b) => {
                    if (a.firstName > b.firstName)
                        return 1;
                    else if (b.firstName > a.firstName)
                        return -1;
                    else return 0;

                })],
                isFetching: false,
                isValid: true,
                page: state.page + 1,
            };
        default:
            return state;
    }
};