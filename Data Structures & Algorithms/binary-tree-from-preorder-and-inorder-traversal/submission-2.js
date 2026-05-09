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
     * @param {number[]} preorder
     * @param {number[]} inorder
     * @return {TreeNode}
     */
    buildTree(preorder, inorder) {
        if (!preorder.length || !inorder.length) {
            return null
        }
        let root = new TreeNode(preorder[0]);
        let mid = inorder.indexOf(root.val); 
        // Split the inorder and preorder arrays for left and right subtrees.
        let inorderLeft = inorder.slice(0, mid);
        let inorderRight = inorder.slice(mid + 1);

        let preorderLeft = preorder.slice(1, mid + 1);
        let preorderRight = preorder.slice(mid + 1);

        
        root.left = this.buildTree(preorderLeft, inorderLeft);
        root.right = this.buildTree(preorderRight, inorderRight);
        return root;
    }
}
