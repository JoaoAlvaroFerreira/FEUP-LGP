import React, { Component } from 'react';
import {
    StyleSheet,
    Text,
    View,
    Dimensions
} from 'react-native';
import MultiSlider from '@ptomasroos/react-native-multi-slider';
import RangeOutput from './RangeOutput';
import CustomMarker from './CustomMarker';

export default class RangeSliderInput extends Component {
    constructor(props) {
        super(props);
        this.state = {
            multiSliderValue: [this.props.min, this.props.max],
            label: this.props.label,
            Slidewidth: (Dimensions.get('window').width*3/4)
        };
    }

    multiSliderValuesChange = values => {
        var newValues = [];

        if (this.state.multiSliderValue[0] == values[0]) {
            newValues[0] = this.state.multiSliderValue[0];
        } else {
            newValues[0] = values[0] * this.props.interval;
        }

        if (this.state.multiSliderValue[1] == values[1]) {
            newValues[1] = this.state.multiSliderValue[1];
        } else {
            newValues[1] = values[1] * this.props.interval;
        }

        this.setState({
            multiSliderValue: newValues
        });

        this.props.onChange(this.state.multiSliderValue);
    };

    renderScale = () => {
        var dimesionPerDivision=this.state.Slidewidth/((this.props.max-this.props.min)/this.props.interval);
        var paddingFirst=(dimesionPerDivision*(this.state.multiSliderValue[0]/this.props.interval-this.props.min))+1/16*Dimensions.get('window').width;
        return (
            <RangeOutput
                paddingFirst={paddingFirst}
                paddingSecond={((this.state.multiSliderValue[1]-this.state.multiSliderValue[0])/this.props.interval*dimesionPerDivision)-1/16*Dimensions.get('window').width}
                first={this.state.multiSliderValue[0]}
                second={this.state.multiSliderValue[1]}
                unit={this.props.unit}
            />
        );
    };

    render() {
        return (
            <View style={styles.container}>
                <Text style={styles.label}>
                    {this.state.label}
                </Text>
                <View style={styles.slider}>
                    <MultiSlider
                        values={[this.state.multiSliderValue[0], this.state.multiSliderValue[1]]}
                        sliderLength={this.state.Slidewidth}
                        onValuesChange={this.multiSliderValuesChange}
                        min={this.props.min}
                        max={this.props.max / this.props.interval}
                        step={1}
                        snapped
                        trackStyle={{ backgroundColor: '#bdc3c7' }}
                        selectedStyle={{ backgroundColor: "#17224D" }}
                        customMarker={CustomMarker}
                    />
                </View>
                <View style={styles.column}>
                    {this.renderScale()}
                </View>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        marginTop: 20
    },
    slider: {
        alignItems: 'center',     
    },
    column: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between'
    },
    label: {
        marginBottom: 5,
        color: "#17224D"
    }
});