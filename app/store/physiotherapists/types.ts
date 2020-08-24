export type Physiotherapist = {
    id: string;
    name: string;
    professional_certificate: string;
    email: string;
    state: string;
}

export type State = {
    id: string;
    name: string;
    description: string;
}

export type PhysiotherapistsState = {
    Physiotherapists: Physiotherapist[];
    isFetching: boolean;
    isValid: boolean;
} & Pagination;

export type Pagination = {
    page: number;
    size: number;
};

// Actions types
export type InvalidatePhysiotherapistsAction = {
    type: typeof INVALIDATE_PHYSIOTHERAPISTS;
};

export type RequestPhysiotherapistsAction = {
    type: typeof REQUEST_PHYSIOTHERAPISTS;
};

export type ReceivePhysiotherapistsAction = {
    type: typeof RECEIVE_PHYSIOTHERAPISTS | typeof GET_MORE_PHYSIOTHERAPISTS;
    Physiotherapists: Physiotherapist[];
};

export type PhysiotherapistsActionTypes = InvalidatePhysiotherapistsAction | RequestPhysiotherapistsAction | ReceivePhysiotherapistsAction;

// Actions constants
export const INVALIDATE_PHYSIOTHERAPISTS = '/store/Physiotherapists/action/INVALIDATE_PHYSIOTHERAPISTS';
export const REQUEST_PHYSIOTHERAPISTS = '/store/Physiotherapists/action/REQUEST_PHYSIOTHERAPISTS';
export const RECEIVE_PHYSIOTHERAPISTS  = '/store/Physiotherapists/action/RECEIVE_PHYSIOTHERAPISTS';
export const GET_MORE_PHYSIOTHERAPISTS  = '/store/Physiotherapists/action/GET_MORE_PHYSIOTHERAPISTS';