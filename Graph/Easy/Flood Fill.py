class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def adj(cord,L = image):
            print(cord)
            i,j = cord[0], cord[1]
            clr = L[i][j]
            adjL = []
            n = len(L); m = len(L[0])
            if i>0: adjL.append((i-1,j))
            if j>0: adjL.append((i,j-1))
            if j<m-1: adjL.append((i,j+1))
            if i<n-1: adjL.append((i+1,j))
            Ladj = []
            for i in adjL:
                if L[i[0]][i[1]]==clr:
                    Ladj.append(i)
            return Ladj

        # bfs
        que = [(sr,sc)]
        vis = []
        while que:
            cord = que.pop(0)
            if cord in vis: continue
            vis.append(cord)
            que += adj(cord)
        for i in vis:
            image[i[0]][i[1]] = color
        return image
