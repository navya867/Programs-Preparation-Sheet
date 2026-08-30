class Solution: 
    def bubbelSort(self, arr,n):
        swap=False
        if n==1:
            return arr
        else:
            for i in range(0,n-1):
                if arr[i+1]<arr[i]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                    swap=True
            if not swap:
                return arr
            else:
                return self.bubbelSort(arr,n-1)


sol=Solution()
arr=[10,34,5,6,2,56]
n=len(arr)
arr_result=sol.bubbelSort(arr,n)
print(arr_result)

