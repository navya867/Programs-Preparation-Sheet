class Solution: 
    def selectionSort(self, arr):
        # code here
        for i in range(len(arr)):
            min=i
            for j in range(i+1,len(arr)):
                if arr[min]>arr[j]:
                    min=j
            arr[i],arr[min]=arr[min],arr[i]
        return arr

sol=Solution()
arr=[10,34,5,6,2,56]
arr_result=sol.selectionSort(arr)
print(arr_result)

#TC= O(N^2)
#SC= O(1)
