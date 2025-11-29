# Last updated: 29/11/2025, 22:35:20
1class Solution:
2    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
3        people = []
4        for i in range(len(names)):
5           people.append((names[i], heights[i]))
6           people.sort(key=lambda x:x[1], reverse =True)
7        result=[]
8        for person in people:
9            result.append(person[0])
10        return result
11
12
13        