import React from 'react'

export default function PoweredBy() {
    return (
        <div className='powerby'>
            <div className="powerbylogo">
                <iconify-icon icon="simple-icons:openai" width="30" style={{color: "#a998fd"}}></iconify-icon>
                <h1>OpenAI</h1>
            </div>
            <span>Powered By</span>
        </div>
    )
}
