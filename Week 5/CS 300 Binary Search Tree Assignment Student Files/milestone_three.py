from docx import Document

doc = Document()
doc.add_heading('CS 300 Project One Milestone Three: Binary Search Tree Pseudocode', 0)

doc.add_heading('1. Data Structure Definitions', level=1)
ds_text = """STRUCTURE Course
    String courseNumber
    String title
    LIST of String prerequisites
END STRUCTURE

STRUCTURE Node
    Course course
    Node left
    Node right
END STRUCTURE

STRUCTURE BinarySearchTree
    Node root

    METHOD Insert(course)
        IF root is null THEN
            root = Create Node(course)
        ELSE
            addNode(root, course)

    METHOD addNode(node, course)
        IF course.courseNumber < node.course.courseNumber THEN
            IF node.left is null THEN
                node.left = Create Node(course)
            ELSE
                addNode(node.left, course)
        ELSE
            IF node.right is null THEN
                node.right = Create Node(course)
            ELSE
                addNode(node.right, course)

    METHOD Search(courseNumber)
        current = root
        WHILE current is not null
            IF current.course.courseNumber EQUALS courseNumber THEN
                RETURN current.course
            IF courseNumber < current.course.courseNumber THEN
                current = current.left
            ELSE
                current = current.right
        RETURN empty course

    METHOD GetAllCourses(node, list)
        // In-order traversal helper to retrieve all courses for validation
        IF node is not null THEN
            GetAllCourses(node.left, list)
            ADD node.course TO list
            GetAllCourses(node.right, list)
END STRUCTURE"""
doc.add_paragraph(ds_text)

doc.add_heading('2. File Ingestion and Format Validation', level=1)
ingest_text = """FUNCTION loadCourseData(String fileName) RETURNS BinarySearchTree
    INITIALIZE BinarySearchTree bst

    OPEN file from fileName
    IF file fails to open THEN
        PRINT "Error: Unable to open file."
        RETURN empty tree
    END IF

    // First Pass: Read data, parse lines, and validate basic format
    WHILE NOT end of file
        READ currentLine FROM file
        TRIM whitespace from currentLine
        
        IF currentLine is empty THEN
            CONTINUE to next line
        END IF

        SPLIT currentLine by comma delimiter INTO tokens list

        // Validation Rule 1: Each line must have at least 2 parameters
        IF length of tokens < 2 THEN
            PRINT "Format Error: Line contains fewer than 2 parameters: " + currentLine
            CLOSE file
            RETURN empty tree
        END IF

        CREATE Course newCourse
        newCourse.courseNumber = TRIM(tokens[0])
        newCourse.title = TRIM(tokens[1])

        // Add optional prerequisites if present
        FOR i FROM 2 TO length of tokens - 1
            String prereq = TRIM(tokens[i])
            IF prereq is not empty THEN
                ADD prereq TO newCourse.prerequisites
            END IF
        END FOR

        bst.Insert(newCourse)
    END WHILE

    CLOSE file

    // Validation Rule 2: Verify every prerequisite exists as a defined course
    INITIALIZE empty list allCourses
    bst.GetAllCourses(bst.root, allCourses)
    
    FOR EACH course IN allCourses
        FOR EACH prereq IN course.prerequisites
            Course foundCourse = bst.Search(prereq)
            IF foundCourse is empty THEN
                PRINT "Validation Error: Prerequisite " + prereq + " for course " + course.courseNumber + " does not exist in the curriculum."
                RETURN empty tree
            END IF
        END FOR
    END FOR

    PRINT "Successfully loaded and validated courses."
    RETURN bst
END FUNCTION"""
doc.add_paragraph(ingest_text)

doc.add_heading('3. Search and Print Course Information', level=1)
search_text = """FUNCTION searchCourse(BinarySearchTree bst, String targetCourseNumber)
    // Perform O(log n) lookup using the binary search tree
    Course foundCourse = bst.Search(targetCourseNumber)

    IF foundCourse is not empty THEN
        PRINT foundCourse.courseNumber + ", " + foundCourse.title

        IF foundCourse.prerequisites is empty THEN
            PRINT "Prerequisites: None"
        ELSE
            PRINT "Prerequisites:"
            FOR EACH prereqNumber IN foundCourse.prerequisites
                // Secondary lookup to grab the prerequisite's full title
                Course prereqCourse = bst.Search(prereqNumber)
                
                IF prereqCourse is not empty THEN
                    PRINT "  " + prereqNumber + ", " + prereqCourse.title
                ELSE
                    PRINT "  " + prereqNumber
                END IF
            END FOR
        END IF
        
        RETURN
    END IF

    PRINT "Error: Course " + targetCourseNumber + " not found."
END FUNCTION"""
doc.add_paragraph(search_text)

doc.add_heading('4. Design Summary', level=1)
summary_text = (
    "Structuring this curriculum data in a Binary Search Tree works exactly like subnetting a massive network. "
    "Every time you move left or right down the tree, you instantly cut the remaining search space in half. "
    "The file ingestion logic parses the comma-separated values and immediately drops any line failing the two-parameter minimum requirement. "
    "During the secondary validation pass, we have to verify that every single listed prerequisite actually maps to a real course. "
    "If we used a standard vector, that validation loop would cause a massive bottleneck as the dataset scales. "
    "By utilizing the BST, the Search function hits O(log n) time complexity, ensuring the prerequisite validation remains incredibly fast. "
    "When a user searches for a course, the program navigates the nodes to instantly pull the core data and performs rapid secondary searches to print the full titles of any attached prerequisites."
)
doc.add_paragraph(summary_text)

doc.save('CS300_Milestone_Three_BST_Pseudocode.docx')
print("Milestone Three BST document generated successfully.")
