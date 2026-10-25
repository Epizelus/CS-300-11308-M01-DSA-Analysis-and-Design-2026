#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

// Define a structure to hold course information
struct Course {
    string courseNumber;
    string title;
    vector<string> prerequisites;
};

// Create the structure of the binary tree node
struct TreeNode {
    Course course;
    TreeNode* left;
    TreeNode* right;

    // Default constructor
    TreeNode() {
        left = nullptr;
        right = nullptr;
    }

    // Initialize with a course
    TreeNode(Course aCourse) : TreeNode() {
        course = aCourse;
    }
};

// Binary Search Tree Class
class BinarySearchTree {
private:
    TreeNode* root;

    void addNode(TreeNode* node, Course course) {
        // Traverse left or right based on alphanumeric order
        if (course.courseNumber < node->course.courseNumber) {
            if (node->left == nullptr) {
                node->left = new TreeNode(course);
            }
            else {
                addNode(node->left, course);
            }
        }
        else {
            if (node->right == nullptr) {
                node->right = new TreeNode(course);
            }
            else {
                addNode(node->right, course);
            }
        }
    }

    void inOrder(TreeNode* node) {
        if (node != nullptr) {
            inOrder(node->left);
            cout << node->course.courseNumber << ", " << node->course.title << endl;
            inOrder(node->right);
        }
    }

    // Destructor helper to clear memory
    void destroyTree(TreeNode* node) {
        if (node != nullptr) {
            destroyTree(node->left);
            destroyTree(node->right);
            delete node;
        }
    }

public:
    BinarySearchTree() {
        root = nullptr;
    }

    ~BinarySearchTree() {
        destroyTree(root);
    }

    void Insert(Course course) {
        if (root == nullptr) {
            root = new TreeNode(course);
        }
        else {
            addNode(root, course);
        }
    }

    void PrintInOrder() {
        inOrder(root);
    }

    Course Search(string courseNumber) {
        TreeNode* current = root;
        while (current != nullptr) {
            if (current->course.courseNumber == courseNumber) {
                return current->course;
            }
            else if (courseNumber < current->course.courseNumber) {
                current = current->left;
            }
            else {
                current = current->right;
            }
        }
        // Return an empty course if not found
        Course emptyCourse;
        return emptyCourse;
    }
};

// Print the details of a single course
void printCourseDetails(Course course) {
    cout << course.courseNumber << ", " << course.title << endl;
    cout << "Prerequisites: ";

    if (course.prerequisites.empty()) {
        cout << "None" << endl;
    }
    else {
        for (size_t i = 0; i < course.prerequisites.size(); ++i) {
            cout << course.prerequisites[i];
            if (i < course.prerequisites.size() - 1) {
                cout << ", ";
            }
        }
        cout << endl;
    }
}

// Load data from file into the Binary Search Tree
void loadCoursesFromFile(string filename, BinarySearchTree* bst) {
    ifstream file(filename);

    if (!file.is_open()) {
        cerr << "Error: Unable to open file " << filename << endl;
        return;
    }

    string currentLine;
    int loadCount = 0;

    while (getline(file, currentLine)) {
        // Trim whitespace and carriage returns
        currentLine.erase(0, currentLine.find_first_not_of(" \t\n\r\f\v"));
        currentLine.erase(currentLine.find_last_not_of(" \t\n\r\f\v") + 1);

        if (currentLine.empty()) {
            continue;
        }

        stringstream ss(currentLine);
        string token;
        vector<string> tokens;

        while (getline(ss, token, ',')) {
            token.erase(0, token.find_first_not_of(" \t\n\r\f\v"));
            token.erase(token.find_last_not_of(" \t\n\r\f\v") + 1);
            tokens.push_back(token);
        }

        // Validation check: line must contain at least course number and course title
        if (tokens.size() < 2) {
            cerr << "Format Error: Line contains fewer than 2 parameters: " << currentLine << endl;
            continue; // Skip bad line but keep loading the rest of the file
        }

        Course newCourse;
        newCourse.courseNumber = tokens[0];
        newCourse.title = tokens[1];

        for (size_t i = 2; i < tokens.size(); i++) {
            if (!tokens[i].empty()) {
                newCourse.prerequisites.push_back(tokens[i]);
            }
        }

        bst->Insert(newCourse);
        loadCount++;
    }

    file.close();
    cout << "Data successfully loaded into the Binary Search Tree (" << loadCount << " courses)." << endl;
}

// Convert string to uppercase for case-insensitive searching
string toUpper(string str) {
    transform(str.begin(), str.end(), str.begin(), ::toupper);
    return str;
}

int main() {
    BinarySearchTree* courseTree = new BinarySearchTree();
    int choice = 0;
    string filename;
    string targetCourse;
    bool dataLoaded = false;

    cout << "Welcome to the ABCU Academic Advising Course Planner." << endl;

    while (choice != 9) {
        cout << "\n  1. Load Data Structure." << endl;
        cout << "  2. Print Course List." << endl;
        cout << "  3. Print Course." << endl;
        cout << "  9. Exit" << endl;
        cout << "\nWhat would you like to do? ";

        if (!(cin >> choice)) {
            cin.clear();
            cin.ignore(10000, '\n');
            cout << "Invalid input. Please enter a number." << endl;
            continue;
        }

        switch (choice) {
        case 1:
            cout << "Enter course data file name (e.g., CS 300 ABCU_Advising_Program_Input.csv): ";
            cin.ignore();
            getline(cin, filename);

            // Allow a quick default load for testing purposes
            if (filename.empty()) {
                filename = "CS 300 ABCU_Advising_Program_Input.csv";
            }

            loadCoursesFromFile(filename, courseTree);
            dataLoaded = true;
            break;

        case 2:
            if (!dataLoaded) {
                cout << "Error: No course data loaded. Please select Option 1 first." << endl;
            }
            else {
                cout << "Here is a sample schedule:" << endl;
                courseTree->PrintInOrder(); // Native BST in-order prints alphabetically automatically
            }
            break;

        case 3:
            if (!dataLoaded) {
                cout << "Error: No course data loaded. Please select Option 1 first." << endl;
            }
            else {
                cout << "What course do you want to know about? ";
                cin >> targetCourse;
                targetCourse = toUpper(targetCourse);

                Course foundCourse = courseTree->Search(targetCourse);

                if (!foundCourse.courseNumber.empty()) {
                    printCourseDetails(foundCourse);
                }
                else {
                    cout << "Error: Course " << targetCourse << " not found." << endl;
                }
            }
            break;

        case 9:
            cout << "Thank you for using the course planner!" << endl;
            break;

        default:
            cout << choice << " is not a valid option. Please choose 1, 2, 3, or 9." << endl;
            break;
        }
    }

    // Clean up memory before exiting
    delete courseTree;
    return 0;
}