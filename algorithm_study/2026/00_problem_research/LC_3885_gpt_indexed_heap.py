class EventManager:

    def __init__(self, events):
        self.heap = []  # (priority, eventId)
        self.pos = {}  # eventId -> index

        for eid, p in events:
            self.heap.append([p, eid])
            self.pos[eid] = len(self.heap) - 1

        # build heap
        for i in reversed(range(len(self.heap) // 2)):
            self._down(i)

    # ---------- helper: compare ----------
    def _better(self, a, b):
        # return True if a should be above b
        if a[0] != b[0]:
            return a[0] > b[0]
        return a[1] < b[1]

    # ---------- swap ----------
    def _swap(self, i, j):
        self.pos[self.heap[i][1]] = j
        self.pos[self.heap[j][1]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # ---------- sift up ----------
    def _up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self._better(self.heap[i], self.heap[parent]):
                self._swap(i, parent)
                i = parent
            else:
                break

    # ---------- sift down ----------
    def _down(self, i):
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            best = i

            if left < n and self._better(self.heap[left], self.heap[best]):
                best = left
            if right < n and self._better(self.heap[right], self.heap[best]):
                best = right

            if best == i:
                break

            self._swap(i, best)
            i = best

    # ---------- API ----------
    def updatePriority(self, eventId, newPriority):
        i = self.pos[eventId]
        oldPriority = self.heap[i][0]
        self.heap[i][0] = newPriority

        # decide direction
        if newPriority > oldPriority:
            self._up(i)
        else:
            self._down(i)

    def pollHighest(self):
        if not self.heap:
            return -1

        top_id = self.heap[0][1]

        last = self.heap.pop()
        del self.pos[top_id]

        if self.heap:
            self.heap[0] = last
            self.pos[last[1]] = 0
            self._down(0)

        return top_id