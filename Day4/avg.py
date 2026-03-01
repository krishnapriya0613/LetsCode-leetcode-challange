class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum=0
        avg=0
        count=0
        for num in nums:
            if num%2==0:
                if num%3==0:
                    sum+=num
                    count+=1

        if(count!=0):
            avg=int(sum/count)
        return avg


        
