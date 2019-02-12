#Memory - python thinks you go from 0 to 2^48

import sys

for line in sys.stdin:
    print(range(int(line)), end='')

