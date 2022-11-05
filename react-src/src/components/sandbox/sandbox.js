
import React, { useEffect, useRef } from 'react';
import Styles from './sandbox.module.css';


export default function CodeSandbox({title, src, code, ...rest}) {
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
            } else {
                console.log("this is not the message I'm looking for");
            }
        }
        window.addEventListener('message', onMsg);
        return () => window.removeEventListener('message', onMsg);
    });

    return (
        <iframe title={title} ref={sandboxEl}
            src={src} className={Styles.sandbox}
            sandbox="allow-scripts" frameBorder="0" {...rest}>
        </iframe>
    );
}