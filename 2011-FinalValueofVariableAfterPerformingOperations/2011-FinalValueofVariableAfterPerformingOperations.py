# Last updated: 13/12/2025, 07:11:55
1class Solution:
2    def finalValueAfterOperations(self, operations: List[str]) -> int:
3        X = 0
4        for i in operations:
5            if i=="X++" or i== "++X":
6                X=X+1
7            elif i== "X--" or i== "--X":
8                X=X-1
9        return X
10
11        #Increment and decrement the number
12        
13        #store the numbers iteratively things iteratively
14        #then return the final result
15        