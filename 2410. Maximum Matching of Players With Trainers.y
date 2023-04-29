class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()

        i = j = res = 0
        n , m = len(players) , len(trainers)

        while i < n and j < m :
            if players[i] <= trainers[j] :
                res += 1
            else :
                try :
                    while players[i] > trainers[j] :
                        j += 1
                    res += 1
                except :
                    break
            i += 1
            j += 1

        return res