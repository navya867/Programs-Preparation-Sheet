class Solution: 
    def Merge(self, arr,low,mid,high):
        left=low
        right=mid+1
        temp=[]
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1

        while left<=mid:
            temp.append(arr[left])
            left+=1
        while right<=high:
            temp.append(arr[right])
            right+=1
        for i in range(low,high+1):
            arr[i]=temp[i-low]

    def Mergesort(self,arr,low,high):
        if low>=high:
            return
        mid= (low+high) //2
        self.Mergesort(arr,low,mid)
        self.Mergesort(arr,mid+1,high)
        self.Merge(arr,low,mid,high)



sol=Solution()
arr=[10,34,5,6,2,56]
high=len(arr)-1   #while merging elements in merge it will throw list index out of range error
low=0
sol.Mergesort(arr,low,high)
print(*arr)

