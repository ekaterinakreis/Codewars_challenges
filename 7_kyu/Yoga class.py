# Lets imagine a yoga classroom as a Square 2 D Array of Integers classroom,
# with each integer representing a person, and the value representing their skill level.
#
# classroom = [
#     [3, 2, 1, 3],
#     [1, 3, 2, 1],
#     [1, 1, 1, 2],
# ]
#
# poses = [1, 7, 5, 9, 10, 21, 4, 3]
# During a yoga class the instructor gives a list of integers poses representing a yoga pose
# that each person in the class will attempt to complete.
# A person can complete a yoga pose if the sum of their row and their skill level is greater
# than or equal to the value of the pose.
# Task
# Your task is to return the total amount poses
# completed for the entire classroom.

import numpy as np


def yoga(classroom, poses):
    if classroom == [] or poses == []:
        return 0
    classroom = np.array(classroom)
    total_poses = 0
    for row in classroom:
        row_total = sum(row)
        row += row_total
        for pose in poses:
            total_poses += np.sum([pose <= row])
    return total_poses

# ____________________________
def yoga1(classroom, poses):
    result = 0
    for row in classroom:
        s = sum(row)
        result += sum(s+r >= p for r in row for p in poses)
    return result