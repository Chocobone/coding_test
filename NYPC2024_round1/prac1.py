import sys

m = int(sys.stdin.readline())

job_list = []
for _ in range(m):
    job = str(sys.stdin.readline())
    job = job[:-1]
    job_list.append(job)

n = int(sys.stdin.readline())
for _ in range(n):
    made_job = str(sys.stdin.readline())
    made_job = made_job[:-1]
    for a in job_list:
        if(a==made_job):
            job_list.remove(a)
            break

t = len(job_list)
print(t)
for i in range(t):
    print(job_list[i])
