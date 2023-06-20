# given an array of intervals, where each interval represents a
# start time and an end time (like [1,3]), determine the smallest
# number of intervals that need to be removed so that no intervals
# overlap. "touch" is allowed, so [1,3] and [3,5] could stay.
# e.g. for [[1,3],[3,5],[2,4],[6,8]] we need to return 1 because
# 1 interval (namely [2,4]) needs to be removed

import numpy as np
import sys
intervals = np.array([[1,3],[3,5],[2,4],[6,8],[7,9]])

# plan: loop through intervals once, creating a hash table where
# each interval is paired with the intervals it overlaps with;
# then, remove the interval with the most conflicts, update the
# hash table, and repeat until there are no further conflicts

def min_to_delete(intervals):
    intervals.sort(axis=0)
    end_prev = -1
    count = 0
    offenders = {}
    for intr in intervals:
        start_curr = intr[0]
        if end_prev!=-1:
            if start_curr<end_prev:
                if offenders.get(str(prev_intr))!=True:
                    count += 1
                    offenders.update({str(intr):True})
        end_prev = intr[1]
        prev_intr = intr
    return count

print(min_to_delete(intervals))
