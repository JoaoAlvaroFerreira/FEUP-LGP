import { LogInAction, LOG_IN, LogOutAction, LOG_OUT } from "./types";
import { LoginResponse } from "../api/types";

export const logIn = (loginResponse: LoginResponse): LogInAction => (
    {
        type: LOG_IN,
        firstName: loginResponse.first_name,
        lastName: loginResponse.last_name,
        email: loginResponse.email,
        id: loginResponse.id,
        isAdmin: loginResponse.is_admin,
    }
);

export const logOut = (): LogOutAction => (
    {
        type: LOG_OUT,
    }
);
