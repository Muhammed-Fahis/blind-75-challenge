class Two_sum:
    def twosum(self,target,nums):
        prev_map=dict()
        for i,num in enumerate(nums):
            if target - num in prev_map:
                return[i,prev_map[target-num]]
            prev_map[num] = i

two_sum = Two_sum()
print(two_sum.twosum(9,[2,7,11,15,9]))
      
   
   