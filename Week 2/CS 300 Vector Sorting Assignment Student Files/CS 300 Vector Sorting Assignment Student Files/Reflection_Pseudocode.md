# Code Reflection & Pseudocode

## Pseudocode for Selection Sort

```plaintext
For i from 0 to length of bids - 1
    minIndex = i
    For j from i + 1 to length of bids
        If bids[j].title < bids[minIndex].title
            minIndex = j
    If minIndex != i
        Swap bids[i] and bids[minIndex]
```

## Pseudocode for Quick Sort

```plaintext
Function partition(bids, begin, end)
    pivot = bids[midpoint].title
    low = begin
    high = end
    While not done
        While bids[low].title < pivot, increment low
        While pivot < bids[high].title, decrement high
        If low >= high
            done = true
        Else
            Swap bids[low] and bids[high]
            Increment low, Decrement high
    Return high

Function quickSort(bids, begin, end)
    If begin >= end, Return
    mid = partition(bids, begin, end)
    quickSort(bids, begin, mid)
    quickSort(bids, mid + 1, end)
```

## Code Reflection

The purpose of this program was to parse a CSV file containing municipal auction bids, load them into a vector, and sort them alphabetically by title using two completely different algorithms. Implementing the selection sort was relatively straightforward because the logic is highly intuitive. You simply scan the list for the lowest value, move it to the front, and repeat. However, the real challenge was dealing with the massive performance hit when scaling up. While working with the smaller dataset was fine, running selection sort on the 12,023 record file took over ten seconds to process.

To overcome this performance bottleneck, I implemented a quicksort algorithm. The main hurdle with quicksort was getting the recursive partition logic exactly right, specifically ensuring the string comparisons for bid.title didn't cause out-of-bounds errors with the low and high index pointers. Once the divide-and-conquer logic was properly implemented, the performance difference was staggering. The quicksort tackled the same 12,000 records in a fraction of a second. This assignment was a great practical lesson in why choosing the right algorithm is just as important as writing code that simply functions.

