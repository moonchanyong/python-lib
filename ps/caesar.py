def pop(arr):
    return arr[1:]

class task:
    def __init__(self, time):
        self.jobNumber = 0
        self.fullTime = time
        self.current = 0

    def ager(self):
        self.current += 1
        if self.fullTime == self.current:
            self.current = 0
            ret = self.jobNumber
            self.jobNumber = 0
            return ret
    def isReady(self):
        return True if self.jobNumber == 0 else False

    def assign(self, jobNumber):
        self.current = 0
        self.jobNumber = jobNumber


def getCoreNumber(n, cores):
    answer = 0
    tasker = []
    for j in cores:
        tasker.append(task(time=j))

    tasks = range(1, n+1)

    while tasks.__len__() > 0 :
        # aging
        for core in tasker:
            core.ager()

        # give task
        for core in tasker:
            if core.isReady():
                core.assign(pop(tasks))
            if tasks.__len__() == 0:
                return tasker.index(core)+1

    return answer



print(getCoreNumber(6, [1, 2, 3]))
