class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const checkBoard = {
            "[": "]",
            "(": ")",
            "{": "}"
        };
        const stack = [];
        for (let subString of s){
            if ( checkBoard.hasOwnProperty(subString) )  {
                stack.push(subString);
            }
            else if (stack.length && checkBoard[stack[stack.length - 1 ]] === subString) {
                stack.pop();
            } else {
                return false;
            }
        }
        return stack.length === 0;
    }
}
