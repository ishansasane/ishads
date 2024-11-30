def isSafe(processes,available,max_need,allocation):
    n=len(processes)
    m=len(available)

    need=[[max_need[i][j]-allocation[i][j] for j in range(m)]for i in range(n)]
    print(need)

    finish=[False]*n

    work=avaliable[:]

    safe_sequence=[]

    while len(safe_sequence)<n:
        found_processes=False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j]<=work[j] for j in range(m)):
                    for j in range(m):
                        work[j]+=allocation[i][j]
                    finish[i]=True
                    safe_sequence.append(processes[i])
                    found_processes=True
                    break
        if not found_processes:
            return False,[]
    print(safe_sequence)
    return True,safe_sequence

if __name__ == "__main__":
    processes=[0,1,2,3]
    avaliable =[3,3,2]
    maxneed=[
        [7,5,3],
        [3,2,2],
        [9,0,2],
        [2,2,2]
    ]
    allocation=[
        [0,1,0],
        [2,0,0],
        [3,0,2],
        [2,1,1]
    ]
    isSafe(processes,avaliable,maxneed,allocation)
