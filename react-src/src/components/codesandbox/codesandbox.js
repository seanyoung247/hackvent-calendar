
import React, { useEffect, useRef } from 'react';


const style = {
    "position": "absolute",
    "pointerEvents": "none",
    "width":"0",
    "height":"0",
    "opacity": "0"
}


export default function CodeSandbox({title, code, ...rest}) {
    const sandboxEl = useRef(null);
    const message = {
        sender: "main",
        type: "post",
        data: code || 'none'
    }
    sandboxEl.current?.contentWindow.postMessage(message, '*');

    useEffect(()=>{
        const onMsg = e => {
            const message = e.data;
            if (message.sender === 'sandbox') {
                console.log('Main recieved:', message.data);
            }
        }
        window.addEventListener('message', onMsg);
        return () => window.removeEventListener('message', onMsg);
    });

    return (
        <iframe 
            {...rest}
            title={title}
            ref={sandboxEl}
            style={style}
            sandbox="allow-scripts" 
            frameBorder="0"
        />
    );
}