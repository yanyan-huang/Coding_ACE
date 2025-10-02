"""
Date: Oct 2, 2025

Amazon sells millions of products on its website and for better customer experience we like to show a widget with the "most popular items bought" on the home page.
You can assume that you told me how you'd go about calculating the top K popular items sold on Amazon.
I'd like you to tell me how you have a service and your service gets notified in the form of a (Customerld, Itemld, Timestamp) message whenever a customer purchases an item.

Input:
- All purchaseRecords: array of array [[Customerld(str), Itemld(str),Timestamp(int)], … ]
- For each purchase: Customerld, Itemld,Timestamp
- int K 

Output:
- ItemId for the top K popular items [Itemld,... ]
(order by purchaseAmount/timestamp in descending order, )

Constraints:
- Size of purchaseRecords: n ~10^6

Edge:
- Empty input array:[] => no purchase => []
- Equal purchaseAmount for some items 
- Item1: 10, 1(timestamp), Item2: 10,2(timestamp), => rank 1 and 2
- k : 0 => []; k >= n => all items on file

N = len(purchaseRecords), U = unique items, k
sorting O(nlogn)
heap solution
- T: O(N + U*logK + klogK) 
- S: O(N+K)
"""
from collections import defaultdict
import heapq

def topKItems(purchaseRecords,k):
    # counter for purchaseRecords => freq dict {itemId: purchaseAmount} 
    freq = defaultdict(int) 
    # last_purchase dict {itemId: timestamp of its last purchase}
    last_purchase = defaultdict(int)

    for _, itemId,timestamp in purchaseRecords: # O(N)
        freq[itemId] += 1
        last_purchase[itemId] = max(timestamp, last_purchase[itemId])

    # heap of size k 
    heap = []
    for itemId, count in freq.items(): # O(U*logK)
        timestamp = last_purchase[itemId]
        heapq.heappush(heap, (count, timestamp, itemId)) # O(logK)
        if len(heap) > k: 
            heapq.heappop(heap)
    
    # [(count, timestamp, itemId)]
    return [itemId for _, _, itemId in sorted(heap, key=lambda x: (-x[0], -x[1]))] # O(klogK+U)

# ========== Tests =====================
purchaseRecords = []
k = 2
print(topKItems(purchaseRecords,k))  # []

purchaseRecords = [["c1", "id1",1],
                    ["c2", "id1",2],
                    ["c3", "id1",3],
                    ["c1", "id2",10],
                    ["c4", "id2",20]]
k = 1
print(topKItems(purchaseRecords,k))  # ["id1"]  

purchaseRecords = [["c1", "id1",1],
                    ["c2", "id1",2],
                    ["c3", "id1",3],
                    ["c1", "id2",10],
                    ["c4", "id2",20]]
k = 2
print(topKItems(purchaseRecords,k)) # ["id1", "id2"] order doesnt matter here

purchaseRecords = [["c1", "id1",1],
                    ["c2", "id1",2],
                    ["c1", "id2",10],
                    ["c4", "id2",20]]
k = 1
print(topKItems(purchaseRecords,k)) # ["id2"]

