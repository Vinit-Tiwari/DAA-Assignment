# DAA_Assignment
**Problem Statement:** 
Implement the solution for Maximum Sum Array by populating the array of size 14 with non-zero [positive/negative] random numbers.
Comment on sum, if first element is positive/negative and last element is positive/negative.

**Approach:**
Following steps are performed in order to find Maximum Crossing Sum Subarray:
Step 1: Find out the mid location of the array[mid=(low+high)/2]
Step 2: Calculate the sum of the left half array and find out the value of maximum sum and left most point of the array.
Step 3: Calculate the sum of the right half array and find out the value of maximum sum and right most point of the array.

**Solved Example:**
a= [ 5, -3, 9, 12, -8, 7, 11, -9, 1, -2, 4, 6] 
mid=(low+high)/2=(1+12)/2=13/2=6.5=6
From the above example we can conclude that Maximum sum from left side is 23 and from right side is 11 and Maximum sum at crossing is 33 hence maximun sum array is 33
starting from index - 0
and end index - 7
Crossing subarray of maximum sum is:
b= {5, -3, 9, 12, -8, 7, 11}
Maximum sum is: 33


Test Case 1: first element positive & last element positive
a= [3 , 52, -8, 16, 12, -15, 69, -22, 66, -55, 9, 6,-9, 44, 16]
Comment on sum: Maximum sum obtained is 184

Test Case 2: first element positive & last negative
a= [3 , 52, -8, 16, 12, -15, 69, -22, 66, -55, 9, 6,-9, 44, -16]
Comment on sum: Maximum sum obtained is 173

Test Case 3: first element negative & last element positive
a= [-3 , 52, -8, 16, 12, -15, 69, -22, 66, -55, 9, 6,-9, 44, 16]
Comment on sum: Maximum sum obtained is 181

Test Case 4: first element negative & last element negative
a= [-3 , 52, -8, 16, 12, -15, 69, -22, 66, -55, 9, 6,-9, 44, -16]
Comment on sum: Maximum sum obtained is 170

**Observations:** Sum obtained in the case-01 where first and last element is positive is the largest. Second largest is case-03 where first element is negative and last element is positive (last element is greater than first). And the lowest sum is in the case-04 where both elements are negative.
Therefore we can conclude that the sum od maximum subArray will be largest when both element are positive and least when both are negative.


**Code:**
```
import math

def findMaximumSubArray(a,low,high):
    if low==high:
        return low,high,a[low]
    else:
        mid=math.floor((low+high)/2)
        leftLow,leftHigh,leftSum=findMaximumSubArray(a,low,mid)
        rightLow,rightHigh,rightSum=findMaximumSubArray(a,low,mid)
        crossLow,crossHigh,crossSum=findMaxCrossingSubArrray(a,low,mid,high)
        if (leftSum>crossSum and leftSum>rightSum):
            return leftLow,leftHigh,leftSum
        elif (rightSum>crossSum and rightSum>leftSum):
            return rightLow,rightHigh,rightSum
        else:
            return crossLow,crossHigh,crossSum

def findMaxCrossingSubArrray(a,low,mid,high):
    leftSum=-math.inf
    sum=0
    for i in reversed(range(mid+1)):
        sum+=a[i]
        if (sum>leftSum):
            leftSum=sum
            maxLeft=i

    rightSum=-math.inf
    sum=0
    maxRight=mid+1
    for j in range(mid+1,high+1):
        sum+=a[j]
        if sum>rightSum:
            rightSum=sum
            maxRight=j

    return maxLeft,maxRight,(leftSum+rightSum)

#Test casee-01
#First and last element are positive
a=[3 , 52, -8, 16, 12, -15, 69, -22, 66, -55, 9, 6,-9, 44, 16]
print('\nTest case 1- First and last elements are positive')
l,h,s=findMaximumSubArray(a,0,len(a)-1)
print('Starting index of maximum sum array: ',l)
print('End index of maximum sum array: ',h)
print('Sum of maximun sum array: ',s)

#Test casee-02
#First element is negative and last element is positive
a=[-3 , 52, -8, 16, 12, -15, 69, -22, 66, -55, 9, 6,-9, 44, 16]
print('\nTest case 2- First element is negative and last element is positive')
l,h,s=findMaximumSubArray(a,0,len(a)-1)
print('Starting index of maximum sum array: ',l)
print('End index of maximum sum array: ',h)
print('Sum of maximun sum array: ',s)

#Test case-03
#First element is positive and last element is negative
a=[3 , 52, -8, 16, 12, -15, 69, -22, 66, -55, 9, 6,-9, 44, -16]
print('\nTest case 3- First element is positive and last element is negative')
l,h,s=findMaximumSubArray(a,0,len(a)-1)
print('Starting index of maximum sum array: ',l)
print('End index of maximum sum array: ',h)
print('Sum of maximun sum array: ',s)

#Test case-04
# First and last elemests are negative
a=[-3 , 52, -8, 16, 12, -15, 69, -22, 66, -55, 9, 6,-9, 44, -16]
print('\nTest case-04- First and last elements are negative')
l,h,s=findMaximumSubArray(a,0,len(a)-1)
print('Starting index of maximum sum array: ',l)
print('End index of maximum sum array: ',h)
print('Sum of maximun sum array: ',s)


```

**OutPut:**
```

Test case 1- First and last elements are positive
Starting index of maximum sum array:  0
End index of maximum sum array:  14
Sum of maximun sum array:  184

Test case 2- First element is negative and last element is positive
Starting index of maximum sum array:  1
End index of maximum sum array:  14
Sum of maximun sum array:  181

Test case 3- First element is positive and last element is negative
Starting index of maximum sum array:  0
End index of maximum sum array:  8
Sum of maximun sum array:  173

Test case-04- First and last elements are negative
Starting index of maximum sum array:  1
End index of maximum sum array:  8
Sum of maximun sum array:  170

```
