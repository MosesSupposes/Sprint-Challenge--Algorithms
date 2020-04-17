#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)

b) 0(nlogn)

c) 0(n)

## Exercise II

This is the linear approach to solving this challenge:
For each floor in the building, starting from the lowest
floor, drop an egg. As soon as the egg breaks, stop looping.
The time complexity of this algorithm is O(n).

This is the binary approach to solving this challenge:
Split the number of floors in half and store both halfs in a list. Keep on splitting the floors in half until you reach a list with one or zero elements inside of it. Once you've split until you can't split anymore, start merging the list of floors back together. For each merge, you should have two lists: a left and a right, comprised of different floor levels. Alternating between the left and right lists, drop the egg from the first floor on each list. If you exhaust through
both lists and the egg doesn't crack, join those lists together in the order of the number of floors. Keep repeating this process until you reach a floor that cracks the egg. Once the egg cracks, you've found your f. If your merge all of the lists back together and the egg didn't crack at any of the floors, then your n was too low; try this process again with a higher input.
The time complexity of this algorithm is O(logn)
