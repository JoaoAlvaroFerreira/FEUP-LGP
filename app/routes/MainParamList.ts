import { StackNavigationProp } from "@react-navigation/stack";
import { RouteProp } from "@react-navigation/native";
import { User } from "../store/user/types";
import { MuscleTest, Treatment, Summary, Perimetry, Goniometry, OtherAnnotations } from "../store/treatment/types";
import { Patient } from "../store/patients/types";
import { BodyPart } from "../store/body_parts/types";
import { Physiotherapist } from "../store/physiotherapists/types";

export type MainStackParamList = {
    AddDoctor: undefined;
    PhysiotherapistInfo:
    {
        physiotherapist: Physiotherapist
    };
    AddDate: {
        treatment: Treatment
    }
    Profile: {
        patient: Patient
    };
    Patients: undefined;
    Treatment: {
        treatment?: Treatment;
    };
    OtherAnnotations: {
        annotationType: string,
        otherAnnotations: OtherAnnotations,
        onSave: (otherAnnotations: OtherAnnotations) => void;
    }
    OtherAnnotationsList: {
        otherAnnotations: OtherAnnotations,
        onSave: (otherAnnotations: OtherAnnotations) => void;
    }
    MuscleTestList: {
        tests: MuscleTest[];
        onSave: (tests: MuscleTest[]) => void;
    };
    MuscleTest: {
        test?: MuscleTest;
        onSave: (test: MuscleTest) => void;
    };
    PerimetryList: {
        tests: Perimetry[];
        onSave: (tests: Perimetry[]) => void;
    };
    Perimetry: {
        test?: Perimetry;
        onSave: (test: Perimetry) => void;
    };
    GoniometryList: {
        tests: Goniometry[];
        onSave: (tests: Goniometry[]) => void;
    };
    Goniometry: {
        test?: Goniometry;
        onSave: (test: Goniometry, index?: number) => void;
        index?: number;
    };
    Test: undefined;
    AddTreatmentSummary: {
        summary: Summary;
        onSave: (summary: Summary) => void;
    };
    TermsAndConditions: {
        onSave: () => void;
    };
    ListPreviousTreatments: undefined;
    SearchBodyPart: {
        muscle: string;
        onSave: (muscle: BodyPart) => void;
    };
};

export type MainNavProps<T extends keyof MainStackParamList> = {
    navigation: StackNavigationProp<MainStackParamList, T>;
    route: RouteProp<MainStackParamList, T>;
};
