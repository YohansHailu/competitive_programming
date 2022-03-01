class Solution:
    def rec_fun(self,image,sr,sc,newColor):
        f_color = image[sr][sc]
        image[sr][sc] = newColor

        index = (0,1,0,-1,0)
        for i in range(len(index) - 1):
            nsr = sr + index[i]
            nsc = sc + index[i+1]

            if not (0 <= nsr < len(image) and 0 <= nsc < len(image[0])):
                continue

            if image[nsr][nsc] == f_color:
                 self.rec_fun(image, nsr, nsc, newColor)
                    
        return image 
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if image[sr][sc] == newColor:
            return image
        
        return self.rec_fun(image,sr,sc,newColor)
        
