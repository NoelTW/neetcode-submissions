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
     * @return {number[][]}
     */
    levelOrder(root) {
        let que = [];
        let res = [];
        if (root) {
            que.push(root);
        }
        while (que.length > 0) {
            let length = que.length;
            let layer = [];
            for (let i = 0 ;  i < length; i++){
                let curr = que.shift();
                if (curr.left) {
                    que.push(curr.left);
                }
                if (curr.right) {
                    que.push(curr.right);
                }
                layer.push(curr.val)
            }
            res.push(layer)
        }
        return res
    }
}
