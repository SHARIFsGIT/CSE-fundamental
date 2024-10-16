/*
    a = 13
      = 1 1 0 1
          ^
    I want to change the 2nd bit.

    1 1 0 1
    0 1 0 0 (Mask)
    -------
    1 0 0 1

    Formula:
    a ^ (1 << x)

    XOR operation:
        1 ^ 0 = 1
        0 ^ 0 = 0
    So, x ^ 0 = x

*/