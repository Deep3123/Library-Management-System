# Library Management System 📚

## Objective 🧐
The Library Management System is a simple Python-based application designed to manage a collection of books. It allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books.

## Requirements ✅
### 1. Add Books 📖
- Users should be able to add new books to the library.
- Each book should have a unique identifier (e.g., ISBN), title, author, and publication year.

### 2. Borrow Books 📚
- Users should be able to borrow a book from the library.
- The system should ensure that the book is available before allowing it to be borrowed.
- If the book is not available, the system should raise an appropriate error.

### 3. Return Books 🔄
- Users should be able to return a borrowed book.
- The system should update the availability of the book accordingly.

### 4. View Available Books 👀
- Users should be able to view a list of all available books in the library.

## Technology ⚙️

This project is developed using the following technologies:

- **Python**: The main programming language used for logic and functionality.
- **Pytest**: A testing framework used to ensure code reliability through unit tests.
- **Git**: Version control for tracking changes and collaboration.

## Getting Started 🚀

### Prerequisites 📋
- Python 3.6 or higher
- `pytest` for running tests

### Installation 🔧
1. Clone the repository:
   ```shell
   git clone https://github.com/Deep3123/Library-Management-System
   cd library-management-system

2. Install dependencies (if any):
    ```shell
    pip install -r requirements.txt

### Running the Application ▶️
As this is a code-only project, there is no user interface. To run the application, execute the Python files directly in your terminal or use an IDE like VS Code.

### Running Tests 🧪
- To run the test suite, use pytest:
   ```shell
   pytest

### Features Implemented 🌟
- Add Books: Adds a new book to the library's collection.
- Borrow Books: Allows a user to borrow a book if it is available.
- Return Books: Allows a user to return a borrowed book.
- View Available Books: Lists all books that are currently available in the library.

### Additional Features 💡
- Validation: The Book class ensures that all required parameters (ISBN, Title, Author,   Year) are provided when creating a new book.
- Error Handling: Proper error handling for cases like borrowing a non-existent or    unavailable book.

## Git Repository 🗂️
Find the source code and all commits in the Git repository here: https://github.com/Deep3123/Library-Management-System

## Test Report 📝
A detailed test report showing the results of all test cases is included in the repository(report.xml).

## Contact 📫
For any questions, feedback, or issues, please feel free to reach out:

- Email: deepp3123@gmail.com
- GitHub Profile: Deep3123
- Portfolio: https://portfolioatdeep.onrender.com/