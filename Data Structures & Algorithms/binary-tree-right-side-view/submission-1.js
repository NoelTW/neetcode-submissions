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
     * @return {number[]}
     */
    rightSideView(root) {
        // inorder
        let res = [];
        let que = [];
        if (root) {
            que.push(root);
        }
        while ( que.length > 0 ) {
            let length = que.length;
            for (let i = 0; i < length; i++ ){
                var curr = que.shift();
                if (curr.left){
                    que.push(curr.left);
                }
                if (curr.right){
                    que.push(curr.right);
                }
            }
            res.push( curr.val )
        }
    return res
    }
}
