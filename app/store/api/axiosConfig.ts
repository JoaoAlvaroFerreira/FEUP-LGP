import axios from "axios";
import { AsyncStorage } from 'react-native';
import { TokenStore, LoginResponse } from './types';

export const TOKEN = "TOKEN";

const physioBE = axios.create({
    baseURL: "http://ec2-34-197-76-240.compute-1.amazonaws.com:8000/",
    //headers
});

physioBE.interceptors.request.use(async config => {
    const tokens = await AsyncStorage.getItem(TOKEN);
    if (tokens !== null) {
        const tokenStore: TokenStore = JSON.parse(tokens);
        config.headers['authorization'] = `Bearer ${tokenStore.access.token}`;
    }

    return config;
});

physioBE.interceptors.response.use(response => {
    if (response.config.url?.includes('auth/login') || response.config.url?.includes('auth/refresh')) {
        const data: LoginResponse = response.data;
        const data1: TokenStore = {
            access: data.access,
            refresh: data.refresh,
        };
        AsyncStorage.setItem(TOKEN, JSON.stringify(data1));
    }

    return response;
}, async (error) => {
    const origConfig = error.config;
    if (error.response.status === 401 && !origConfig.retry) {
        origConfig.retry = true;
        const tokens = await AsyncStorage.getItem(TOKEN);
        const tokenStore: TokenStore = tokens !== null ? JSON.parse(tokens) : undefined;

        return physioBE({
            method: "POST",
            url: "/auth/refresh",
            data: {
                "refresh_token": tokenStore.refresh.token
            },
        })
            .then(response => {
                if (response.status === 200) {
                    return physioBE(origConfig);
                }
                // TODO: dispatch redux action to logout user
            });
    }
    return error;
});

export default physioBE;
