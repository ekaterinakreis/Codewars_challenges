# You will be given an array of events, which are represented by strings. The strings are dates in HH:MM:SS format.
#
# It is known that all events are recorded in chronological order and two events can't occur in the same second.
#
# Return the minimum number of days during which the log is written.

def check_logs(log):
    if len(log) == 0:
        return 0
    elif len(log) == 1:
        return 1

    counter = 1
    for x in range(1, len(log)):
        if log[x-1] >= log[x]:
            counter += 1
    return counter
