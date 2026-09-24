/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timerId = null;

    return function(...args) {
        // Clear any existing pending call
        if (timerId !== null) {
            clearTimeout(timerId);
        }

        // Schedule execution after `t` milliseconds
        timerId = setTimeout(() => {
            fn(...args);
        }, t);
    };
};

/**
 * Example usage:
 * const log = (...args) => console.log(...args);
 * const dlog = debounce(log, 50);
 * dlog(1); // cancelled
 * dlog(2); // executed after 50ms
 */