class Document:

    def __init__(self, filepath: str, title: str = "", author: str = "", id: int = 0):
        self.filepath = filepath
        self.content = self.read(self.filepath)

        self.title = title
        self.author = author
        self.id = id

    def read(self, filepath: str) -> str:
        with open(filepath, "r", encoding="utf-8") as file:
            raw_data = file.read()
        if not raw_data:
            raise ValueError("File is empty.")
        return raw_data

    def get_line_count(self) -> int:
        return len(self.content.splitlines())


    def get_word_occurence(self, word: str) -> int:
        return self.content.lower().count(word.lower())

