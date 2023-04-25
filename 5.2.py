# write a program with takes as input an array of digits encoding as non-negative decimal integer D and updates the array to represent the integer D + 1 

# Example: [1,2,9] -> [1,3,0]

A = [1,2,9]

def plus_one(A: list[int]) -> list[int]:
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    else:
        if A[i] == 10:
            A[0] = 1
            A.append(0)
        return A