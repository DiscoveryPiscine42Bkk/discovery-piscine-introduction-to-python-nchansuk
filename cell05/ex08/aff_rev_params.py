import sys
import re

if len(sys.argv) == 3:
    keywork = sys.argv[1]
    string_to_search = sys.argv[2]
    occurrences = re.findall(re.escape(keywork), string_to_search)
    print(len(occurrences))
else:
    print("none")