import sys
input = sys.stdin.readline
print = sys.stdout.write
from collections import Counter

word = Counter(input().strip().upper()).most_common()
print("%s" % word[0][0]) if len(word) < 2 else print("?") if word[0][1] == word[1][1] else print("%s" % word[0][0])