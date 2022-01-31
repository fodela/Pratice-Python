# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.

# Constraints

# Output Format

# Print the runner-up score.

# Sample Input 0

# 5
# 2 3 6 6 5
# Sample Output 0

# 5
# Explanation 0

# Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

# create list of scores
arr = list(arr)

# get the highest score
highest_score = max(arr)

# find out how many times the highest score occurred
no_of_highest_score = arr.count(highest_score)

# remove the highest to find the second highest
for i in range(no_of_highest_score):
    arr.remove(highest_score)

print(max(arr))