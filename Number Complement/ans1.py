class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        binary_list = list(str(bin(num)))

        ans = []
        
        for i in range(2, len(binary_list), 1):
        	if binary_list[i] != str(0):
        		ans.append('0')
        	else:
        		ans.append('1')
        
        ans = int(str(int(''.join(ans))), 2)
        
        return ans
