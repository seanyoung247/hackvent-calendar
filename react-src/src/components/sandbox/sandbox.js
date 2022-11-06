
import React, { useEffect, useRef } from 'react';
import Styles from './sandbox.module.css';


export default function CodeSandbox({code, ...rest}) {
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
            ref={sandboxEl}
            className={Styles.sandbox}
            sandbox="allow-scripts" frameBorder="0">
        </iframe>
    );
}