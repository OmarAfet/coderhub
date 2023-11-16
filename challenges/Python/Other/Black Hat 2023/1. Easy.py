def perfect_number_finder(num: int) -> bool:
  sum = 0
  for i in range(1, num):
    if num % i == 0:
      sum += i
  return sum == num