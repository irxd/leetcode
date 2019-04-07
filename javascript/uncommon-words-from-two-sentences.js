// https://leetcode.com/problems/uncommon-words-from-two-sentences/

var uncommonFromSentences = function(A, B) {
    const splittedA = A.split(" ");
    const splittedB = B.split(" ");
    const wordCounter = {};
    const result = [];
    
    for(let i=0; i<splittedA.length; i++) {
        wordCounter[splittedA[i]] = (wordCounter[splittedA[i]] || 0) +1;
    }
    
    for(let i=0; i<splittedB.length; i++) {
        wordCounter[splittedB[i]] = (wordCounter[splittedB[i]] || 0) +1;
    }
    
    for(let key in wordCounter) {
        if(wordCounter[key] === 1) result.push(key);
    }
    
    return result;
};
