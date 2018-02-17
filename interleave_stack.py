#!/usr/bin/env python3


def interleave_stack(stack):
    """
    Given a stack of N elements, interleave the first half of the stack
    with the second half reversed using only one other queue.
    This should be done in-place.

    For example,
    if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3].
    If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
    """

    n = len(stack)
    queue = []    # queue (auxiliary space)
    for x in range(n, 0, -1):
        for i in range(x-1):
            queue.append(stack.pop())
        for i in range(len(queue)):
            stack.append(queue.pop(0))


if __name__ == "__main__":
    stack = [1, 2, 3, 4, 5]
    interleave_stack(stack)
    print(stack)
