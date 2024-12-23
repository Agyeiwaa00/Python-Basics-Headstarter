def count_code(s):
    count = 0
    for j in range(len(s) - 3):
        if s[j:j+2] == 'co' and s[j + 3] == 'e':
          count += 1
    
    return count

result = count_code("ghjcomenaj")
print(result)
