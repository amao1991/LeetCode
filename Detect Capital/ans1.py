class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.istitle() == 1 or word.islower() == 1 or word.isupper() == 1:
        	return True
        else:
        	return False