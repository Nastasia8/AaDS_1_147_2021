def teams(studs):
    team1 = []
    team2 = []
    team3 = []
    team4 = []

    for i in studs:
        if i[0] == '1':
            team1.append(i)
        if i[0] == '2':
            team2.append(i)
        if i[0] == '3':
            team3.append(i)
        if i[0] == '4':
            team4.append(i)
    for i in team1:
       print(i)
    for i in team2:
        print(i)
    for i in team3:
        print(i)
    for i in team4:
        print(i)


def main():
    n = int(input())
    studs = [] * n
    for i in range(n):
        studs.append(input())
    teams(studs)
main()