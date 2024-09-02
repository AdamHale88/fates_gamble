import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import './App.css';
import StartScreen from "./components/startscreen";
import Layout from "./components/layout";
import MainScreen from "./components/mainscreen";

const App = () => {

    return (
        <Router>
            <Routes>
                <Route element={<Layout/>}>
                    <Route path="/" element={<StartScreen/>}/>
                    <Route path="MainScreen" element={<MainScreen/>}/>
                </Route>
            </Routes>
        </Router>
    );
}

export default App;
