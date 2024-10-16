/*
If I want to find is there 1 or 0 in the ith index, then the operation:

  Formula:
  (n & (1 << i)) == 0 then ith index bit is 0

  Here, (1 << i) is the mask.

  Example:
    1 1 0 1
  & 1 0 0 0
  1 << 3
*/