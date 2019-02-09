// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

/**
 * @param {number[]} A
 * @return {number}
 */
var repeatedNTimes = function(A) {
    let lastNum = 0;
    let result;
    let sortedArr = A.sort((a,b) => a-b);
    
    sortedArr.forEach(arr => {
        if (lastNum === arr) result = arr;
        lastNum = arr
    });
    
    return result;
};
