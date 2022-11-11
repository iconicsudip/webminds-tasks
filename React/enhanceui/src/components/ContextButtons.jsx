import React from 'react'

export default function ContextButtons({context,contextKey,contextLine,contextIcon,setContext}) {
    const showContext=(key)=>{
        setContext(key)
    }
    return (
        <div className={context===contextKey?'_buttons bactive':'_buttons'} onClick={()=>showContext(contextKey)} >
            {contextIcon}
            <span>{contextLine}</span>
        </div>
    )
}
