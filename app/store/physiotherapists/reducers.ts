import { PhysiotherapistsState, PhysiotherapistsActionTypes, INVALIDATE_PHYSIOTHERAPISTS, RECEIVE_PHYSIOTHERAPISTS, REQUEST_PHYSIOTHERAPISTS, GET_MORE_PHYSIOTHERAPISTS } from "./types";

const initialState: PhysiotherapistsState = {
    Physiotherapists: [],
    isFetching: false,
    isValid: true,
    page: 1,
    size: 10,
};

export const PhysiotherapistsReducer = (state: PhysiotherapistsState = initialState, action: PhysiotherapistsActionTypes): PhysiotherapistsState => {
    switch (action.type) {
        case INVALIDATE_PHYSIOTHERAPISTS:
            return {
                ...state,
                isValid: true,
            };
        case RECEIVE_PHYSIOTHERAPISTS:
            return {
                ...state,
                Physiotherapists: action.Physiotherapists.sort((a, b) => {
                    if (a.name > b.name)
                        return 1;
                    else if (b.name > a.name)
                        return -1;
                    else return 0;

                }),
                isFetching: false,
                isValid: true,
                page: state.page + 1,
            };
        case REQUEST_PHYSIOTHERAPISTS:
            return {
                ...state,
                isFetching: true,
                page: 1,
            };
        case GET_MORE_PHYSIOTHERAPISTS:
            return {
                ...state,
                Physiotherapists: [...state.Physiotherapists, ...action.Physiotherapists.sort((a, b) => {
                    if (a.name > b.name)
                        return 1;
                    else if (b.name > a.name)
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