jobs  = [(0, 6),(1, 4),(3, 5),(3, 8),(4, 7),(5, 9),(6, 10),(8, 11)]

def isOverlapping(job1, job2):
    if(job2[1] >= job1[1] and job2[0] < job1[1]):
        return True
    if(job2[1] >= job1[0] and job2[0] < job1[0]):
        return True
    if(job2[1] <= job1[1] and job2[0] >= job1[0]):
        return True
    return False

def find_compatible_jobs(jobs):
    jobs_map = {}
    for current_job in jobs:
        for job in jobs:
            if (current_job != job):
                if (not isOverlapping(current_job, job)):
                    if (current_job in jobs_map.keys()):
                        jobs_map[current_job].append(job)
                    else:
                        jobs_map[current_job] = [job]
    return jobs_map

def find_jobs_cost(jobs_map):
    jobs_cost = []
    for job in jobs_map.keys():
        num_valid_options = len(jobs_map[job])
        jobs_cost.append((job, num_valid_options))
    return sorted(jobs_cost, key=lambda x: x[1], reverse=True)

def choose_jobs(jobs_map, cost_map, choosen):
    for job, cost in cost_map:
        if (job in choosen):
            continue
        valid = True
        for other_job in choosen:
            if (job not in jobs_map[other_job]):
                valid = False
                break
        if (valid == True):
            choosen.append(job)
    print(choosen)

jobs_map = find_compatible_jobs(jobs)
jobs_cost = find_jobs_cost(jobs_map)
job = jobs_cost[0][0]
choose_jobs(jobs_map, jobs_cost, [job])

