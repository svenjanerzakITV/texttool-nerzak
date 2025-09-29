import pytest
import texttool as tt
# or better 

def test_hello():
    assert tt.hello("My Name") == "Hello, My Name!"

# Testing edge cases
def test_hello_empty_string():
    with pytest.raises(ValueError):
        tt.hello("")