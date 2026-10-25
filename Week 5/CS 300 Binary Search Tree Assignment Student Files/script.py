from docx import Document

doc = Document()
doc.add_heading('Code Reflection & Pseudocode', 0)

doc.add_heading('Code Reflection', level=1)
doc.add_paragraph("I approached this Binary Search Tree implementation similar to managing an Active Directory hierarchy. You need a data structure that naturally filters out half the remaining dataset with every step. By routing smaller bid IDs to the left and larger ones to the right, the search function operates at O(log n) time complexity. That drastically reduces the processing overhead compared to the linear search we used in the linked list. Searching over 12,000 records now executes in a fraction of a millisecond.")
doc.add_paragraph("The biggest challenge was handling the removal of a node with two children. It is exactly like swapping out a core network switch without dropping the live routing connections beneath it. You cannot just delete the target node, or you instantly orphan the entire sub-tree and create a massive memory leak. I solved this by finding the minimum value in the right sub-tree, copying that data up to replace the target node, and then recursively deleting the duplicate leaf node further down the chain. This preserves the strict ordering of the tree while freeing the correct block of memory.")

doc.add_heading('Pseudocode', level=1)
pseudo = """CLASS BinarySearchTree
    Initialize root = null

    METHOD Insert(bid)
        IF root is null THEN
            root = Create Node(bid)
        ELSE
            addNode(root, bid)

    METHOD addNode(node, bid)
        IF bid.bidId < node.bidId THEN
            IF node.left is null THEN
                node.left = Create Node(bid)
            ELSE
                addNode(node.left, bid)
        ELSE
            IF node.right is null THEN
                node.right = Create Node(bid)
            ELSE
                addNode(node.right, bid)

    METHOD Search(bidId)
        current = root
        WHILE current is not null
            IF current.bidId == bidId THEN
                RETURN current.bid
            IF bidId < current.bidId THEN
                current = current.left
            ELSE
                current = current.right
        RETURN empty bid

    METHOD Remove(bidId)
        root = removeNode(root, bidId)

    METHOD removeNode(node, bidId)
        IF node is null THEN RETURN node
        
        IF bidId < node.bidId THEN
            node.left = removeNode(node.left, bidId)
        ELSE IF bidId > node.bidId THEN
            node.right = removeNode(node.right, bidId)
        ELSE
            IF node.left is null AND node.right is null THEN
                DELETE node
                RETURN null
            ELSE IF node.left is not null AND node.right is null THEN
                temp = node.left
                DELETE node
                RETURN temp
            ELSE IF node.left is null AND node.right is not null THEN
                temp = node.right
                DELETE node
                RETURN temp
            ELSE
                temp = node.right
                WHILE temp.left is not null
                    temp = temp.left
                node.bid = temp.bid
                node.right = removeNode(node.right, temp.bidId)
        
        RETURN node"""

doc.add_paragraph(pseudo)

doc.save('BinarySearchTree_Reflection_Pseudocode.docx')
print("Document generated successfully.")
