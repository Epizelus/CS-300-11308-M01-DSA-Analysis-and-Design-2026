# CS-300-11308-M01-DSA-Analysis-and-Design-2026

# Project Portfolio ReflectionWhat was the problem you were solving in the projects for this course?

The goal of this project was to design and build a command-line academic advising assistance program for ABCU. The software needed to ingest a CSV file containing course data and prerequisites, store that data efficiently in memory, and provide advisors with an interactive menu to print a sorted catalog and search for specific course details.

# How did you approach the problem? Consider why data structures are important to understand.

I approached the problem by first analyzing the Big O runtime and memory trade-offs of three candidate data structures: Vectors, Hash Tables, and Binary Search Trees (BST). I ultimately selected the BST because it perfectly aligned with the software's operational goals. While a Hash Table offered fast insertions, it lacked inherent order and would require expensive sorting algorithms to print the catalog. The BST naturally maintained an alphanumeric order for effortless O(n) in-order printing while simultaneously offering efficient O(log n) search times for individual course lookups. This highlighted how choosing the right data structure isn't just about syntax; it dictates the fundamental performance constraints of the software.

# How did you overcome any roadblocks you encountered while going through the activities or project?

One significant logic roadblock I hit was a timing bug during file ingestion. I initially placed my secondary prerequisite validation check inside the main file-reading loop, which caused the program to falsely flag missing prerequisites because the entire catalog hadn't been loaded into memory yet. I overcame this by stepping back, mapping out the physical execution timeline, and successfully separating the ingestion logic from the validation passes. On the syntax side, I overcame C++ hurdles (like resolving nested function errors and managing manual memory with pointers) by learning to rely on official documentation (like cppreference) and tracing return types rather than guessing methods.

# How has your work on this project expanded your approach to designing software and developing programs?

This project shifted my mindset from writing basic, top-to-bottom scripts to thinking about modular, object-oriented systems engineering. By designing a custom BinarySearchTree class and writing my own destructors, I gained a deeper appreciation for manual memory management and pointer manipulation. I also learned to view code mathematically, understanding how nested loops and recursive tree traversals directly impact computational cost.

# How has your work on this project evolved the way you write programs that are maintainable, readable, and adaptable?
I have become highly deliberate about isolating responsibilities within my code. Rather than cramming CSV parsing, validation, and tree insertion into one massive block, I learned to structure my program into distinct phases. Furthermore, I improved my use of in-line comments to explain why a block of code exists (e.g., explaining the need to left-trim and right-trim whitespace from text tokens) rather than just stating what it does. Moving away from heavy standard library dependencies in favor of clean, custom class architecture has made my code much more adaptable for future updates.
