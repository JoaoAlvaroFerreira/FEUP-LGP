import { User, UserActionTypes, LOG_IN, LOG_OUT } from "./types";

const initialState: User = {
    firstName: "",
    lastName: "",
    email: "",
    id: "",
    isLogged: false,
    isAdmin: false,
};

export const userReducer = (state: User = initialState, action: UserActionTypes): User => {
    switch (action.type) {
        case LOG_IN:
            return {
                ...state,
                isLogged: true,
                firstName: action.firstName,
                lastName: action.lastName,
                email: action.email,
                id: action.id,
                isAdmin: action.isAdmin,
            };
        case LOG_OUT:
            return initialState;
        default:
            return state;
    }
};