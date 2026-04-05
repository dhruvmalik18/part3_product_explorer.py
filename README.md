Product Explorer & Error-Resilient Logger

This project is part of a Python assignment where I worked on file handling, API integration, exception handling, and logging.

The goal was to build something that behaves like a small real-world script — reading/writing files, fetching data from an API, handling errors properly, and keeping logs.

---

🚀 Features

1. File Handling

- Writes some basic Python notes into a file ("python_notes.txt")
- Appends a few extra lines
- Reads the file and prints each line with numbering
- Allows user to search for a keyword in the file

---

2. API Integration

- Fetches product data from a public API (DummyJSON)
- Displays product details like ID, title, price, and rating
- Filters products with rating ≥ 4.5
- Sorts them by price (high to low)
- Fetches laptop category products separately
- Simulates adding a product using a POST request

---

3. Exception Handling

- Safe division function that handles:
  - Division by zero
  - Invalid input types
- Safe file reader that:
  - Handles missing files
  - Uses "finally" block to confirm execution

---

4. Logging System

- Logs errors into a file ("error_log.txt")
- Each log entry includes:
  - Timestamp
  - Function name
  - Error message
- Demonstrates:
  - Connection error
  - HTTP error (404)

---

🛠️ Technologies Used

- Python 3
- requests library
- datetime module

---

▶️ How to Run

1. Install dependencies:
   
   pip install requests

2. Run the script:
   
   python part3_product_explorer.py

---

📂 Files

- "part3_product_explorer.py" → Main script
- "python_notes.txt" → Generated file for notes
- "error_log.txt" → Stores error logs

---

💡 Note

This project focuses more on understanding concepts than writing perfect production-level code.
Some parts are intentionally simple to keep things easy to follow.

---

👨‍💻 Author

Dhruv Malik

---