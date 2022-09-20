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

