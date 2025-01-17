import tkinter as tk
from tkinter import ttk

class NetflixInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Netflix Interface")
        self.geometry("800x600")
        self.configure(bg="black")

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self, text="Netflix", font=("Arial", 24), fg="red", bg="black")
        title_label.pack(pady=20)

        # Search Bar
        search_frame = tk.Frame(self, bg="black")
        search_frame.pack(pady=10)
        search_label = tk.Label(search_frame, text="Search:", font=("Arial", 14), fg="white", bg="black")
        search_label.pack(side=tk.LEFT, padx=5)
        search_entry = tk.Entry(search_frame, font=("Arial", 14), width=40)
        search_entry.pack(side=tk.LEFT, padx=5)
        search_button = tk.Button(search_frame, text="Search", font=("Arial", 14), command=self.search)
        search_button.pack(side=tk.LEFT, padx=5)

        # Categories
        categories_frame = tk.Frame(self, bg="black")
        categories_frame.pack(pady=20)
        categories_label = tk.Label(categories_frame, text="Categories", font=("Arial", 18), fg="white", bg="black")
        categories_label.pack(pady=10)
        categories = ["Action", "Comedy", "Drama", "Horror", "Romance"]
        for category in categories:
            category_button = tk.Button(categories_frame, text=category, font=("Arial", 14), command=lambda c=category: self.show_category(c))
            category_button.pack(side=tk.LEFT, padx=10)

        # Content Area
        self.content_frame = tk.Frame(self, bg="black")
        self.content_frame.pack(pady=20)

    def search(self):
        # Placeholder for search functionality
        print("Search button clicked")

    def show_category(self, category):
        # Placeholder for showing category content
        print(f"Showing category: {category}")

if __name__ == "__main__":
    app = NetflixInterface()
    app.mainloop()