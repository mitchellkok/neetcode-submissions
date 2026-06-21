class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Input: two strings, where perm of s1 might reside within s2
        # output: Bool

        # approach 1: brute force
        # would require two loops - through letters of s2, then through possible letters of s1
        tracker = [0] * 26 

        # fill tracker
        for i in range(len(s1)):
            char = s1[i]
            tracker[ord(char)-ord('a')] += 1

        for i in range(len(s2) - len(s1) + 1):
            char = s2[i]
            if tracker[ord(char)-ord('a')] > 0:
                # this letter exists in s1
                print("found", s2[i], "at", i)
                pointer = i
                tracker_temp = tracker.copy()
                while pointer < len(s2) and tracker_temp[ord(s2[pointer])-ord('a')] > 0:
                    print("\tPopping", s2[pointer], "at", pointer, ", sum", sum(tracker_temp))
                    tracker_temp[ord(s2[pointer])-ord('a')] -= 1
                    pointer += 1
                if sum(tracker_temp) == 0:
                    return True
        
        return False