import { START_FETCHING, StartFetchingAction, RECEIVED, BodyPart, FILTER, ReceivedBodyParts, FilterBodyParts } from "./types";

export const startFetchingBodyParts = (): StartFetchingAction => (
    {
        type: START_FETCHING,
    }
);


export const receivedBodyParts = (bodyParts: BodyPart[]): ReceivedBodyParts => (
    {
        type: RECEIVED,
        bodyParts,
    }
);

export const filterBodyParts = (query: string): FilterBodyParts => (
    {
        type: FILTER,
        query,
    }
);