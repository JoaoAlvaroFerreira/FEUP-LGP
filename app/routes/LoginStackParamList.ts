import { StackNavigationProp } from "@react-navigation/stack";
import { RouteProp } from "@react-navigation/native";

export type LoginStackParamList = {
    Login: undefined;
    Recover: undefined;
};

export type LoginNavProps<T extends keyof LoginStackParamList> = {
    navigation: StackNavigationProp<LoginStackParamList, T>;
    route: RouteProp<LoginStackParamList, T>;
};
