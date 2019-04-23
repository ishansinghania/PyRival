def mergesort(iterable, key=lambda x: x, reverse=False):
    A = list(iterable)
    B = A[:]
    n = len(A)

    for i in range(0, n - 1, 2):
        if key(A[i]) > key(A[i ^ 1]):
            A[i], A[i ^ 1] = A[i ^ 1], A[i]

    width = 2
    while width < n:
        for i in range(0, n, 2 * width):
            R1, R2 = min(i + width, n), min(i + 2 * width, n)
            j, k = R1, i

            while i < R1 and j < R2:
                if key(A[i]) > key(A[j]):
                    B[k] = A[j]
                    j += 1
                else:
                    B[k] = A[i]
                    i += 1
                k += 1

            while i < R1:
                B[k] = A[i]
                k += 1
                i += 1

            while k < R2:
                B[k] = A[k]
                k += 1

        A, B = B, A
        width *= 2

    if reverse:
        A.reverse()

    return A
