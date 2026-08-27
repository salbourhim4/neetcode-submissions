class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        rlist1 = []
        rlist2 = []
        newrlist1 = []
        newrlist2 = []
        for item in s:
            rlist1.append(ord(item))
        for item in t:
            rlist2.append(ord(item))
        while len(rlist1) > 0:
            newrlist1.append(min(rlist1))
            rlist1.remove(min(rlist1))
        while len(rlist2) > 0:
            newrlist2.append(min(rlist2))
            rlist2.remove(min(rlist2))
        if newrlist1 == newrlist2:
            return True
        else:
            return False
        


        
        
        