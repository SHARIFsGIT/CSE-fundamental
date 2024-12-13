n = input()
reversed = str(int(n[ : : -1]))

print(reversed)

if n == reversed:
    print("YES")
else:
    print("NO")