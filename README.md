
## Performance Analysis

| Input Size          | Time Complexity | Space Complexity                      |
|---------------------|-----------------|---------------------------------------|
| Tree with `n` nodes | O(n)            | O(w), where `w` is the maximum width  |
| Large Tree          | Linear          | Linear                                |
| Skewed Tree         | Linear          | Constant                              |


## Space Complexity

| Algorithm                     | Time Complexity | Space Complexity |
|-------------------------------|-----------------|------------------|
| Height of a Binary Tree       | O(n)            | O(h)             |
| Tree Level Order Traversal    | O(n)            | O(w)             |
| Swap Nodes at a Specific Level| O(n)            | O(w)             |

## Notes:

**Balanced Tree: For a balanced tree:**

- h ≈ log n, and 𝑤 ≈ 𝑛 / 2

**Skewed Tree: For a skewed tree:**

- ℎ = 𝑛, and 𝑤 = 1