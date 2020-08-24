// Entities
export type User = {
    firstName: string;
    lastName: string;
    email: string;
    id: string;
    isLogged: boolean;
    isAdmin: boolean;
};

// Actions types
export type LogInAction = {
    type: typeof LOG_IN;
    firstName: string;
    lastName: string;
    email: string;
    id: string;
    isAdmin: boolean;
};

export type LogOutAction = {
    type: typeof LOG_OUT;
};

export type UserActionTypes = LogInAction | LogOutAction;

// Actions constants
export const LOG_IN = "store/user/types/LOG_IN";
export const LOG_OUT = "store/user/types/LOG_OUT";
