# Jesus Carlos Martinez Gonzalez
# 12/07/2023
# QHEAP1 (https://www.hackerrank.com/challenges/qheap1/problem)

"""
This question is designed to help you get a better understanding of basic heap operations.
There are 3 types of query:
• "I v" -Add an element v to the heap.
• "2 v" - Delete the element v from the heap.
• "3" - Print the minimum of all the elements in the heap.
"""

import heapq


def main():
    n = int(input())
    heap = []
    heap_ignore = set()

    for _ in range(n):
        query = input()
        match query[0]:
            case "1":
                heapq.heappush(heap, int(query.split()[1]))
            case "2":
                heap_ignore.add(int(query.split()[1]))
            case "3":
                while heap[0] in heap_ignore:
                    heap_ignore.discard(heap[0])
                    heapq.heappop(heap)
                print(heap[0])


if __name__ == "__main__":
    main()
