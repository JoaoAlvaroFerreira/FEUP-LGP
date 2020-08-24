import faker from 'faker/locale/pt_BR';
import { Patient } from "../patients/types";
import { PostCreatePatientData } from "./types";

export const mockPatient = (): Patient => {
    const x = faker.random.number({ min: 0, max: 20 });
    return {
        id: faker.random.uuid(),
        firstName: faker.name.firstName(),
        lastName: faker.name.lastName(),
        email: faker.internet.email(),
        address: {
            city: faker.address.city(),
            street: faker.address.streetName(),
            zipCode: faker.address.zipCode(),
            houseNumber: faker.random.number().toString(),
        },
        completedSession: faker.random.number({ min: 0, max: x }),
        numberOfSessions: x,
        phone: faker.phone.phoneNumber(),
        therapyHistoryURL: faker.internet.url(),
        treatmentCycle: faker.random.uuid(),
    };
};

export const mockPostPatientData = (): PostCreatePatientData => {
    return {
        first_name: faker.name.firstName(),
        last_name: faker.name.lastName(),
        nif: faker.random.number().toString(),
        email: faker.internet.email(),
        birth_date: faker.date.past(20).toISOString().split('T')[0],
        clinical_history: faker.lorem.text(),
        diagnostic: faker.lorem.text(),
        gender: faker.random.number() % 2 == 0 ? "m" : "f",
        profession: faker.name.jobTitle(),
        telephone_number: faker.phone.phoneNumber(),
        address: {
            street: faker.address.streetName(),
            city: faker.address.city(),
            zip_code: faker.address.zipCode(),
        }
    };
};

// export const mockTreatment = (): Treatment => {
//     const startDate = faker.date.between(new Date(new Date().setDate(new Date().getDate() - 1)), new Date());
//     return (
//         {
//             id: faker.random.uuid(),
//             patientName: faker.name.firstName() + " " + faker.name.lastName(),
//             startDate: startDate,
//             endDate: new Date(startDate.getTime() + 30 * 6000),
//             isOpen: faker.random.boolean(),
//             checkBoxes: Array.from(new Array(5), () => true),
//             goniometries: Array.from(new Array(faker.random.number({min: 1, max: 10})), () => {}),
//     }
//     );

// }