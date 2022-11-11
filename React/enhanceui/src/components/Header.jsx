import React, { useState } from 'react'
import {Link} from 'react-router-dom';
import LoginLink from './Authentication/LoginLink';
import SignupLink from './Authentication/SignupLink';

export default function Header({linkColor,setLinkColor}) {
    const [getClass,setClass] = useState("navlinks");
    const [hamburger,setHamburger] = useState(<iconify-icon width="30" icon="charm:menu-hamburger"></iconify-icon>);
    const change = (path)=>{
        setLinkColor(path)
    }
    const classChange = ()=>{
        if(getClass === "navlinks"){
            setClass("navlinks navactive")
            setHamburger(<iconify-icon width="30" icon="akar-icons:cross"></iconify-icon>)
        }else{
            setClass("navlinks")
            setHamburger(<iconify-icon width="30" icon="charm:menu-hamburger"></iconify-icon>)
        }
    }
    return (
        <div className='header'>
            <div className="header_all">
                <div className="logo">
                    <Link onClick={()=>change("/")} to="/">
                        <img src="./logo.png" alt="logo" />
                        <h2>Enhance AI</h2>
                    </Link>
                </div>
                <div className="hamburger" onClick={classChange}>
                    {hamburger}
                </div>
                <div className={getClass}>

                    <div className={linkColor==="/"?"outside-link active":"outside-link"}>
                        <Link onClick={()=>change("/")} to="/">Home</Link>
                    </div>
                    <div className={linkColor==="/features"?"outside-link active":"outside-link"}>
                        <Link onClick={()=>change("/features")} to="features">Features</Link>
                    </div>
                    <div className={linkColor==="/pricing"?"outside-link active":"outside-link"}>
                        <Link onClick={()=>change("/pricing")} to="pricing">Pricing</Link>
                    </div>
                    <div className={linkColor==="/contact"?"outside-link active":"outside-link"}>
                        <Link onClick={()=>change("/contact")} to="contact">Contact</Link>
                    </div>
                    <div className={linkColor==="/login"?"outside-link active":"outside-link"}>
                        <LoginLink setLinkColor={setLinkColor}/>
                    </div>
                    <Link to="/signup" style={{width:"8rem",background:"linear-gradient(to right,#7157f6 , #391ec6)"}} onClick={()=>change("/signup")} className={linkColor==="/signup"?"signupbutton":"signupbutton"}>
                        <SignupLink iconcolor={"white"}/>
                    </Link>
                </div>
            </div>
        </div>
    )
}
