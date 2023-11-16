def repetitions(s: str) -> int:
  max_count = 0
  count = 1

  for i in range(1, len(s)):
    if s[i] == s[i-1]:
      count += 1
    else:
      max_count = max(max_count, count)
      count = 1

  return max(max_count, count)