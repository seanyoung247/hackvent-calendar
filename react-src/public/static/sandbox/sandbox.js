
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
/* End Messaging */


/* Code to be run in the worker */
function workerCode() {

    console.log('in worker?', typeof WorkerGlobalScope !== 'undefined');

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

    // Just send a test message to prove worker creation and messaging
    onmessage = function(e) {
        postMessage(Message(
            "worker",
            msgTypes.success,
            "worker started"
        ));
    }
    //TODO: The actual code...
}
/* End worker code */


/// TODO refactor to one code base for sandbox and worker



/* Code to be run in the sandboxed iframe */
window.onmessage = e => {
    const message = e.data;
    const mainWindow = e.source;
    const origin = e.origin;

    console.log('in worker?', typeof WorkerGlobalScope !== 'undefined');
    
    // If this message is coming from the main window
    if (message.sender === 'main') {
        // Because the iframe is sandboxed without permissions to load files
        // we have to construct the worker from a data blob instead of a js file
        const blob = new Blob([`(${workerCode.toString()})()`], {type: 'application/javascript'});
        const worker = new Worker(URL.createObjectURL(blob));

        // Recieves mesages from the worker
        worker.onmessage = e => {
            mainWindow.postMessage(Message(
                "sandbox",
                e.data.type,
                e.data.data
            ), origin);
            //ToDo: worker should be terminated after time delay or 
            //      completion signal, whichever comes first
            worker.terminate();
        }
        // Sends the start message to the worker
        worker.postMessage('test');

        // Sends a test confirmation message back to the main window
        
        mainWindow.postMessage(Message(
            "sandbox",
            msgTypes.success,
            `Sandbox received: ${message.data}`
        ), origin);
    }
}