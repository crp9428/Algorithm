year = int(input().strip())
print("0") if year % 4 != 0 else print("1") if year % 400 == 0 or year % 100 != 0 else print("0")