/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {TreeNode}
     */
    invertTree(root) {
        let stack = new Array();
        let cur = root;
        while (cur || stack.length > 0){
            while ( cur ){
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            let temp = cur.right;
            cur.right = cur.left
            cur.left = temp;
            cur = cur.left;
        }
    return root;
    }
     
}
