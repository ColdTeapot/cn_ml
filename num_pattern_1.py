"""
Print the following pattern for n number of rows.

For eg. N = 5

1    1
12   21
123  321
1234 4321
1234554321

Sample Input 1 :

4

Sample Output 1 :

1   1
12  21
123 321
12344321

"""

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
