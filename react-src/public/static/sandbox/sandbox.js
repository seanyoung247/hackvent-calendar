
(function sandbox() {
    /* Messaging */
    const msgTypes = Object.freeze({
        post: 1,
        code: 2,
        error: 3,
        success: 4
    });    
    const Message = (
        sender='none', 
        type=msgTypes.post, 
        data='none'
    ) =>({sender, type, data});

    const isWorker = (typeof WorkerGlobalScope !== 'undefined' && self instanceof WorkerGlobalScope);
    if (isWorker) {

        /* Worker Code */
        onmessage = e => {
            console.log(e.data);
        }

    } else {

        /* iFrame Code */
        window.onmessage = e => {
            const message = e.data;
            const sender = e.source;
            const origin = e.origin;

            // If the main window is sending us some code to run
            if (message.sender === 'main' && message.type === msgTypes.code) {
                // Create the webworker to run the code
                const blob = new Blob([`(${sandbox.toString()})()`], {type: 'application/javascript'});
                const worker = new Worker(URL.createObjectURL(blob));

                worker.onmessage = e => {
                    // react to messaging from worker here
                }

                // Send the code to the worker
                worker.postMessage(Message('sandbox', msgTypes.code, e.data.data));

                // Start worker termination timer...
            }
        }

    }
})();
