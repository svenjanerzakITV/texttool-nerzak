import sys
sys.path.insert(0,"./src")

from texttool import hello
def greet(name: str = "User" ) -> str:
    string = hello(name) + "\nIt's nice to meet you!"
    print(string)
    return string
    