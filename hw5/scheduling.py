#Group 7: Joshua Steward, Lowell Batacan
# Assignment 5
# 11/20/2016

class Activity:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit
    def __lt__(self, other):
        return self.finish < other.finish
    def displayActivity(self):
        print("Start: ", self.start, " - Finish: ", self.finish, " - Profit: ", self.profit, "\n")

# Declare array of activities.
activities = []

f = open('data.txt', 'r')
characters = []
with f as file:
    characters = file.readline()

start = 0
finish = 0
profit = 0
newActivity = False
startRead = False
finishRead = False
profitRead = False
for currentChar in characters:
    if currentChar == '(':
        newActivity = True
        startRead = True
        continue
    elif currentChar == ',' or currentChar == ';':
        continue
    if newActivity is True and startRead is True:
        start = int(currentChar)
        startRead = False
        finishRead = True
    elif newActivity is True and finishRead is True:
        finish = int(currentChar)
        finishRead = False
        profitRead = True
    elif newActivity is True and profitRead is True:
        profit = int(currentChar)
        profitRead = False
        newActivity = False
        activities.append(Activity(start, finish, profit))

print("Activities")
for act in activities:
    act.displayActivity()
print()

activities.sort()

print("Sorted Activities")
for act in activities:
    act.displayActivity()

# Create array for finish times. (u_i)
finish = []

# Compare finish time with previous to determine if they're in the same cluster.
finish_time = 0

# u_0 will be 0.
finish.append(finish_time)

# Clustering together similar finish lines.
# Each index will be the value of one of our u's.
for x in activities:
    if x.finish != finish_time:
        finish.append(x.finish)
        finish_time = x.finish
    else:
        pass

# Finish times
print("Finish Times")
print(finish)

# Array of activities' size. Contains the indices of u.
H = []

# We will compare start times of each activity to the latest finish time.

for activity in activities:
    for y in range(0, len(finish)):
        if activity.start >= finish[len(finish) - 1 - y]:
            ##Append the index of the finish time.
            H.append(len(finish) - 1 - y)
            # Append value of finish time?
            #H.append(finish[len(finish) - 1 - y])
            break

print()
print("H")
print(H)

max = []
max.append(activities[1])
max.append(activities[3])
k = len(finish)
n = len(activities)



#An array is defined with length as the number of unique finish times.
# Then, for the number of finish times, max is re-set, and for all the activities, they are checked for if the finish time of the current activity
#   is equal to the current iteration of the finish times array.
#
#The max variable is then assigned based on this check.
#  Next, before the original for loop continues,
#  a check is made for if the current iteration in
#  the unique finish times is greater than max,
#  and if it is, max is set to this.
#  Finally, the array is incremented as max.
#
def WAS():
    A = [0] * k
    A[0] = 0
    for j in range(1, k):
        max = 0
        count = 1
        for i in activities:
            if i.finish == finish[j]:
                #if (i.profit + A[H[count]]) > max:
                    #max = i.profit + A[H[count]]
                pass
            count = count + 1
        if A[j - 1] > max:
            max = A[j - 1]
        A[j] = max
    return A

print("Maximum profit activities: ")

for i in max:
    i.displayActivity()
A = WAS()
print(A)









