problem = open('several_threes.txt', 'r').readline()
while '{' not in problem:
    problem = problem.decode('hex')
print problem