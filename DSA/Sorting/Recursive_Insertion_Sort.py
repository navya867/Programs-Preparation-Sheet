class Solution: 
    def InsertionSort(self, arr,n,i):
        
        if i==n:
            return arr
        j=i-1
        key=arr[i]

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
        return self.InsertionSort(arr,n,i+1)



sol=Solution()
arr=[10,34,5,6,2,56]
n=len(arr)
i=0
arr_result=sol.InsertionSort(arr,n,i)
print(arr_result)

