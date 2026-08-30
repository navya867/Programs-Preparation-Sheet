# class Insertion_Sort:
#     def insertion():
#     for i in range(1, len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j] < arr[j-1]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]

for i in range(n):
    j=i
    while(j<0 and nums[j-1]>nums[j]):
        nums[j-1],nums[j]=-nums[j],nums[j-1]
        j=j-1

class Solution:
    def insertionSort(self,nums):
        n=len(nums)
        for i in range(n):
            j=i-1
            key=nums[i]
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j=j-1
            nums[j+1]=key
        return nums


if __name__ == "__main__":
    # Create an instance of solution class
    solution = Solution()
    
    nums = [13, 46, 24, 52, 20, 9]
    
    print("Before Using Insertion Sort:")
    for num in nums:
        print(num, end=" ")
    print()
    
    # Function call for insertion sort
    nums = solution.insertionSort(nums)
    
    print("After Using Insertion Sort:")
    for num in nums:
        print(num, end=" ")
    print()


#time - O(N^2) for both worst and avg case
#best case - O(n)
