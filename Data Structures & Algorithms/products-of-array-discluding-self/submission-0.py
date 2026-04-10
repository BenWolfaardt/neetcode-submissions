class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product: int = 1
        product_list = []
        
        # for loop
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                product *= nums[j]

            product_except_self: int = int(product)
            product_list.append(product_except_self)
            product = 1
        
        return product_list
