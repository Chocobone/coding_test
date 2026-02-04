import sys

word = str(sys.stdin.readline())

total_len = len(word)
collon = word.count(':')
under_bar = word.count('_')

result = total_len-1 + collon + 5 * under_bar

print(result)