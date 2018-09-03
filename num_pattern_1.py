n = int(input())
for a in range(1, n + 1):
  for b in range(1, a + 1):
    if b <= a:
      print(b, end="")
    else:
      print(" ", end="")
  for c in range(n, 0, -1):
    if c > a:
      print(" ", end="")
    else:
      print(c, end="")
  print()
