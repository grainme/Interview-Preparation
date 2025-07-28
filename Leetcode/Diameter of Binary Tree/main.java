/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int diameter = 0;

    private int depth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftSubtree = depth(root.left);
        int rightSubtree = depth(root.right);

        this.diameter = Math.max(this.diameter, leftSubtree + rightSubtree);

        return Math.max(leftSubtree, rightSubtree) + 1;
    }

    public int diameterOfBinaryTree(TreeNode root) {
        depth(root);

        return this.diameter;
    }
}
