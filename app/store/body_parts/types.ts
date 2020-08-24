export type BodyPartsState = {
    bodyParts: BodyPart[];
    filteredBodyParts: BodyPart[];
    isFetching: boolean;
};

export type BodyPart = {
    id: string;
    name: string;
};

export type StartFetchingAction = {
    type: typeof START_FETCHING;
};

export type ReceivedBodyParts = {
    type: typeof RECEIVED;
    bodyParts: BodyPart[];
};

export type FilterBodyParts = {
    type: typeof FILTER,
    query: string,
};

export type BodyPartsAction = StartFetchingAction | ReceivedBodyParts | FilterBodyParts;

export const START_FETCHING = "store/body_parts/types/START_FETCHING";
export const RECEIVED = "store/body_parts/types/RECEIVED";
export const FILTER = "store/body_parts/types/FILTER";
