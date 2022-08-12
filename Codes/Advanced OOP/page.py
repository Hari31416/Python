class Pages:
    def __init__(self, page_number=None, text="", type=None):
        self.page_number = page_number
        self.text = text
        self.type = type

    def __str__(self):
        if self.page_number == 0:
            return "Title Page"
        else:
            return f"This is the page {self.page_number}"

    def add_text(self, text):
        self.text += text

    def get_text(self):
        print(self.text)

    def change_page_number(self, new_page_number):
        self.page_number = new_page_number
