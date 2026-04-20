smilinjake.github.io
ePortfolio for SNHU CS-499 Capstone

[View My Github Profile](https://github.com/smilinjake)
[Code Review Link](https://github.com/smilinjake/smilinjake.github.io/releases/tag/Code_Review_Video)

## Table of Contents

- [Code Review Video](https://github.com/smilinjake/smilinjake.github.io/releases/tag/Code_Review_Video)
- [Artifact 1 Narrative](Narratives/Artifact_1_Narrative.pdf)
- [Artifact 2 Narrative](Narratives/Artifact_2_Narrative.pdf)
- [Artifact 3 Narrative](Narratives/Artifact_3_Narrative.pdf)
- [Artifact 1 original artifact](Original_Artifacts/Artifact_1/CS%20300%20Binary%20Search%20Tree%20Assignment/BinarySearchTree.cpp)
- [Artifact 1 improved artifact](Improved_Artifacts/Improved_Artifact_1/CS_499_Milestone_2_Assignment/Binary_Search_Tree.py)
- [Artifact 2 original artifact](Original_Artifacts/Artifact_2/Binary_Search_Tree.py)
- [Artifact 2 improved artifact](Improved_Artifacts/Improved_Artifact_2/Red_Black_Tree.py)
- [Artifact 3 original artifact](Original_Artifacts/Artifact_3/CRUD_Python_Module.py)
- [Artifact 3 improved artifact](Improved_Artifacts/Improved_Artifact_3/)

## Professional Self-Assessment

Completing the SNHU Computer Science program and developing this ePortfolio has helped me showcase strengths in technical problem solving, software design, and effective communication. Through coursework and projects, I have built confidence collaborating in team environments, speaking clearly with stakeholders, and applying data structures and algorithms to real problems.

Recently at work as a full stack python developer, I communicated with the C-Suite to develop a new workflow to show new information on our customers within the Odoo 12 environment using the Heron Api Enricher endpoints. I would not have been able to efficiently create this new workflow without the SNHU Computer Science Program preparing me to speak to corporate executives without using technical jargon. This enabled me to develop and actually contribute in a large way to the product repo at the company that I work for.

In team settings, I learned to coordinate work, share responsibilities, and keep projects moving forward while respecting deadlines. Communicating with stakeholders became a regular part of class projects and capstone planning, where I translated technical ideas into practical solutions and explained trade-offs clearly.

The SNHU curriculum reinforced my understanding of data structures and algorithms, from binary search trees and self-balancing trees to efficient search and sort techniques. Software engineering and database work appeared across multiple courses, helping me design maintainable systems and integrate backend APIs with data storage. I also developed a stronger awareness of security practices, especially around protecting access to application data and using authentication in web-based projects.

This portfolio brings those strengths together through three artifacts. Each artifact reflects different areas of my skill set: algorithmic design and translation between languages, advanced tree structures and performance improvements, and full stack development with backend APIs and frontend integration. Together, they provide a complete view of my technical abilities and prepare me for professional roles in computer science.

# Artifact Portfolio Overview

## Artifact 1

### Original Artifact

The original artifact for this milestone was the BinarySearchTree.cpp. It was an implementation of a binary search tree in the C++ language. The program was designed to utilize a CSV parser to read the lines of a csv document and, in tandem with the binary search tree implementation, organize them in a binary search tree data structure. The artifact was also created with an interactive menu to perform searches, deletions, and printing the data in various ways (which were not connected on the menu). It was created for an assignment in my data structures and algorithms class in 2025.

### Justification and Improvement

I selected this artifact so that I could meet the CS 499 outcome, “Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices (data structures and algorithms)” for the, “Software Design and Engineering” section of the capstone project. This was done by translating the artifact to the Python language, as well as implementing the CSVparser to demonstrate its successful translation. I improved the artifact by adding additional options to the user command prompt menu for the differing methods of BST traversals for printing. I also removed the hard coding of bid removals and searches. In addition to these improvements, I added input validation to the command line interface user prompt. Also while it was not necessary as python has automatic garbage collection, I added a “self destruct” option to the menu to demonstrate the destructor added to the pythonic BST that was not implemented in the original artifact.

### Course Outcomes and Reflection

I did meet the course outcome, “Category One - Software Design and Engineering: Performs planned enhancements to artifact and develops an accompanying narrative that explains why the artifact was selected and the skills showcased in the enhancement.”. I opted to perform an iterative approach to the BST instead of a recursive approach, as the recursive implementations can quickly overwhelm lower grade computers due to limited resources on stack and heap sizes. This is not normally an issue, but if the CSV that we would be interacting with was sufficiently large, it would error out with the recursive insertion approach.

I also touched on the concept “Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals (software engineering/design/database)” by adding well rounded docstrings in the PEP-8 standard to increase the modules readability, and to bring the document up to professional standards. Also by implementing a more robust input validation, the program no longer breaks when faced with input types that are not expected for user choices. This new version also takes advantage of built in python libraries like csv to enable our program to read in lines from the external csv. This aided greatly in the implementation of the CSVparser method that was given to us by the instructor in C++ code for the original assignment.

The biggest challenge in this milestone was implementing the CSVparser section. This was previously just given to us by our instructor and was not intended for us to ever need to adjust. It was purposefully left obfuscated to the students as tinkering with it was not necessary or in bounds for the original Data Structures and Algorithms course.

I did however learn a lot about documentation for this milestone, aligning with the course outcomes related to software engineering/design. This deep dive on PEP-8 standards really helped me look at and learn the nuances of docstrings for pythonic coding and method documentation. This works well in alignment with current code IDEs like vscode (my favorite) because the IDEs natively understand this format and add it to the on-hover functionality of variables and methods in the code. This means that when someone is reviewing or reading my code, all they need to do for an explanation of the return type, arguments, or attributes of classes and methods, is to hover over the artifact in question. Compared to my previous code which was only explained by poor commenting, this method of documentation is on par with my own work in my career as a python developer.

### Links

- Original artifact: [BinarySearchTree.cpp](Original_Artifacts/Artifact_1/CS%20300%20Binary%20Search%20Tree%20Assignment/BinarySearchTree.cpp)
- Improved artifact: [Binary_Search_Tree.py](Improved_Artifacts/Improved_Artifact_1/CS_499_Milestone_2_Assignment/Binary_Search_Tree.py)

## Artifact 2

### Original Artifact

The artifact that I used for this assignment is a Binary Search Tree in python. It was created for my previous milestone as a translation to python from an older C++ project. This artifact had to handle multiple different jobs that previously took multiple different C++ files to accomplish. These were a csv reader that enabled the BST to interact with a csv to organize and display data, as well as a main menu that is interactive on the command line.

### Justification and Improvement

I selected this item because for the second and third milestones I wanted to take a single project, translate it, and then make it more efficient through algorithmic processes and refinement. In this case, the project was improved by taking the Binary Search Tree and creating a Red Black Tree instead. This is a much more efficient tree, but it is a much more complicated tree as well. The time complexity of the original artifact was improved by this tree swap significantly. A BST has a worst case of linear or 0(n) time complexity, whereas the RBT has a worst case time complexity of O(log n) or logarithmic time complexity. This is due to the fact that the RBT is a self correcting and self balancing version of a BST. It operates in pretty much the same way, but the removal and insertion processes have additional helper functions to rotate and balance the does after standard operations are done on the tree.

### Course Outcomes and Reflection

I did meet the course outcomes that I planned on meeting with this enhancement in Module one. The course outcomes from Module One that I forecasted would be met in this current module were the following:

#3 - Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution while managing the trade-offs involved in design choices.
#4 - Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals.

As I was creating and improving the artifact for this module, I learned that I was completely underprepared for the complexity of a Red Black Tree. The self balancing and self repairing properties of this tree are accomplished through the red and black labels placed onto the nodes of the tree as well as the rotation processes that help correct the tree after a node is inserted or removed. I faced significant logical challenges in the creation of this implementation. Due to the complexity of these methods and helper functions, I had to provide extensive commenting to help sort out the dense nature of the methods for readers, reviewers, and myself after I have forgotten the implementation, to help everyone understand what is actually happening.

### Links

- Original artifact: [Binary_Search_Tree.py](Original_Artifacts/Artifact_2/Binary_Search_Tree.py)
- Improved artifact: [Red_Black_Tree.py](Improved_Artifacts/Improved_Artifact_2/Red_Black_Tree.py)

## Artifact 3

### Original Artifact

The artifact that I used for this assignment was CRUD_Python_Module.py. It was the crud module for a python api for a project that I created last year in SNHU CS-340. The main problem with this artifact is that it would not run on its own. I originally created the assignment using apporto, a virtual web hosting environment used by SNHU so that students could work on full stack projects for school while only needing to implement the targeted areas in specific files. So I had to create the full stack for this project to just utilize the CRUD module artifact that I needed. I ended up using Create React App for the frontend, FastAPI and MongoDB for the database and backend, and some additional python files to implement the authentication and login/logout workflows.

### Justification and Improvement

I selected this item because it demonstrates my ability to work across multiple layers of a modern software system instead of focusing on only one component. This artifact showcases my skills in backend API development using FastAPI, frontend interaction using React, and database integration using MongoDB. It also demonstrates my ability to organize CRUD operations in a scalable structure that separates responsibilities between the frontend interface and backend logic.
The artifact was improved by restructuring the original database interaction logic into reusable FastAPI routes and connecting those routes to a React interface that allows users to interact with the system dynamically through a browser. I also incorporated authentication logic so that only authorized users are able to access protected endpoints and to complete my projected enhancements that I forecasted in module one. These improvements made the project more secure, more modular, and closer to what would be expected in a real world software development environment.

### Course Outcomes and Reflection

I did meet the course outcomes that I planned on meeting with this enhancement in Module One. The course outcomes from Module One that I forecasted would be met in this current module were the following:

#3 – Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution while managing the trade-offs involved in design choices.

#4 – Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals.

This artifact directly supports these outcomes because it required designing a structured API architecture, organizing database operations efficiently, and integrating multiple technologies together into one working application. At this time, no additional updates to my outcome coverage plans are needed.

As I was creating and improving the artifact for this module, I learned more about how frontend and backend systems communicate through API routes and how authentication can be incorporated into an existing CRUD application structure. I also gained additional experience working with MongoDB collections outside of the Apporto environment and configuring the application to run locally on my own system.
One challenge that I faced during this enhancement process was restructuring the original CS-340 project so that it could operate as a full FastAPI service instead of running only inside the virtual course environment. This required extensive troubleshooting from database connection issues, route handling logic, and ensuring that authentication worked correctly across protected endpoints. Working through these challenges improved my understanding of full stack system integration and strengthened my ability to debug issues across multiple components of an application.

### Links

- Original artifact: [CRUD_Python_Module.py](Original_Artifacts/Artifact_3/CRUD_Python_Module.py)
- Improved artifact: [Improved_Artifact_3 folder](Improved_Artifacts/Improved_Artifact_3/)
