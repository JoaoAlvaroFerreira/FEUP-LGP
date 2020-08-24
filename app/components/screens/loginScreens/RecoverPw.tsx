import React, { useState } from 'react';
import { View, KeyboardAvoidingView, Text, TouchableHighlight, Alert } from 'react-native';
import LoginTextInput from '../../templates/input/LoginTextInput';
import LogoHeader from './LogoHeader';
import { LoginNavProps } from '../../../routes/LoginStackParamList';
import styles from './styles';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';


const RecoverPw = ({ navigation }: LoginNavProps<'Recover'>) => {
    const [user, setUser] = useState('');

    const recoverPassword = () => {
        Alert.alert('Forgot password clicked, email sent to ' + user);
        navigation.navigate('Login');
    };


    return (
        <View style={{ flex: 1 }}>
            <LogoHeader hasBack onPress={navigation.goBack} />
            <View
                style={styles.InputDivision}>
                <KeyboardAwareScrollView
                    contentContainerStyle={styles.InputDivision}
                    extraScrollHeight={10}>
                    <View style={{ flex: 0.3 }}>
                        <LoginTextInput
                            placeholder='Email'
                            value={user}
                            onChange={user => setUser(user)}
                            autoCapitalize='none'
                            textContentType={'username'}
                        />
                    </View>
                    <View
                        style={{ flex: 0.3, alignItems: 'center', justifyContent: 'center' }}>
                        <TouchableHighlight
                            style={styles.AuthButtons}
                            onPress={recoverPassword}
                            underlayColor='#338DFF'>
                            <Text
                                style={{ color: "white", fontSize: 20 }}>
                                Enviar nova password
                            </Text>
                        </TouchableHighlight>
                    </View>
                </KeyboardAwareScrollView>
            </View>
        </View>
    );
};

export default RecoverPw;