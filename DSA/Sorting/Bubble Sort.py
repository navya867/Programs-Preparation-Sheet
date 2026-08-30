# class Solution: 
#     def bubbelSort(self, arr):
#         for i in range(len(arr)-1,0,-1):
#             for j in range(i):
#                 if arr[j]>arr[j+1]:
#                     arr[j],arr[j+1]=arr[j+1],arr[j]
#         return arr
    

# sol=Solution()
# arr=[10,34,5,6,2,56]
# arr_result=sol.bubbelSort(arr)
# print(arr_result)

#TC= O(N^2)
#SC= O(1)

###                 Best case -- check if any swap is req if not then its sorted
class Solution: 
    def bubbelSort(self, arr):
        
        for i in range(len(arr)-1,0,-1):
            swap=False
            for j in range(i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swap=True
            if not swap:
                break
        return arr
    

sol=Solution()
arr=[10,34,5,6,2,56]
arr_result=sol.bubbelSort(arr)
print(arr_result)

