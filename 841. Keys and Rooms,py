class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        u = set(range(len(rooms)))
        while q:
            v = q.popleft()
            if v in u:
                u.remove(v)
                q.extend(rooms[v])
        return not u