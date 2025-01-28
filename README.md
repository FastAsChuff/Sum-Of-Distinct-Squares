# Sum-Of-Distinct-Squares
Interesting facts about how natural numbers can be expressed as the sum of distinct squares

Initial question https://math.stackexchange.com/questions/4870356/how-many-natural-numbers-require-at-least-6-terms-to-express-as-the-sum-of-disti

Conjecture about numbers requiring 5 terms https://math.stackexchange.com/questions/5028730/sum-of-5-distinct-squares-conjecture

Appeal for insights on algorithmic improvements https://math.stackexchange.com/questions/5028731/sum-of-5-distinct-squares-algorithm

I wrote a program sum5sq.c to list all cases less than or equal to argument n of integers that require a minimum of exactly 5 terms to be expressed as the sum of distinct squares. Its output for n = 10^10 can be found in sum5sq.txt. A demonstration of the dynamic programming algorithm used to find the cases can be found in sum5sq.py. The c implementation is much more space and time efficient, but much more complicated too. Please report errors if you find them.
