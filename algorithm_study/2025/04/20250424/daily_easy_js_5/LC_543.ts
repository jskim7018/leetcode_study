class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}


function diameterOfBinaryTree(root: TreeNode | null): number {
    
    function getDiameter(node: TreeNode|null): number {
        if (node == null) {
            return 0
        }
        
        let left_height = getDiameter(node.left)
        let right_height = getDiameter(node.right)
        let ret = Math.max(left_height, right_height) + 1

        return ret
    }
};