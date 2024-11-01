#Back-end complete function Template for Python 3
from typing import List

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        ans = []
        # boolean list to mark all the vertices as not visited.
        done = [0]
        # creating a queue for BFS and pushing first vertex in queue.
        q = [0]

        while q:
            # adding front element in output list and popping it from queue.
            v = q[0]
            ans.append(v)

            # traversing over all the connected components of front element.
            for i in adj[v]:
                # if they aren't visited, we mark them visited and add to queue.
                if i not in done:
                    done.append(i)
                    q.append(i)
            q = q[1:]
        # returning the output list.
        return ans
