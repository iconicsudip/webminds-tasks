import React from 'react'


export default function SignupLink({iconcolor}) {
    return (
        <div >
            <iconify-icon icon="heroicons-outline:user-add" style={{color: iconcolor,height: "0.9rem"}}></iconify-icon>
            <p style={{color:iconcolor}}>Free Signup</p> 
        </div>
    )
}
