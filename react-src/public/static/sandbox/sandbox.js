
/* Code to be run in the worker */
function workerCode() {
    // Just send a test message to prove worker creation and messaging
    onmessage = function(e) {
        const message = {
            sender: "sandbox",
            type: "test",
            data: "Worker started"
        }
        postMessage(message);
    }
    //TODO: The actual code...
}
/* End worker code */


/* Code to be run in the sandboxed iframe */
window.onmessage = e => {
    const message = e.data;
    const mainWindow = e.source;
    const origin = e.origin;
    
    // If this message is coming from the main window
    if (message.sender === 'main') {
        // Because the iframe is sandboxed without permissions to load files
        // we have to construct the worker from a data blob instead of a js file
        const blob = new Blob([`(${workerCode.toString()})()`], {type: 'application/javascript'});
        const worker = new Worker(URL.createObjectURL(blob));

        // Recieves mesages from the worker
        worker.onmessage = e => {
            mainWindow.postMessage(e.data, origin);
            worker.terminate();
        }
        // Sends the start message to the worker
        worker.postMessage('test');

        // Sends a test confirmation message back to the main window
        const responce = {
            sender: "sandbox",
            type: "responce",
            data: `I heard: ${message.data}`
        }
        mainWindow.postMessage(responce, origin);
    }
}