# Importing csv module to work directly with the eBid_Monthly_Sales csvs
import csv
import time

class Bid:
    """
    Represents a single Bid from the eBid_Monthly_Sales.csv

    Attributes
    ----------
    bid_id : string
        The string representation of the numerical bid_id.
    title  : string
        The title of the bid.
    fund   : string
        Description of the fund.
    amount : float
        US dollar amount of the bid.
    """
    def __init__(self, bid_id="", title="", fund="", amount=0.0):
        """
        Initializes Bid with argument values or default values

        Args: 
            bid_id: bid's id
            title: bid's title
            fund: bid's fund
            amount: bid's set dollar amount
        """
        self.bid_id = bid_id
        self.title = title
        self.fund = fund
        self.amount = amount


class Node:
    """
    Represents a single node in the Red-Black Tree.

    Attributes
    ----------
    bid   : bid
        Bid attached to the Node. Essentially the value of the node. 
    left  : (Node, optional) 
        Left child Node of current node (bid.bid_id < current.bid.bid_id)
    right : (Node, optional) 
        Right child Node of current node (bid.bid_id > current.bid.bid_id)
    parent : (Node, optional)
        Parent of current node
    color : identifier or classification
        All new nodes start off as red

    """
    def __init__(self, bid):
        """
        Initializes node with a bid and no children

        Args: 
            bid: bid stored on the node
        """
        self.bid = bid
        self.left = None
        self.right = None
        self.parent = None
        self.color = "red"

