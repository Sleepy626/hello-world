# Create a program that will create a sideway pyramid. The sideways height of the pyramid should be equal
# to the input. The pyramid must be composed of $ symbols.
# ## Specifications
# The input will be 0 < k ≤ 10
# The output should be a pyramid of sideways height k.
# ## Examples
# Sample Input
# ```Python
# 3
# ```

# Sample Output:
# ```Python
# $
# $$
# $$$
# $$
# $

k = int(input("input"))
for i in range(1, k + 1):
    print('$' * i)
for i in range (k - 1, 0, -1):
    print('$' * i)

