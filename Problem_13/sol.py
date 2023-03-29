class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = 0
        j = 0
        tab = []
        for i in range(len(s)):
            if s[i] == "I":
                tab.append(1)
            if s[i] == "V":
                tab.append(5)
            if s[i] == "X":
                tab.append(10)
            if s[i] == "L":
                tab.append(50)
            if s[i] == "C":
                tab.append(100)
            if s[i] == "D":
                tab.append(500)
            if s[i] == "M":
                tab.append(1000)
        while j < len(tab) - 1:
            if tab[j] < tab[j + 1]:
                x += tab[j + 1] - tab[j]
                j += 2
            else:
                x += tab[j]
                j += 1
        if len(tab) >= 2:
            if tab[-1] <= tab[-2]:
                x += tab[-1]
        if len(tab) == 1:
            x += tab[0]

        return x