# Implementing the Red Black Tree non recursively for performance (an iterative approach)
class RBT:
    """
    Red Black Tree (RBT) implementation for storing and managing Bid objects.

    A Red-Black Tree is a self-balancing binary search tree that ensures
    O(log n) worst-case time complexity for insertion, searching, and deletion.

    The tree maintains balance using color properties and rotation operations.

    Attributes
    ----------
    root : Node or None
        The root node of the RBT. None if the tree is empty.
    """
    def __init__(self):
        """
        Initializes RBT with no root node

        Args: 
            root: node
        """
        self.root = None

    # -------------------------------- Insertion ------------------------------
    def insert(self, bid):
        """
        Inserts a Bid into the Red-Black Tree.

        This method performs a standard BST insertion according to
        its bid_id value followed by Red-Black Tree balancing to preserve 
        tree properties.

        Parameters
        ----------
        bid : Bid
            The Bid object to insert into the tree.

        Returns
        -------
        None
        """
        new_node = Node(bid)

        parent = None
        current = self.root

        while current:
            parent = current
            if new_node.bid.bid_id < current.bid.bid_id:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.bid.bid_id < parent.bid.bid_id:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "red"

        self.fix_insert(new_node)

    def fix_insert(self, node):
        """
        Restores Red-Black Tree properties after insertion.

        This method resolves violations caused by inserting a red node.
        It ensures:
        - No two consecutive red nodes exist
        - Equal black-height across all paths
        - Root node remains black

        Parameters
        ----------
        node : Node
            The newly inserted node requiring balancing.

        Returns
        -------
        None
        """
        while node != self.root and node.parent.color == "red":

            if node.parent == node.parent.parent.left:

                uncle = node.parent.parent.right

                if uncle and uncle.color == "red":

                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent

                else:

                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.rotate_right(node.parent.parent)

            else:

                uncle = node.parent.parent.left

                if uncle and uncle.color == "red":

                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent

                else:

                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.rotate_left(node.parent.parent)

        self.root.color = "black"
    # -------------------------------- Rotations ------------------------------
    def rotate_left(self, node):
        """
        Performs a left rotation on the specified node.

        Left rotation moves the node downward and promotes its right child.

        Parameters
        ----------
        node : Node
            Node around which the rotation is performed.

        Returns
        -------
        None
        """
        # Identifying the right child that will be promoted
        right_child = node.right

        # Turning the right_childs subtree into the node right subtree
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node

        # Linking right_child parent to node original parent
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        # Put node on left of right_child
        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        """
        Performs a right rotation on the specified node.

        Right rotation moves the node downward and promotes its left child.

        Parameters
        ----------
        node : Node
            Node around which the rotation is performed.

        Returns
        -------
        None
        """
        # Identifying the left child that will be promoted
        left_child = node.left

        # Turn left_child right subtree into nodes left subtree
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node

        # Link left_childs parent to nodes original parent
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        # Put node on the right of left_child
        left_child.right = node
        node.parent = left_child

    # --------------------------------- Removal -------------------------------
    def remove(self, bid_id):
        """
        Removes a Bid from the Red Black Tree based on bid_id.

        This method locates the node containing the specified bid_id,
        removes it from the tree, and restores Red-Black Tree properties
        using deletion balancing operations.

        Parameters
        ----------
        bid_id : str
            The unique identifier of the Bid to remove.

        Returns
        -------
        None
        """
        node = self._search(bid_id)

        if node is None:
            return
        
        self._remove_node(node)

    def _remove_node(self, node):
        """
        Removes a specified node from the Red-Black Tree and restores balance.

        Handles all deletion cases:
        - Node with no children
        - Node with one child
        - Node with two children

        Parameters
        ----------
        node : Node
            Node to remove from the tree.

        Returns
        -------
        None
        """
        original_color = node.color

        # Case 1: Node has no left child (replaces with right child or None)
        if node.left is None:
            replacement = node.right
            self.transplant(node, node.right)

        # Case 2: Node has no right child (replaces with left child)
        elif node.right is None:
            replacement = node.left
            self.transplant(node, node.left)

        # Case 3: Node has two children
        else:
            # Find the smallest node in the right subtree (this will be the successor)
            successor = self.minimum(node.right)
            original_color = successor.color
            replacement = successor.right

            if successor.parent == node:
                # If successor is direct child, link replacement to it
                if replacement:
                    replacement.parent = successor

            else:
                # If successor is deeper, move successor's right child into successor's spot
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor

            # Move successor into the deleted node's spot and copy its color
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
            successor.color = node.color

        # If we removed a BLACK node, we potentially need to fix the tree
        if original_color == "black":
            if replacement:
                self.fix_after_removal(replacement)
            elif self.root:
                self.fix_after_removal(self.root)

    def fix_after_removal(self, node):
        """
        Restores Red-Black Tree properties after deletion.

        Ensures:
        - Equal black-height across all paths
        - No consecutive red nodes
        - Root remains black

        Parameters
        ----------
        node : Node or None
            Node requiring balancing adjustments.

        Returns
        -------
        None
        """
        while node != self.root and node and node.color == "black":
            # Left side cases
            if node == node.parent.left:
                sibling = node.parent.right

                # Sibling is red 
                if sibling and sibling.color == "red":
                    # Rotate and recolor so the sibling becomes black.
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.rotate_left(node.parent)
                    sibling = node.parent.right

                # Sibling is black and both its children are black
                if sibling is None or (
                    (sibling.left is None or sibling.left.color == "black") and
                    (sibling.right is None or sibling.right.color == "black")
                ):
                    sibling.color = "red"
                    node = node.parent

                else:
                    # Sibling is black, but its right child is black (left is red)
                    if sibling.right is None or sibling.right.color == "black":
                        # Rotate sibling right
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self.rotate_right(sibling)
                        sibling = node.parent.right

                    # Sibling is black and its right child is red
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    if sibling.right:
                        sibling.right.color = "black"
                    self.rotate_left(node.parent)
                    node = self.root

            # Left side cases
            else:
                sibling = node.parent.left
                # Sibling is red
                if sibling and sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.rotate_right(node.parent)
                    sibling = node.parent.left

                # Sibling and its children are black
                if sibling is None or (
                    (sibling.left is None or sibling.left.color == "black") and
                    (sibling.right is None or sibling.right.color == "black")
                ):
                    sibling.color = "red"
                    node = node.parent
                else:
                    # Sibling's left child is black
                    # if the far child is black, rotate the near child
                    if sibling.left is None or sibling.left.color == "black":
                        if sibling.right:
                            sibling.right.color = "black"
                        sibling.color = "red"
                        self.rotate_left(sibling)
                        sibling = node.parent.left

                    # Sibling's left child is red
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    if sibling.left:
                        sibling.left.color = "black"
                    self.rotate_right(node.parent)
                    node = self.root

        # Ensure the final node (or root) is black to maintain RBT rules.
        if node:
            node.color = "black"

    def transplant(self, old_limb, new_limb):
        """
        Replaces one subtree with another subtree.

        Used during deletion to replace nodes while maintaining
        proper parent-child relationships.

        Parameters
        ----------
        old_limb : Node
            Node being replaced.
        new_limb : Node or None
            Replacement node.

        Returns
        -------
        None
        """
        # If old_limb was the root, the new_limb becomes the root
        if old_limb.parent is None:
            self.root = new_limb

        # Update the parent's pointer to the new child
        elif old_limb == old_limb.parent.left:
            old_limb.parent.left = new_limb
        else:
            old_limb.parent.right = new_limb

        # Update the new child's pointer back to the parent
        if new_limb:
            new_limb.parent = old_limb.parent

    def minimum(self, node):
        """
        Finds the node with the smallest bid_id in a subtree.

        Used when locating an in-order successor during deletion.

        Parameters
        ----------
        node : Node
            Root of subtree.

        Returns
        -------
        Node
            Node containing the minimum bid_id.
        """
        while node.left:
            node = node.left

        return node
    
    # -------------------------------- Searching ------------------------------
    def _search(self, bid_id):
        """
        Private search method.

        Searches for a Bid in the Red Black Tree by bid_id using an iterative approach.

        Parameters
        ----------
        bid_id : str
            The unique identifier of the Bid to search for.

        Returns
        -------
        Node or None
            The matching Node if found, otherwise None.

        Notes
        -----
        Average time complexity is O(log n)
        """
        current = self.root
        while current:
            if bid_id == current.bid.bid_id:
                return current  
            elif bid_id < current.bid.bid_id:
                current = current.left
            else:
                current = current.right
        return None  
    
    def search(self, bid_id):
        """
        Searches for a Bid in the Red Black Tree by bid_id.

        Parameters
        ----------
        bid_id : str
            Unique identifier of the Bid to locate.

        Returns
        -------
        Bid or None
            Matching Bid object if found, otherwise None.
        """
        node = self._search(bid_id)

        if node:
            return node.bid

        return None
    
    # ------------------------------ Traversals -------------------------------
    def in_order(self):
        """
        Performs an in-order traversal of the RBT.

        Visits nodes in ascending order of bid_id.
        """
        self._in_order(self.root)

    def pre_order(self):
        """
        Performs a pre-order traversal of the RBT.

        Visits the current node before its child nodes.
        """
        self._pre_order(self.root)

    def post_order(self):
        """
        Performs a post-order traversal of the RBT.

        Visits child nodes before the current node.
        """
        self._post_order(self.root)

    def _in_order(self, node):
        """
        Helper method for recursive in-order traversal.

        Parameters
        ----------
        node : Node or None
            The current node being processed.
        """
        if node:
            self._in_order(node.left)
            self.display_bid(node.bid)
            self._in_order(node.right)

    def _pre_order(self, node):
        """
        Helper method for recursive pre-order traversal.

        Parameters
        ----------
        node : Node or None
            The current node being processed.
        """
        if node:
            self.display_bid(node.bid)
            self._pre_order(node.left)
            self._pre_order(node.right)

    def _post_order(self, node):
        """
        Helper method for recursive post-order traversal.

        Parameters
        ----------
        node : Node or None
            The current node being processed.
        """
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            self.display_bid(node.bid)

    # ------------------------------ Destructor -------------------------------
    def destructor(self):
        """
        This breaks the reference to the root node,
        enabling pythons garbage collection to clean everything up
        """
        self.root = None

    # --------------------------- Displaying bids -----------------------------
    def display_bid(self, bid):
        """
        Displays a Bid's details to the console.

        Parameters
        ----------
        bid : Bid
            The Bid object to display.

        Returns
        -------
        None
        """
        print(f"{bid.bid_id}: {bid.title} | {bid.amount} | {bid.fund}")


