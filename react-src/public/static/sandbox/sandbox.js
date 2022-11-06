
/* Code to be run in the worker */
function workerCode() {
    onmessage = function(e) {
        const message = {
            sender: "sandbox",
            type: "test",
            data: "Worker started"
        }
        postMessage(message);
    }
}


/* Code to be run in the sandboxed iframe */
window.onmessage = e => {
    const message = e.data;
    const mainWindow = e.source;
    const origin = e.origin;
    
    if (message.sender === 'main') {
        // Because the iframe is sandboxed without permissions to load files
        // we have to construct the worker from a data blob instead of a js file
        const blob = new Blob([`(${workerCode.toString()})()`], {type: 'application/javascript'});
        const worker = new Worker(URL.createObjectURL(blob));

        worker.onmessage = e => {
            mainWindow.postMessage(e.data, origin);
            worker.terminate();
        }

        worker.postMessage('test');

        const responce = {
            sender: "sandbox",
            type: "responce",
            data: `I heard: ${message.data}`
        }
        mainWindow.postMessage(responce, e.origin);
    }
}