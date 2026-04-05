import requests
from datetime import datetime

# ------------------ TASK 1: FILE WORK ------------------ #

def manage_notes():
    file_name = "python_notes.txt"

    # write mode
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
        f.write("Topic 2: Lists are ordered and mutable.\n")
        f.write("Topic 3: Dictionaries store key-value pairs.\n")
        f.write("Topic 4: Loops automate repetitive tasks.\n")
        f.write("Topic 5: Exception handling prevents crashes.\n")

    print("Notes likh diye bhai 👍")

    # append mode
    with open(file_name, "a", encoding="utf-8") as f:
        f.write("Topic 6: APIs let us fetch real world data.\n")
        f.write("Topic 7: Logging helps track issues.\n")

    print("Extra lines add kar di 👍")

    # read + numbered
    print("\n📖 File content:\n")
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")

        print(f"\nTotal lines: {len(lines)}")

        keyword = input("\nKeyword enter kar: ")
        found = False

        for line in lines:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True

        if not found:
            print("Koi match nahi mila bhai 😅")

    except FileNotFoundError:
        print("File nahi mili bhai ❌")


# ------------------ TASK 2: API ------------------ #

BASE_URL = "https://dummyjson.com/products"

def fetch_products():
    try:
        response = requests.get(BASE_URL + "?limit=20", timeout=5)
        data = response.json()
        return data["products"]

    except requests.exceptions.ConnectionError:
        print("Internet issue bhai ❌")
        return []

    except requests.exceptions.Timeout:
        print("Request slow ho gaya ⏳")
        return []

def display_products(products):
    print("\nID | Title | Category | Price | Rating")
    print("-" * 60)

    for p in products:
        print(f"{p['id']} | {p['title']} | {p['category']} | ${p['price']} | {p['rating']}")

def filter_sort(products):
    result = []

    for item in products:
        if item["rating"] >= 4.5:
            result.append(item)

    result.sort(key=lambda x: x["price"], reverse=True)

    return result

def search_category():
    try:
        response = requests.get(BASE_URL + "/category/laptops", timeout=5)
        data = response.json()

        print("\n💻 Laptops:\n")
        for item in data["products"]:
            print(item["title"], "-", item["price"])

    except Exception as e:
        print("Error:", e)

def add_product():
    try:
        new_product = {
            "title": "My Custom Product",
            "price": 999,
            "category": "electronics",
            "description": "A product I created via API"
        }

        response = requests.post(BASE_URL + "/add", json=new_product)
        print("\nPOST Response:")
        print(response.json())

    except Exception as e:
        print("Error:", e)


# ------------------ TASK 3: EXCEPTION ------------------ #

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: divide by zero"
    except TypeError:
        return "Error: invalid input"


def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"{filename} nahi mila ❌")
    finally:
        print("File check complete ✔️")


# ------------------ TASK 4: LOGGING ------------------ #

def log_error(message):
    with open("error_log.txt", "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] ERROR: {message}\n")


def test_logging():
    # force connection error
    try:
        requests.get("https://this-does-not-exist.xyz")
    except Exception as e:
        log_error(str(e))

    # force 404
    response = requests.get(BASE_URL + "/9999")
    if response.status_code != 200:
        log_error(f"HTTP Error {response.status_code}")

    print("\n📜 Error Log:\n")
    with open("error_log.txt", "r") as f:
        print(f.read())


# ------------------ MAIN ------------------ #

if __name__ == "__main__":
    manage_notes()

    products = fetch_products()
    display_products(products)

    filtered = filter_sort(products)

    print("\n⭐ Filtered Products (rating >= 4.5):\n")
    for p in filtered:
        print(p["title"], "-", p["price"])

    search_category()
    add_product()

    print("\nDivision test:", safe_divide(10, 0))
    print(read_file_safe("python_notes.txt"))

    test_logging()