"""

You are given an integer n representing a tree with n nodes, where the nodes are numbered from 0 to n - 1 and the tree is rooted at node 0. The tree is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

You are also given a string colors of length n, where colors[i] represents the color of node i: 'R' if it is Red, or 'B' if it is Blue.

You may flip the color of any node: from 'R' to 'B', or from 'B' to 'R'. Flipping node u incurs a cost equal to the size of the subtree of node u.

Your goal is to perform flips so the Red nodes form a single connected component in the tree. Blue nodes may be disconnected. A configuration with no Red nodes is also considered valid.

Return the minimum total cost required to achieve this.

 

Example 1:

Input: n = 3, colors = "RBR", edges = [[0,1],[1,2]]

Output: 1

Explanation:



There are two Red nodes (0 and 2) that are not connected to each other.
We can flip node 2 from 'R' (Red) to 'B' (Blue). The subtree size of node 2 is 1, so the cost is 1.
After this flip only node 0 remains Red, forming exactly one connected Red component.
Example 2:

Input: n = 3, colors = "RBR", edges = [[0,1],[0,2]]

Output: 0

Explanation:​​​​​​​



There are two Red nodes (0 and 2) that are already connected to each other.
No flips are needed since all Red nodes already form a single connected group. Thus, the minimum total cost is 0.
Example 3:

Input: n = 4, colors = "BRRR", edges = [[0,1],[0,2],[0,3]]

Output: 2

Explanation:​​​​​​​



There are three Red nodes (1, 2 and 3), which are not connected to each other.
All three Red nodes are leaves and are disconnected from one another.
To obtain a single Red group, we keep one Red leaf and flip the other two to Blue.
Each leaf subtree size is 1, so flipping any two costs 2.
Example 4:

Input: n = 3, colors = "BBB", edges = [[0,1],[1,2]]

Output: 0

Explanation:

​​​​​​​

All nodes are Blue, so there are no Red nodes.
An empty Red group is considered a single connected group, so this state is already valid. Thus, the cost is 0.
 

Constraints:​​​​​​​

1 <= n <= 105
n == colors.length
colors[i] is either 'R' or 'B'.
edges.length == n - 1
edges[i] = [ui, vi]
0 <= ui, vi <= n - 1
The input is generated such that edges represents a valid tree.


"""

class Solution:
    def minCost(self, n, colors, edges):

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        parent[0] = 0
        order = [0]

        for u in order:
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    order.append(v)

        size = [1] * n
        dp = [0] * n
        total = 0

        for u in reversed(order):

            for v in adj[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    dp[u] += min(0, dp[v])

            if colors[u] == 'R':
                total += size[u]
                dp[u] -= size[u]
            else:
                dp[u] += size[u]

        return total + min(0, min(dp))

n = 4 
colors = "BRRR" 
edges = [[0,1],[0,2],[0,3]]

a1 = Solution()


print(a1.minCost(n,colors,edges))
