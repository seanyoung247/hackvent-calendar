
import React, { useEffect, useRef } from 'react';
import { msgTypes, Message } from '../../utils/messaging.js';

const style = {
    "position": "absolute",
    "pointerEvents": "none",
    "width":"0",
    "height":"0",
    "opacity": "0"
}


export default function CodeSandbox({title, code, ...rest}) {
    const sandboxEl = useRef(null);
    sandboxEl.current?.contentWindow.postMessage(Message(
        'main',
        msgTypes.code,
        code
    ), '*');

    useEffect(()=>{
        const onMsg = e => {
            const message = e.data;
            if (message.sender === 'sandbox') {
                console.log('Main received:', message.data);
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