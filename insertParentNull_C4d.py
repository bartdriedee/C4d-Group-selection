import sys
import os

# Insert the location of this file to the path 
# so imported modules can be found
__currdir__ = os.path.dirname(__file__)
if __currdir__ not in sys.path:
    sys.path.insert(0, __currdir__)
from Group import InsertNull


if __name__=='__main__':
    s = InsertNull()
    # Set relative to True for Cinema4d style behaviour
    s.main(True)