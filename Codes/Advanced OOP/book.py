from page import Pages


class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.pages = []
        for i in range(num_pages):
            self.pages.append(Pages(page_number=i))

    def __str__(self):
        return f"{self.title} by {self.author}"

    def create_title_page(self):
        title = f"{self.title}\n\tBy {self.title}"
        self.pages[0].add_text(title)


harry1 = Book("Harry Potter 1", "JK Rowling", 200)
harry1.create_title_page()
len(harry1.pages)

print(harry1.pages[0].text)
