import React, { ReactElement } from 'react';
import { View, StyleSheet, Text } from 'react-native';
import {
    Ionicons,
    MaterialIcons,
    MaterialCommunityIcons,
    Entypo,
    Feather,
} from '@expo/vector-icons';
import { TouchableHighlight } from 'react-native-gesture-handler';

interface Props {
    leftText: string;
    leftSubtitle?: string;
    onPressRight: () => void;
    rightIcon: ReactElement;
    onPressLeft?: () => void;
    rightText: string;
    rightSubtitle?: string;
    date?: string;
    leftIcon?: ReactElement;
}

const SplitMultiButton: React.FC<Props> = ({
    leftText,
    leftSubtitle,
    rightText,
    rightSubtitle,
    onPressRight,
    onPressLeft,
    date,
    rightIcon,
    leftIcon,
}) => (
        <View>
            <View style={styles.SplitMultiButton}>
                <View style={styles.LeftSplit}>
                    <View style={styles.RightSide}>
                        <View style={{ marginRight: 10 }}>
                            {leftIcon &&
                                (onPressLeft ? (
                                    <TouchableHighlight onPress={onPressLeft}>
                                        {leftIcon}
                                    </TouchableHighlight>
                                ) : (
                                        leftIcon
                                    ))}
                        </View>


                    </View>

                    <View style={styles.SplitText}>
                       
                            <Text style={{ fontSize: 12 }}>{leftText}</Text>
                            <Text style={{ fontSize: 12 }}>{leftSubtitle}</Text>
                      
                    </View>
                </View>
                <View style={styles.Separator} />
                <View style={styles.RightSplit}>

                    <View style={styles.RightSide}>
                        <View style={{ marginRight: 10 }}>
                            {rightIcon &&
                                (onPressLeft ? (
                                    <TouchableHighlight onPress={onPressLeft}>
                                        {rightIcon}
                                    </TouchableHighlight>
                                ) : (
                                    rightIcon
                                    ))}
                        </View>


                    </View>

                    <View style={styles.SplitText}>
                    <Text style={{ fontSize: 12 }}>{rightText}</Text>
                            <Text style={{ fontSize: 12 }}>{rightSubtitle}</Text>
                    </View>
                </View>
            </View>
        </View>
    );

const styles = StyleSheet.create({
    SplitMultiButton: {
        height: 80,
        padding: 20,
        marginBottom: 20,
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between',
        backgroundColor: '#fff',
        borderRadius: 50,
        shadowColor: '#000',
        shadowOffset: { width: 1, height: 4 },
        shadowOpacity: 0.3,
        shadowRadius: 4,
        elevation: 5,
    },
    RightSide: {
        flexDirection: 'row',
        alignItems: 'center',
    },
    CheckBoxIcon: {
        marginRight: 10,
    },
    Column: {
        flexDirection: 'column',
    },
    LeftSplit: {
        width: '50%',
        flexDirection: 'column',
        alignItems: 'center',
    },
    RightSplit: {
        width: '50%',
        marginRight: 0,
        flexDirection: 'column',
        alignItems: 'center',
    },
    SplitText:{
       
        alignItems: 'center',
    },
    Separator: {
        borderLeftWidth: 1,
        height: "180%",
        borderLeftColor: 'black',
    },
});

export const ArrowIcon = (
    <Ionicons name='ios-arrow-forward' size={20} color='#17224D' />
);
export const EditIcon = <MaterialIcons name='edit' size={20} color='#17224D' />;
export const CheckBoxIcon = (
    <MaterialCommunityIcons
        name='checkbox-blank-outline'
        size={20}
        color='#17224D'
        style={styles.CheckBoxIcon}
    />
);
export const CalendarIcon = (
    <MaterialIcons name='today' size={20} color='#17224D' />
);


export const ScheduleIcon = (
    <MaterialIcons name='schedule' size={20} color='#17224D' />
);
export const SplitPhoneIcon = <Entypo name='phone' size={20} color='#17224D' />;
export const MobileIcon = (
    <MaterialIcons name='phone-iphone' size={20} color='#17224D' />
);

export const EmailIcon = <Entypo name='mail' size={20} color='#17224D' />;
export const MapIcon = <Feather name='map-pin' size={20} color='#17224D' />;
export const FileIcon = (
    <MaterialCommunityIcons name='file-pdf' size={20} color='#17224D' />
);

export default SplitMultiButton;
