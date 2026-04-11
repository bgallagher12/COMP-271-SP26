from __future__ import annotations
from TreeNode import TreeNode


class BST:

    def __init__(self):
        """A binary search tree.
        The tree contains a reference to the root node and a
        count of the number of unique words in the tree."""
        self._root = None
        self._size = 0

    def insert(self, word: str) -> None:
        """Insert a word into the tree. If the word is already in the
        tree, increment its count."""
        self._root = self._insert(self._root, word)

    def _insert(self, node: TreeNode, word: str) -> TreeNode:
        """Helper method to insert a word into the tree. The method takes
        a node and a word as arguments and returns the node after the word
        has been inserted. If the node is None, a new node is created with
        the word and its count is set to 1. If the word is less than the
        word in the node, the method is called recursively on the left
        child of the node. If the word is greater than the word in the node,
        the method is called recursively on the right child of the node.
        If the word is equal to the word in the node, its count is
        incremented by 1."""
        if node is None:
            # If the node is None, create a new node with the word. The
            # count of the word is set to 1 in the TreeNode constructor,
            # so we don't need to set it here.
            node = TreeNode(word)
            # We need to update the size of the tree because we have added a
            # new unique word to it.
            self._size += 1
        else:
            if word < node.get_word():
                # If the word is less than the word in the node, insert the word
                # into the left subtree of the node.
                left_subtree: TreeNode = node.get_left()
                updated_left_subtree: TreeNode = self._insert(left_subtree, word)
                node.set_left(updated_left_subtree)
            elif word > node.get_word():
                # If the word is greater than the word in the node, insert the word
                # into the right subtree of the node.
                right_subtree: TreeNode = node.get_right()
                updated_right_subtree: TreeNode = self._insert(right_subtree, word)
                node.set_right(updated_right_subtree)
            else:
                # If the word is equal to the word in the node, increment its count.
                node.increment_count()
        # Return the node after the word has been inserted.
        return node

    def get_size(self) -> int:
        """Return the number of unique words in the tree."""
        return self._size

    def insert_iteratively(self, word: str) -> None:
        """Insert a word into the tree iteratively. If the word is already in the
        tree, increment its count. The method is for illustrative purposes and
        as such it is not compliant with the Programmer's Pact."""
        if self._root is None:
            # If the tree is empty, create a new node with the word and set it
            # as the root of the tree. The count of the word is set to 1 in
            # the TreeNode constructor, so we don't need to set it here. We
            # need to update the size of the tree because we have added a new
            # unique word to it.
            self._root = TreeNode(word)
            self._size += 1
        else:
            # If the tree is not empty, we need to find the correct position for
            # the new word. We start at the root of the tree and compare the
            # new word with the word in the current node. If the new word is
            # less than the word in the current node, we move to the left child
            # of the current node. If the new word is greater than the word in
            # the current node, we move to the right child of the current node.
            # If we find a node with the same word as the new word, we increment
            # its count and return. If we reach a None node, we create a new
            # node with the new word and set it as a child of the last non-None
            # node we visited. We also need to update the size of the tree
            # because we have added a new unique word to it.
            current = self._root
            while True:
                if word < current.get_word():
                    if current.get_left() is None:
                        current.set_left(TreeNode(word))
                        self._size += 1
                        break
                    else:
                        current = current.get_left()
                elif word > current.get_word():
                    if current.get_right() is None:
                        current.set_right(TreeNode(word))
                        self._size += 1
                        break
                    else:
                        current = current.get_right()
                else:
                    current.increment_count()
                    break


if __name__ == "__main__":
    bst = BST()
    bst.insert_iteratively("hello")
    bst.insert_iteratively("world")
    bst.insert_iteratively("hello")
    print(bst.get_size())  # Output: 2
    print(bst._root)  # Output: hello: 2
    print(bst._root.get_left())  # Output: None
    print(bst._root.get_right())  # Output: world: 1
    print()

    bst2 = BST()
    bst2.insert("hello")
    bst2.insert("world")
    bst2.insert("hello")
    print(bst2.get_size())  # Output: 2
    print(bst2._root)  # Output: hello: 2
    print(bst2._root.get_left())  # Output: None
    print(bst2._root.get_right())  # Output: world: 1
