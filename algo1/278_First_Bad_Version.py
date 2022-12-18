# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        good = 0
        bad = n
        while good != bad - 1:
            unknown = (good + bad) // 2
            if isBadVersion(unknown):
                bad = unknown
            else:
                good = unknown
        return bad