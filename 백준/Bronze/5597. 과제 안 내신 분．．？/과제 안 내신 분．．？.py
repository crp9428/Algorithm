import sys

submissions = [False for _ in range(30)]
for n in list(map(int, sys.stdin.readlines())):
    submissions[n-1] = True

for i, isSubmission in enumerate(submissions, start=1):
    if isSubmission is False:
        print(i)