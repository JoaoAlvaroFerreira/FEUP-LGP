import { combineReducers, createStore, applyMiddleware } from "redux";
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension';
import { treatmentReducer } from "./treatment/reducers";
import { patientsReducer } from "./patients/reducers";
import { userReducer } from "./user/reducers";
import { bodyPartsReducer } from "./body_parts/reducers";


const rootReducer = combineReducers({
    treatmentStore: treatmentReducer,
    patientsStore: patientsReducer,
    userStore: userReducer,
    bodyPartsStore: bodyPartsReducer,
});

export type AppState = ReturnType<typeof rootReducer>;

export default createStore(
    rootReducer,
    composeWithDevTools(applyMiddleware(thunk)),
);
