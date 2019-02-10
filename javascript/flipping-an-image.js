// https://leetcode.com/problems/flipping-an-image/

/**
 * @param {number[][]} A
 * @return {number[][]}
 */
var flipAndInvertImage = function(A) {
    const reversedArr = A.map(arr => {
        return arr.reverse();
    });
    
    
    const result = reversedArr.map(arr => {
        return arr.map(element => {
            return element ^= 1;
        });
    });
    
    return result;
};
