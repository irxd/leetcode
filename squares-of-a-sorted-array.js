// https://leetcode.com/problems/squares-of-a-sorted-array/

/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortedSquares = function(A) {
    const squaredArr = A.map(arr => {
        return arr*arr;
    });
    return squaredArr.sort((a,b) => a-b);
};
