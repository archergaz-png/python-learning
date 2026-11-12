def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

n = int(input())
numbers = [int(input()) for _ in range(n)]
print(count_even(numbers))
