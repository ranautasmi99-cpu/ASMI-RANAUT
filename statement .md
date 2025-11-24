# Project Statement

## Project Title
**Student Record Management System**

## Problem Statement
Managing student records manually is slow and error-prone. When information is kept on paper or in unstructured files, searching for a student, updating details, or ensuring consistency becomes time consuming and unreliable. This project builds a lightweight command-line application in Python that stores student records in a JSON file and provides simple, reliable operations to add, view, search, update, and delete records.

## Scope
This project focuses on the core needs of small-scale academic record keeping:
- Storing basic student details (ID, name, branch, year) persistently.
- Providing a clear menu-driven interface for common operations.
- Ensuring input validation and safe file handling to prevent data corruption.
- Producing documentation and diagrams suitable for academic submission.

Out-of-scope (for this version):
- Web or mobile front-end (can be added later).
- Multi-user authentication and access control.
- Large-scale database optimizations (SQL/NoSQL).

## Target Users
- Instructors and assistant staff who need a simple tool for small batches of students.  
- Students learning programming concepts (file I/O, modular design).  
- Any small educational unit (tutorial groups, labs, coaching centers) that does not require a full database-backed system.

## High-level Features
1. **Add Student** — Enter and save a new student record with a unique ID.  
2. **View All Students** — List all stored records in a readable format.  
3. **Search Student** — Find a student by their ID and display full details.  
4. **Update Student** — Edit name, branch, or year for an existing record.  
5. **Delete Student** — Remove a record permanently after confirmation.  
6. **Persistent Storage** — All records are kept in `data.json` so data is retained between program runs.  
7. **Input Validation** — Prevents empty fields and invalid numeric input.  
8. **Simple Structure** — Code split into small modules (main controller, validation helpers, file operations) to make it easy to read and maintain.






