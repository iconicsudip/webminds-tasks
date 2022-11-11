import React,{useState} from 'react'
import {Link} from 'react-router-dom';
import SignupLink from './Authentication/SignupLink';
import ContextButtons from './ContextButtons';
import CodeExplain from './ContextItems/CodeExplain';
import Regex from './ContextItems/Regex';
import ConvertCode from './ContextItems/ConvertCode';
import FixGrammer from './ContextItems/FixGrammer';
import Todo from './ContextItems/Todo';
import PoweredBy from './PoweredBy';

export default function Home({linkColor,setLinkColor}) {
    const [context,setContext] = useState("explain");
    const programming_buttons = [
        {
            "key":"explain",
            "line":"Explain Code",
            "icon":<iconify-icon icon="bx:message-detail" style={{color: '#351ac8'}}></iconify-icon>
        },
        {
            "key":"regex",
            "line":"Regex",
            "icon":<iconify-icon icon="bi:regex" style={{color: '#351ac8'}}></iconify-icon>
        },
        {
            "key":"convert",
            "line":"Convert Code",
            "icon":<iconify-icon icon="icon-park-outline:transfer-data" style={{color: '#351ac8'}}></iconify-icon>
        }
    ]
    const content_buttons = [
        {
            "key":"grammer",
            "line":"Fix Grammer",
            "icon":<iconify-icon icon="akar-icons:pencil" style={{color: '#351ac8'}}></iconify-icon>
        },
        {
            "key":"todo",
            "line":"Todo",
            "icon":<iconify-icon icon="fluent:document-one-page-24-regular" style={{color: '#351ac8'}}></iconify-icon>
        }
    ]
    const change = (path)=>{
        setLinkColor(path)
    }
    return (
        <div className='body'>
            <div className="contents">
                <section className='content1'>
                    <div className="heading">
                        <h1>AI <span>to write code, blogs & more</span></h1>
                        <div className="tagline">
                            <h5>Enhance everything you do by using the latest from OpenAI to solve problems, write solutions and make life easier.</h5>
                        </div>
                    </div>
                    <Link className='get_started' to="/">Get Started</Link>
                </section>
                <section className='content2'>
                    <div className="context">
                        <div className="blocks">
                            <div className="context_section">
                                {context==="explain"?<CodeExplain />:null}
                                {context==="regex"?<Regex />:null}
                                {context==="convert"?<ConvertCode />:null}
                                {context==="grammer"?<FixGrammer />:null}
                                {context==="todo"?<Todo />:null}
                            </div>
                        </div>
                        <div className="context_buttons">
                            <div className="ai_programming">
                                <div className="buttons">
                                    {programming_buttons.map((button,ind)=>{
                                        return <ContextButtons context={context} setContext={setContext} key={"prog"+ind} contextKey={button.key} contextLine={button.line} contextIcon={button.icon}/>
                                    })}
                                </div>
                                <span>Examples of AI for Programming</span>
                            </div>
                            <div className="ai_content">
                                <div className="buttons">
                                    {content_buttons.map((button,ind)=>{
                                        return <ContextButtons context={context} setContext={setContext} key={"cont"+ind} contextKey={button.key} contextLine={button.line} contextIcon={button.icon}/>
                                    })}
                                </div>
                                <span>Examples of AI for Content</span>
                            </div>
                            <div className="poweredby">
                                <PoweredBy />
                            </div>
                        </div>
                    </div>
                    <Link to="/signup" style={{width:"11rem",height:"2rem",background:"white"}} onClick={()=>change("/signup")} className={linkColor==="/signup"?"signupbutton":"signupbutton"}>
                        <SignupLink iconcolor={"#351ac8"}/>
                    </Link>
                </section>
            </div>
        </div>
    )
}
