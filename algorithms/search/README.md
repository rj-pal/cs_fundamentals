### Linear Search

Linear search is a naive or brute force search approach for finding an element in iterable of size n. It requires looking at every element in the list until the search item is found of not. The time complexity is **O(n)** as the alogrithm has to look at each element one by one sequentially. The string implementation, which may take a string of size m <= n, has a worst case time complexity of **O(n*m)**. 

It is essential in searching an unsorted list, as a more efficient search approach like binary search, is not possible.

### Binary Search 

Binary searh approach takes advantage of sorted iterables where knowing that the elements of the data are ordered can be exploited. Analagous to looking for a name quickly in an alphabetical list, once we have looked at element in the list, we know the relative position of the search item, either greater than or less (or later in the alphabet or earlier). By looking at an element half way in the list and applying the greater or less than concept, we can keep iterating by checking the next next mid point until we have bracketed the element. The reducing the number of elements we have to look at by half each time, makes the time complexity of binary search **O(log(n))**. 

This is a classic search algorithm and the core idea of dividing the interval in half in each step is a deep concept for algorithmic efficiency.