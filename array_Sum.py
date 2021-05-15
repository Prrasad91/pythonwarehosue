#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 10:28:33 2021

@author: venkateshprasads
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

"""


class solution:
    
    def __init__(self,nums,target):
        self.nums=nums
        self.target=target
        
    def twoSum(self, nums: 'list', target: int) -> 'list':
      
        for i in range(len(nums)-1):
            #print(i,len(nums))
            j=0
            if i != len(nums):
                for j in range(len(nums)-1):
                    #print(i,j)
                    if ((nums[i] + nums[j+1]) == target):
                        lst = [i , j+1]
                        return lst
                    j=j+1

a=solution.twoSum('vale',[2,7,11,15], 9)
print(a)
