import React from 'react';
import { StyleSheet, Text, View, Slider, Dimensions } from 'react-native';

interface Props {
    label?: string;
    min?: number;
    max?: number;
    unit: string;
    value: number;
    onChange: (text: number) => void;
}

const SliderInput: React.FC<Props> = ({
    label,
    min,
    max,
    unit, 
    value,
    onChange
}) => (
    <View style={styles.container}>
        <Text style={styles.label}>
            {label}
        </Text>
        <View style={styles.slider}>
            <Slider
                style={{ width: Dimensions.get('window').width - 40 }}
                step={1}
                minimumValue={min}
                maximumValue={max}
                value={value}
                onValueChange={onChange}
                minimumTrackTintColor="#17224D"
                thumbTintColor="#17224D"
            />
        </View>
        <Text style={styles.value}>
            {value} {unit}
        </Text>
    </View>
);


const styles = StyleSheet.create({
    container: {
        flex: 1
    },
    value: {
        textAlign: 'center',
        color: '#17224D'
    },
    label: {
        marginTop: 20,
        marginBottom: 5,
        color: '#17224D'
    },
    slider: {
        alignItems: 'center',
        marginTop: 20
    }
});

export default SliderInput;