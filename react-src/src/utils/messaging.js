
export const msgTypes = Object.freeze({
    post: 1,
    code: 2,
    error: 3,
    success: 4
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
