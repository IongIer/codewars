def digital_root(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    if len(str(sum)) == 1:
        return sum
    else:
        return digital_root(sum)
