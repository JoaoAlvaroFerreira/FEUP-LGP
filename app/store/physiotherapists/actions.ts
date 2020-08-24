import { InvalidatePhysiotherapistsAction, INVALIDATE_PHYSIOTHERAPISTS, RequestPhysiotherapistsAction, REQUEST_PHYSIOTHERAPISTS, Physiotherapist, ReceivePhysiotherapistsAction, RECEIVE_PHYSIOTHERAPISTS, GET_MORE_PHYSIOTHERAPISTS } from "./types";
import { GetPhysiotherapistsResponse } from "../api/types";

export const invalidatePhysiotherapists = (): InvalidatePhysiotherapistsAction => (
    {
        type: INVALIDATE_PHYSIOTHERAPISTS,
    }
);

export const startFetchingPhysiotherapists = (): RequestPhysiotherapistsAction => (
    {
        type: REQUEST_PHYSIOTHERAPISTS,
    }
);

export const receivedPhysiotherapists = (PhysiotherapistResponse: GetPhysiotherapistsResponse): ReceivePhysiotherapistsAction => {
    const Physiotherapists: Physiotherapist[] = PhysiotherapistResponse.results.map(result => ({
        id: result.id,
        name: result.name,
        firstName: result.person.first_name,
        lastName: result.person.last_name,
        phone: result.person.telephone_number,
        email: result.person.email,
        address: {
            houseNumber: "11", // TODO: Change it
            street: result.person.address.street,
            city: result.person.address.city,
            zipCode: result.person.address.zip_code,
        },
        professional_certificate: result.professional_certificate,
        state: result.state,
    } as Physiotherapist));

    return {
        type: RECEIVE_PHYSIOTHERAPISTS,
        Physiotherapists,
    };
};

export const getMorePhysiotherapists = (Physiotherapists: Physiotherapist[]): ReceivePhysiotherapistsAction => (
    {
        type: GET_MORE_PHYSIOTHERAPISTS,
        Physiotherapists,
    }
);