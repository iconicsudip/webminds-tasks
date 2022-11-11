import React from 'react'

export default function CodeExplain() {
    return (
        <div className='CodeExplain'>
            <div className="codesection">
                <div className='codeheading'>
                    <iconify-icon icon="bx:message-detail" width="30" style={{color: 'black'}}></iconify-icon>
                    <h1>Explain Code</h1>
                </div>
                <p>Explain some code based on the syntax provided</p>
                <p style={{color:"black",fontSize:"1rem",margin:"1rem 0"}}>Paste your code below:</p>
                <div className='code'>
                    <pre>
                        <code>
<><span style={{color:"#381bcb"}}>function </span><span style={{color:"#e63d3d"}}>HelloWorld</span></>{`(text){
    echo text ||`} <><span style={{color:"#009471"}}>"Hello World"</span>;</>
<div>{`}`}</div>
                        </code>
                        {/* <div>
                            {`function HelloWorld(text){
                                echo text || "Hello World";
                            }`}
                        </div> */}
                    </pre>
                </div>
                <div className="enhancecode">
                    <div className="enhancebutton">
                        <iconify-icon icon="tabler:copy" style={{color: "white"}} width="20"></iconify-icon>
                        Enhance with AI
                    </div>
                </div>
            </div>
            <div className="line"></div>
            <div className="explainsection">
                <div className="codeheading2">
                    <iconify-icon icon="bi:arrow-right-circle-fill" width="30"></iconify-icon>
                    <h1>What does the code do?</h1>
                </div>
                <p>The following code does:</p>
                <div className="codepara">
                    <iconify-icon icon="icon-park-twotone:arrow-circle-right" width="20"></iconify-icon>
                    <p>The code above is a function definition</p>
                </div>
                <hr />
                <div className="codepara">
                    <iconify-icon icon="icon-park-twotone:arrow-circle-right" width="20"></iconify-icon>
                    <p>It defines a new function called `HelloWorld` that takes a single argument called `text`</p>
                </div>
                <hr />
                <div className="codepara">
                    <iconify-icon icon="icon-park-twotone:arrow-circle-right" width="20"></iconify-icon>
                    <p>The body of the function is a single line of code that prints out the value of `text` if it is defined, or `Hello World` if it is not defined.</p>
                </div>
                <div className="enhancecode">
                    <div className="copybutton">
                        <iconify-icon icon="tabler:copy" style={{color: "black"}} width="20"></iconify-icon>
                        Copy Output
                    </div>
                </div>
            </div>
        </div>
    )
}
