import React from 'react';
import { StyleSheet, View, TextInput } from 'react-native';

interface Props {
    placeholder?: string;
    value: string;
    onChange: (text: string) => void;
}

const Bigtext: React.FC<Props> = ({
    placeholder,
    value,
    onChange,
}) => (
        <View style={{ flex: 1, alignItems: "stretch" }}>
            <TextInput
                value={value}
                onChangeText={onChange}
                placeholder={placeholder}
                placeholderTextColor="grey"
                multiline
                style={styles.Textinput}
            />
        </View>
    );

const styles = StyleSheet.create({
    Textinput: {
        color: "black",
        borderRadius: 25,
        height: 200,
        paddingHorizontal: 20,
        paddingTop: 20,
        paddingBottom: 20,
        borderColor: "grey",
        borderWidth: StyleSheet.hairlineWidth,
    },
});

export default Bigtext;