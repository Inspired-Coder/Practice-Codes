'''Generalised Chocolate
Description
Earlier you solved the chocolate problem where Sanjay had m rupees and cost of each chocolate was c rupees. Shopkeeper gave away one chocolate for three wrappers. In this problem lets generalise the question saying, Sanjay has m rupees, each chocolate costs c rupees, shopkeeper will give away k chocolates for w wrappers. Can you find now how many chocolates Sanjay will be able to eat?


Input: 4 integers separated by commas in order m c w k
integers c and w will be >0
integers m and k will be >=0
integer k will be <w

Output: An integer denoting number of chocolates Sanjay will be able to get.

Sample input:
15, 2, 3, 1

Sample output:
10

Explanation:
Sanjay has 15 rupees, buys 7 chocolates for 2 rupees each.
Sanjay now has 7 wrappers, exchanges 6 of them for 2 more chocolates.
Sanjay now has 3 wrappers and exchanges them for 1 more chocolate making a total of 10 chocolates

Sample input:
15, 2, 3, 2

Sample output:
17

Explanation:
Sanjay has 15 rupees, buys 7 chocolates for 2 rupees each.
Sanjay now has 7 wrappers, exchanges 6 of them for 4 more chocolates.
Sanjay now has 5 wrappers and exchanges 3 of them for 2 more chocolates.
Sanjay now has 4 wrappers and exchanges 3 of them for 2 more chocolates.
Sanjay now has 3 wrappers and exchanges them for 2 chocolates making a total of 17 chocolates.
'''




s=input().split(',')

m=int(s[0])
c=int(s[1])
w=int(s[2])
k=int(s[3])

tc=m//c  
tw=m//c  

while tw>=w:
 tc=tc+tw//w*k
 tw=tw-((tw//w)*w)+(tw//w)*k

print('Total Chocolates can buy is:',tc)


