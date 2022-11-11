import React from 'react'
import {Link} from 'react-router-dom';

export default function LoginLink({setLinkColor}) {
    const change = (path)=>{
        setLinkColor(path)
    }
    return (
        <Link onClick={()=>change("/login")} to="/login">Login</Link>
    )
}
