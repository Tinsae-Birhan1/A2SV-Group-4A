class Solution:
    def winner(self,nums: List[int],  l, r, turn):
        if l == r:
            return turn * nums[r]
        left = turn * nums[l] + self.winner(nums, l+1, r, -turn)
        right =  turn * nums[r] + self.winner(nums, l, r-1, -turn)

        if turn == 1:
            return max(left, right)
        else:
            return min(left, right)

    def PredictTheWinner(self, nums: List[int]) -> bool:
        result = self.winner(nums, 0, len(nums)-1, 1)
        return result >= 0
        