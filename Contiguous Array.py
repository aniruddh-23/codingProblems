class Solution:
    def rec(self,nums,index,dp,run,f):
        global karma
        if index<=0:
            return 0
        if dp[index]!=None and (dp[index]!=0 or run==0):
            return dp[index]
        dp[index]=0
        if dp[index-1]>0 :
            dp[index]= self.rec(nums,index-dp[index-1]-1,dp,run,f)+dp[index-1]
            
            
        if run==1:
            #print(11,f,nums[index-2])
            if index-2>=0 and nums[f]^nums[index-2]==1:
                #print(00)
                karma[f]=1
                dp[index]=self.rec(nums,index-2,dp,0,f)+2
        return dp[index]
                
    def findMaxLength(self, nums) -> int:
        global karma
        dp=[None]*(len(nums)+1)
        dp[0]=0
        m=0
        karma=[0 for i in nums]
        for i in range(1,len(nums)+1):
            dp[i]=self.rec(nums,i,dp[::],1,i-1)
            dp[i]*=karma[i-1]
            #print(i,nums[i-1],dp[i],karma[i-1],dp,karma)
            m=max(dp[i],m)
        #print(dp)
        return m
karma=[]
nums=[0,1,1,0,1,1,1,0]
s=Solution()
print(s.findMaxLength(nums))
"""
nums=[1,0]       
s=[0]
for i in nums:
    s.append(s[-1]+i)
m=0
for beg in range(1,len(s)):
    for end in range(beg+1,len(s)):
        print(end,beg)
        a=end-beg+1
        b=s[end]-s[beg-1]
        #print(beg,end,a,b)
        if a/b==2:
            m=max(m,a)
"""