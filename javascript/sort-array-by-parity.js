// https://leetcode.com/problems/sort-array-by-parity/

/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function(A) {
    let odds = [];
    let evens = [];
    A.forEach(element => {
        if (element % 2 === 0) {
            evens.push(element);
        } else {
            odds.push(element);
        }
    });
    
    return evens.concat(odds);
};
