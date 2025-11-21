class pair_elements:
    def twoSum(self,nums,traget):
        lookup={}
        for i, num in enumerate(nums):
            if traget - num in lookup:
                return(lookup[traget - num],i)
            lookup[num] =i
value=int(input("Enter sum for which want to make this search :"))
print("index1=%d, index2=%d" %
pair_elements().twoSum((10,20,30,40,50,60,70),value))90
