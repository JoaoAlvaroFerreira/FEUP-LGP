import { Action } from 'redux';
import { ThunkAction } from 'redux-thunk';
import { AsyncStorage } from 'react-native';
import { GetPatientsResponse, LoginResponse, GetBodyPartsResponse, GetTreatmentsResponse } from './types';
import physioBE, { TOKEN } from './axiosConfig';
import { User } from '../user/types';
import { logIn, logOut } from '../user/actions';
import { TreatmentsState } from '../treatment/types';
import { mockPostPatientData } from './mockups';
import { invalidateTreatments, startFetchingTreatments, receivedTreatments } from '../treatment/actions';
import { startFetchingBodyParts, receivedBodyParts } from '../body_parts/actions';
import { AppState } from '..';
import { invalidatePatients, startFetchingPatients, receivedPatients } from '../patients/actions';

export const fetchFreshPatients = (): ThunkAction<void, AppState, unknown, Action<string>> => async dispatch => {
    dispatch(invalidatePatients());
    dispatch(fetchPatients());
};

export const fetchPatients = (): ThunkAction<void, AppState, unknown, Action<string>> => async (dispatch, getState) => {
    dispatch(startFetchingPatients());
    physioBE({
        method: 'GET',
        url: 'patients',
        params: {
            page_num: getState().patientsStore.page,
            page_size: getState().patientsStore.size,
        },
    })
        .then(response => response.data)
        .then((data: GetPatientsResponse) => {
            dispatch(receivedPatients(data));
        });
};

export const fetchFreshTreatments = (): ThunkAction<void, AppState, unknown, Action<string>> => async dispatch => {
    dispatch(invalidateTreatments());
    dispatch(fetchTreatments());
};

export const fetchTreatments = (): ThunkAction<void, AppState, unknown, Action<string>> => async (dispatch, getState) => {
    dispatch(startFetchingTreatments());
    physioBE({
        method: 'GET',
        url: 'treatments',
        params: {
            page_num: getState().treatmentStore.page,
            page_size: getState().treatmentStore.size,
        },
    })
        .then(response => response.data)
        .then((data: GetTreatmentsResponse) => {
            dispatch(receivedTreatments(data));
        });
};

export const createPatient = (): ThunkAction<void, AppState, unknown, Action<string>> => async dispatch => {
    physioBE({
        method: "POST",
        url: 'patients',
        data: mockPostPatientData(),
    });
};

export const postLogIn = (email: string, password: string): ThunkAction<void, User, unknown, Action<string>> => async dispatch => {
    physioBE({
        method: "POST",
        url: "auth/login",
        data: {
            email: email,
            password: password,
        }
    })
        .then(response => response.data)
        .then((data: LoginResponse) => {
            dispatch(logIn(data));
        });
};

export const postLogOut = (): ThunkAction<void, User, unknown, Action<string>> => async dispatch => {
    await AsyncStorage.removeItem(TOKEN);
    dispatch(logOut());
};

export const fetchBodyParts = (): ThunkAction<void, TreatmentsState, unknown, Action<string>> => async (dispatch) => {
    dispatch(startFetchingBodyParts());

    physioBE({
        method: "GET",
        url: "body-zones",
        params: {
            page_num: 1,
            page_size: 200,
        }
    }).then(response => response.data)
        .then((data: GetBodyPartsResponse) => {
            dispatch(receivedBodyParts(data.results));
        });
};