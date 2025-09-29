import pytest
from unittest.mock import mock_open
from texttool.document import Document

@pytest.fixture(autouse = True)
def mock_file(monkeypatch):
    mock = mock_open(read_data="This is a test document. It contains words.\nIt is only a test document.")
    monkeypatch.setattr("builtins.open", mock)
    return mock

@pytest.fixture
def doc():
    return Document(filepath="tests/example_file.txt")

# Test Create Document 
def test_create_document(doc):
    assert doc.filepath == "tests/example_file.txt"

# Test Get Line Count 
def test_get_line_count(doc):
    assert doc.get_line_count() == 2

# Test Get Word Count
def test_get_word_count(doc):
    assert doc.get_word_occurence("test") == 2
    assert doc.get_word_occurence("words") == 1

def test_empty_file(monkeypatch):
    mock = mock_open(read_data="")
    monkeypatch.setattr("builtins.open", mock)

    with pytest.raises(ValueError):
        Document(filepath="empty_file.txt")

# def test_real_file():
#     doc2 = Document(filepath="../meditations_book.txt")
#     print(doc2.get_line_count())
#     assert doc2.get_line_count() > 1
    