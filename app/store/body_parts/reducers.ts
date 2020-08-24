import { BodyPartsState, BodyPartsAction, START_FETCHING, RECEIVED, FILTER } from "./types";

const initialState: BodyPartsState = {
    bodyParts: [],
    filteredBodyParts: [],
    isFetching: false,
};

export const bodyPartsReducer = (state: BodyPartsState = initialState, action: BodyPartsAction): BodyPartsState => {
    switch (action.type) {
        case START_FETCHING:
            return {
                ...state,
                isFetching: true,
            };
        case RECEIVED:
            return {
                ...state,
                bodyParts: action.bodyParts,
                filteredBodyParts: action.bodyParts,
            };
        case FILTER:
            return {
                ...state,
                filteredBodyParts: state.bodyParts.filter(bodyPart => bodyPart.name.includes(action.query)),
            };
        default:
            return state;
    }
};