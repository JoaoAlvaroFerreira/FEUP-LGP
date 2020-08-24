import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

interface Props {
    first: number;
    second: number;
    unit: string;
    paddingFirst: number;
    paddingSecond: number;
}

const RangeOutput: React.FC<Props> = ({
    first,
    second,
    unit,
    paddingFirst,
    paddingSecond
}) => (
        <View style={styles(paddingFirst, paddingSecond).container}>
            <Text style={styles(paddingFirst, paddingSecond).first}>{first}{unit}</Text>
            <Text style={styles(paddingFirst, paddingSecond).second}>{second}{unit}</Text>
        </View>
    );

const styles = ( paddingFirst: number, paddingSecond: number ) => StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: 'row'
    },
    first: {
        fontSize: 13,
        color: '#17224D',
        marginLeft: paddingFirst
    },
    second: {
        fontSize: 13,
        color: '#17224D',
        textAlign: 'right',
        marginLeft: paddingSecond
    }
});

export default RangeOutput;