package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
	// what if the tree is empty :)
	if root == nil {
		return nil
	}

	// swapping nodes
	tempNode := root.Left
	root.Left = root.Right
	root.Right = tempNode

	// we should invert every subtree
	invertTree(root.Left)
	invertTree(root.Right)
	return root
}

func main() {
	// no need
}
