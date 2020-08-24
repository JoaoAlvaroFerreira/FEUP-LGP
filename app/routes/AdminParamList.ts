import { StackNavigationProp } from "@react-navigation/stack";
import { RouteProp } from "@react-navigation/native";
import { Physiotherapist } from "../store/physiotherapists/types";

export type AdminStackParamList = {
    AddDoctor: undefined;
    PhysiotherapistInfo:
    {
        physiotherapist: Physiotherapist
    };
};

export type AdminNavProps<T extends keyof AdminStackParamList> = {
    navigation: StackNavigationProp<AdminStackParamList, T>;
    route: RouteProp<AdminStackParamList, T>;
};
