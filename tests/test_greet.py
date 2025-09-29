import sys
sys.path.insert(0,"./src")

import texttool as tt

result = tt.greet("My Name")

if result == "Hello, My Name!" + " \nIt's nice to meet you!":
    print("Test passed")
else:
    print("Test failed")
