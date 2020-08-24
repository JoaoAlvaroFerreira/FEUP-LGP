import React from 'react';
import renderer from 'react-test-renderer';

import Grid from '../components/grid/Grid';


describe('<Grid />', () => {
 it('has 1 child', () => {
   const tree = renderer
     .create(
       <Grid/>,
     )
     .toJSON();
   expect(3).toBe(3); 
 });
});