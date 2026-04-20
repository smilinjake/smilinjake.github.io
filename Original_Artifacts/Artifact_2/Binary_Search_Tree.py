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
    Represents a single node from on the BST

    Attributes
    ----------
    bid   : bid
        Bid attached to the Node. Essentially the value of the node. 
    left  : (Node, optional) 
        Left child Node of current node (bid.bid_id < current.bid.bid_id)
        
    right : (Node, optional) 
        Right child Node of current node (bid.bid_id > current.bid.bid_id)

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

# Implementing the Binary Search Tree non recursively for performance (an iterative approach)
class BST:
    """
    Binary Search Tree (BST) implementation for storing and managing Bid objects.

    The BST organizes Bid objects based on their bid_id values, allowing for
    efficient insertion, searching, deletion, and traversal operations.

    Attributes
    ----------
    root : Node or None
        The root node of the BST. None if the tree is empty.
    """
    def __init__(self):
        """
        Initializes BST with a root node or none

        Args: 
            root: node
        """
        self.root = None

    def insert(self, bid):
        """
        Inserts a Bid into the Binary Search Tree.

        The Bid is placed according to its bid_id value to maintain BST ordering:
        left subtree contains smaller bid_ids, right subtree contains larger or equal.

        Parameters
        ----------
        bid : Bid
            The Bid object to insert into the tree.

        Returns
        -------
        None
        """
        new_node = Node(bid)

        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        # checking where the new node belongs and inserting it 
        while True:
            if bid.bid_id < current.bid.bid_id:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
    
    def remove(self, bid_id):
        """
        Removes a Bid from the Binary Search Tree based on bid_id.

        This method updates the root of the tree after deletion.

        Parameters
        ----------
        bid_id : str
            The unique identifier of the Bid to remove.

        Returns
        -------
        None
        """
        self.root = self._remove_node(self.root, bid_id)

    def _remove_node(self, node, bid_id):
        """
        Recursively removes a node with the given bid_id from the subtree.

        Handles all three deletion cases:
        - Node with no children
        - Node with one child
        - Node with two children (for in-order successor replacement)

        Parameters
        ----------
        node : Node or None
            The current node in the recursion.
        bid_id : str
            The bid_id to remove.

        Returns
        -------
        Node or None
            The updated subtree root after deletion.
        """
        if node is None:
            return None

        if bid_id < node.bid.bid_id:
            node.left = self._remove_node(node.left, bid_id)
        elif bid_id > node.bid.bid_id:
            node.right = self._remove_node(node.right, bid_id)
        else:
            # Case 1: no children
            if node.left is None and node.right is None:
                return None

            # Case 2: one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: two children
            temp = node.right
            while temp.left:
                temp = temp.left

            node.bid = temp.bid
            node.right = self._remove_node(node.right, temp.bid.bid_id)

        return node

    # -------------------------------- Searching ------------------------------
    def search(self, bid_id):
        """
        Searches for a Bid in the BST by bid_id using an iterative approach.

        Parameters
        ----------
        bid_id : str
            The unique identifier of the Bid to search for.

        Returns
        -------
        Bid or None
            The matching Bid object if found, otherwise None.

        Notes
        -----
        Time complexity is O(h), where h is the height of the tree.
        """
        current = self.root
        while current:
            if bid_id == current.bid.bid_id:
                return current.bid  
            elif bid_id < current.bid.bid_id:
                current = current.left
            else:
                current = current.right
        return None  

    # ------------------------------ Traversals -------------------------------
    def in_order(self):
        """
        Performs an in-order traversal of the BST.

        Visits nodes in ascending order of bid_id.
        """
        self._in_order(self.root)

    def pre_order(self):
        """
        Performs a pre-order traversal of the BST.

        Visits the current node before its child nodes.
        """
        self._pre_order(self.root)

    def post_order(self):
        """
        Performs a post-order traversal of the BST.

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

    bst = BST()

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
            load_bids(csv_path, bst)
            end = time.time()
            print(f"time: {(end - start):.6f} seconds")

        # -------- Display All Bids (In-Order)--------
        elif choice == 2:
            bst.in_order()

        # -------- Display All Bids (Pre-Order)--------
        elif choice == 3:
            bst.pre_order()

        # -------- Display All Bids (Post-Order)--------
        elif choice == 4:
            bst.post_order()

        # -------- Find Bid --------
        elif choice == 5:
            bid_key = input("Enter Bid ID to search: ")
            start = time.time()
            bid = bst.search(bid_key)
            end = time.time()

            if bid:
                bst.display_bid(bid)
            else:
                print(f"Bid Id {bid_key} not found.")

            print(f"time: {(end - start):.6f} seconds")

        # -------- Remove Bid --------
        elif choice == 6:
            bid_key = input("Enter Bid ID to remove: ")
            bst.remove(bid_key)
            print(f"Bid {bid_key} removed.")

        # ------- Self Destruct (Proof of Concept)------
        elif choice == 7:
            print("Destroying BST")
            bst.destructor()


    print("Good bye.")


if __name__ == "__main__":
    main()
