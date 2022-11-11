import Header from './components/Header';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import './index.css';
import Home from './components/Home';
import Features from './components/Features'
import Pricing from './components/Pricing'
import Contact from './components/Contact'
import Login from './components/Login'
import Signup from './components/Signup'
import { useState } from 'react';


function App() {
  const [linkColor,setLinkColor] = useState(window.location.pathname)
  
  return (
    <div className="App">
      <Router>
        <Header linkColor={linkColor} setLinkColor={setLinkColor}/>
        <Routes>
          <Route exact path="/" element={<Home linkColor={linkColor} setLinkColor={setLinkColor}/>} />
          <Route exact path="features" element={<Features />} />
          <Route exact path="pricing" element={<Pricing />} />
          <Route exact path="contact" element={<Contact />} />
          <Route exact path="login" element={<Login />} />
          <Route exact path="signup" element={<Signup />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
