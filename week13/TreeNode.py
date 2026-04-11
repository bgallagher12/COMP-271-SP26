from __future__ import annotations


class TreeNode:

    def __init__(self, word: str):
        """A node in a binary search tree.
        The node contains a word, a count of the number of times the
        word has been added to the tree, and references to the left
        and right child nodes."""
        self._word = word
        self._count = 1
        self._left = None
        self._right = None

    def __str__(self) -> str:
        """Return a string representation of the node."""
        return f"{self._word}: {self._count}"

    def get_word(self) -> str:
        """Return the word stored in the node."""
        return self._word

    def get_count(self) -> int:
        """Return the count of the word stored in the node."""
        return self._count

    def set_count(self, count: int) -> None:
        """Set the count of the word stored in the node."""
        self._count = count

    def increment_count(self) -> None:
        """Increment the count of the word stored in the node by 1."""
        self._count += 1

    def get_left(self) -> TreeNode:
        """Return the left child node."""
        return self._left

    def set_left(self, left: TreeNode) -> None:
        """Set the left child node."""
        self._left = left

    def get_right(self) -> TreeNode:
        """Return the right child node."""
        return self._right

    def set_right(self, right: TreeNode) -> None:
        """Set the right child node."""
        self._right = right
