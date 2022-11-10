
export const msgTypes = Object.freeze({
    post: 1,    // Misc
    code: 2,    // Code injection
    error: 3,   // Error during code run
    success: 4  // Code run success
});

/**
 * Creates a message object of the expected messaging format for messaging 
 * between the main window and sandbox.
 * @param {String} sender - name of the sender
 * @param {Number} type - msgType type code
 * @param {*} data - message payload 
 * @returns {Object} The message object
 */
export const Message = (
    sender='none', 
    type=msgTypes.post, 
    data='none'
) =>({sender, type, data});
