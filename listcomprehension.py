sentence = "georgina loves music so much"
words = sentence.split()
print(words)

print([len(word) for word in words])
print([len(word) for word in words if word != "so"])

def positive_numbers(x): return x >0
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print(list(filter(positive_numbers,numbers)))


def even_number(x): return x%2 ==0
numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
print(list(filter(even_number,numbers)))


words = ["hello", "my", "name", "is", "Sam"]
for w in words: print ((w.upper(),len(w)))