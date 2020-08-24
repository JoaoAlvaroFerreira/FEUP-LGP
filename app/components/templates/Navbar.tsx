import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { TouchableOpacity } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import { useNavigation } from '@react-navigation/native';

const Navbar: React.FC = () => {
    const navigation = useNavigation();
    
    return (
        <View style={styles.BottomBar}>
            <TouchableOpacity style={styles.Button} onPress={() => navigation.navigate('ListPreviousTreatments')} >
                <AntDesign name="user" size={25} color="white" />
                <Text style={{ color: "white", textAlign: "center", marginTop: 5 }}>Perfil</Text>
            </TouchableOpacity>

            <TouchableOpacity style={styles.Button} onPress={() => navigation.navigate('Patients')}>
                <AntDesign name="plus" size={25} color="white" />
                <Text style={{ color: "white", textAlign: "center", marginTop: 5 }}>Pacientes</Text>
            </TouchableOpacity>
        </View>
    );
};

const styles = StyleSheet.create({
    BottomBar: {
        position: "absolute",
        bottom: 0,
        left: 0,
        right: 0,
        height: 70,
        flexDirection: "row",
        borderTopColor: '#FFFFFF',
        borderTopWidth: 1,
    },
    Button: {
        flex: 1,
        justifyContent: "center",
        backgroundColor: "#17224D",
        alignItems: "center",
    }
});

export default Navbar;