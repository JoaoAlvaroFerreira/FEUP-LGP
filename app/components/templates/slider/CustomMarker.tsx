import React from 'react';
import { StyleSheet, Image } from 'react-native';

const CustomMarker: React.FC = () => (
  <Image
    style={styles.image}
    source={{ uri: 'https://i.ibb.co/3rkdXnY/custom-marker.png' }}
    resizeMode="contain"
  />
);

const styles = StyleSheet.create({
  image: {
    height: 11,
    width: 11
  },
});

export default CustomMarker;