def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

a = [float(x) for x in input("Enter numbers: ").split()]

print (mean(a))
