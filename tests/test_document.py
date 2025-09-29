from texttool.document import Document

# Test Create Document 
def test_create_document():
    doc = Document(filepath="tests/example_file.txt")
    assert doc.filepath == "tests/example_file.txt"

# Test Get Line Count 
def test_get_line_count():
    doc = Document(filepath="tests/example_file.txt")
    assert doc.get_line_count() == 2

# Test Get Word Count
def test_get_word_count():
    doc = Document(filepath="tests/example_file.txt")
    assert doc.get_word_occurence("test") == 2