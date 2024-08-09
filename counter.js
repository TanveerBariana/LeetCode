/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    
    return function() {
        const j = n
        n = n + 1
        return j    
    };
};


// const counter = createCounter(10)
// counter() // 10
// counter() // 11
// counter() // 12
