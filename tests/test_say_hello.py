import sys
sys.path.insert(0,"./src")

import texttool as tt

result = tt.hello("My Name")

if result == "Hello, My Name!":
    print("Test passed")
else:
    print("Test failed")
