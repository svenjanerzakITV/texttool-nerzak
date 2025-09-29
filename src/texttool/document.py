class Document:
    def __init__(self, filepath, title="", author="", bookID=0):
        self.filepath = filepath
        self.title = title
        self.author = author
        self.bookID = bookID
        self.content = self.read(self.filepath)
    
    def read(self, filepath: str) -> str:
        with open(filepath, "r", encoding="utf-8") as file_obj:
            return file_obj.read()
        
    def get_line_count(self) -> int:
        return len(self.content.splitlines())
    
    def get_word_occurence(self, word: str) -> int:
        return self.content.lower().count(word.lower())