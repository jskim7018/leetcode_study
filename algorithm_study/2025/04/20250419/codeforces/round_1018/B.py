import heapq

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    l = list(map(int,input().split()))
    r = list(map(int,input().split()))

    heap = []
    for i in range(n):
        heap.append((-l[i],i))
        heap.append((-r[i],i))
    heapq.heapify(heap)
    st = set()
    ans = 0
    while heap and k:
        popped = heapq.heappop(heap)
        v = -popped[0]
        i = popped[1]
        if i in st and k == 1:
            continue
        else:
            if i in st:
                k-=1
            else:
                st.add(i)
            ans += v
    print(ans + 1)
