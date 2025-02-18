count = 1
even_count = 0
while even_count < 4:
    count += 1
    if count % 2 != 0:
        continue  # Skip odd numbers
    print(count)
    even_count += 1
