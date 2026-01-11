import requests
import tkinter as tk

def get_books():
    response = requests.get("https://potterapi-fedeperin.vercel.app/en/books")
    if response.status_code != 200:
        print("Error 200 thingy")
    return response.json()

def book_description(title):
    books = get_books()
    for book in books:
        if title.lower() == book["title"].lower():
            return book.get("description", "No description available")
    return "Book not found"

def search_book():
    title = entry.get().strip()
    if not title:
        result_label.config(text="Please enter a book title")
        return
    description = book_description(title)
    result_label.config(text=description)

window = tk.Tk()
window.title("Harry Potter Book Finder")
window.geometry("600x400")
window.resizable(False, False)

prompt = tk.Label(window, text="Enter the Harry Potter book title:", font=("Times New Roman", 14))
prompt.pack(pady=10)

entry = tk.Entry(window, font=("Times New Roman", 14), width=40)
entry.pack(pady=5)

search_button = tk.Button(window, text="Find Description", font=("Arial", 14), command=search_book)
search_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Times New Roman", 12), wraplength=550, justify="left", fg="blue")
result_label.pack(pady=10)

window.mainloop()