# ======================================================
# CSV Loader (replacing CSVparcer.cpp and CSVparser.hpp)
# ======================================================
def load_bids(csv_path, bst):
    """
    Loads bid data from a CSV file into a Binary Search Tree.

    Each row in the CSV file is parsed into a Bid object and inserted
    into the provided BST.

    Parameters
    ----------
    csv_path : str
        The file path to the CSV file.
    bst : BST
        The Binary Search Tree where bids will be stored.

    Returns
    -------
    None
    """
    print(f"Loading CSV file {csv_path}")

    with open(csv_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        for h in header:
            print(h, "|", end=" ")
        print("\n")

        for row in reader:
            bid = Bid(
                bid_id=row[1],
                title=row[0],
                fund=row[8],
                amount=float(row[4].replace("$", "").replace(",", ""))
            )
            bst.insert(bid)

# ==========================
# Main Menu (C++ equivalent)
# ==========================
def main():
    """
    Entry point for the application.

    Provides a command-line interface for interacting with the BST,
    including loading data, displaying bids, searching, and removing entries.

    Returns
    -------
    None
    """
    csv_path = "./eBid_Monthly_Sales.csv"

    rbt = RBT()

    choice = 0
    while choice != 9:
        print("\nMenu:")
        print("  1. Load Bids")
        print("  2. Display All Bids (In-Order)")
        print("  3. Display All Bids (Pre-Order)")
        print("  4. Display All Bids (Post-Order)")
        print("  5. Find Bid")
        print("  6. Remove Bid")
        print("  7. Self Destruct (delete BST)")
        print("  9. Exit")

        while True:
            user_input = input("Enter choice: ")
            try:
                choice = int(user_input)
                break
            except ValueError:
                print("Invalid input. Please enter a number (1-7 or 9).")

        # -------- Load Bids --------
        if choice == 1:
            start = time.time()
            load_bids(csv_path, rbt)
            end = time.time()
            print(f"time: {(end - start):.6f} seconds")

        # -------- Display All Bids (In-Order)--------
        elif choice == 2:
            rbt.in_order()

        # -------- Display All Bids (Pre-Order)--------
        elif choice == 3:
            rbt.pre_order()

        # -------- Display All Bids (Post-Order)--------
        elif choice == 4:
            rbt.post_order()

        # -------- Find Bid --------
        elif choice == 5:
            bid_key = input("Enter Bid ID to search: ")
            start = time.time()
            bid = rbt.search(bid_key)
            end = time.time()

            if bid:
                rbt.display_bid(bid)
            else:
                print(f"Bid Id {bid_key} not found.")

            print(f"time: {(end - start):.6f} seconds")

        # -------- Remove Bid --------
        elif choice == 6:
            bid_key = input("Enter Bid ID to remove: ")
            rbt.remove(bid_key)
            print(f"Bid {bid_key} removed.")

        # ------- Self Destruct (Proof of Concept)------
        elif choice == 7:
            print("Destroying RBT")
            rbt.destructor()


    print("Good bye.")


if __name__ == "__main__":
    main()
