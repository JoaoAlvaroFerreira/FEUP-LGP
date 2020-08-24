import React from 'react';
import {Provider} from 'react-redux';
import store from './store/index';
import {Crossroad} from './routes/Crossroad';

const App: React.FC = () => {
	return (
		<Provider store={store}>
			<Crossroad />
		</Provider>
	);
};

export default App;
