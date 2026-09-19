class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        d={}
        n=len(names)
        for i in range(n):
            d[heights[i]]=names[i]
        print(d)
        heights.sort()
        print(heights)
        ans=[]
        for he in heights:
            ans.append(d[he])
        return ans[::-1]




    
