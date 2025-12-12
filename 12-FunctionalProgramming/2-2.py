def f(a):
    return len(a)

names = [
    'James',
    'Emily',
    'William',
    'Olivia',
    'Benjamin',
    'Sophia',
    'Henry']

print(sorted(names, key=f, reverse=True))