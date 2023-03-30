# # n,d= [int(x) for x in input().split()]
# # arr=[int(x) for x in input().split()]

# # arr.sort(reverse=True)
# # #90 80 70 60 50 100
# # #100 90 80 70 60 50 t=90 w=1
# # wins = 0
# # team_power = 0
# # for i in range(n):
# #     team_power += arr[i]
# #     if team_power > d:
# #         wins += 1
# #         team_power = arr[i]

# # print(wins)


# n, d = map(int, input().split())
# players = list(map(int, input().split()))
# players.sort(reverse=True)
# count = 0
# for i in range(n):
#     if sum(players[:i+1]) > d:
#         count += 1
# print(count)
n, d = map(int, input().split())
players = sorted(map(int, input().split()), reverse=True)

teams = []
for player in players:
    added = False
    for team in teams:
        if sum(team) + player > d:
            team.append(player)
            added = True
            break
    if not added:
        teams.append([player])

wins = sum(1 for team in teams if sum(team) > d)
print(wins)
