#lab 9 function

#q1
def count_lower_upper(s):
    result = {"lowercase": 0, "uppercase": 0}
    for char in s:
        if char.islower():
            result["lowercase"] += 1
        elif char.isupper():
            result["uppercase"] += 1
    return result
sample_string = "Hello World!"
print(count_lower_upper(sample_string))

# qe 2
def compute(n):
    n_str = str(n)
    result = int(n_str) + int(n_str * 2) + int(n_str * 3) + int(n_str * 4)
    return result


for i in range(4, 8):
    print("compute({i}) = {compute(i)}")
    #3
def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average
# q 4
# Test the function
marks = [80, 90, 70, 85, 95]
total, avg = sum_avg(marks)
print(f"Total: {total}, Average: {avg}")
 # q 5
def ispangram(s):
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    return set(s.lower()) >= alphabet_set

# Test the function 
test_string = "The quick brown fox jumps over the lazy dog"
print(ispangram(test_string))  # Should return True
# q 6
def create_tuples(end):
    return [(x, x**2, x**3) for x in range(1, end + 1)]

# Test the function
result = create_tuples(5)
print(result)
#  q 7
def ispalindrome(s):
    s = ''.join(s.split()).lower()
    return s == s[::-1]

# Test the function
test_string = "A man a plan a canal Panama"
print(ispalindrome(test_string))  # Should return True
 #  q 8
 def convert(s):
    words = s.split()
    unique_sorted_words = sorted(set(words))
    return ' '.join(unique_sorted_words)

# Test the function
test_string = "apple banana apple cherry banana"
print(convert(test_string))  # Should return 'apple banana cherry'
 #q 9
def count_alpha_digits(s):
    count = {'alphabets': 0, 'digits': 0}
    for char in s:
        if char.isalpha():
            count['alphabets'] += 1
        elif char.isdigit():
            count['digits'] += 1
    return count

# Test the function
sample_string = "Hello123"
result = count_alpha_digits(sample_string)
print(result)
#q10
from collections import Counter

def frequency(s):
    words = s.split()
    word_count = Counter(words)
    return dict(sorted(word_count.items()))

# Test the function
sample_string = "apple banana apple cherry banana"
print(frequency(sample_string))


# q11
def create_list(list1, list2):
    return list(set(list1) & set(list2))

# Test the function
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(create_list(list1, list2))  # Should return [3, 4]
#q1
def prime_factors(n, i=2):
    if i * i > n:
        if n > 1:
            print(n)
        return
    if n % i == 0:
        print(i)
        prime_factors(n // i, i)
    else:
        prime_factors(n, i + 1)

# Test the function
prime_factors(56)
# q2
def binary_equivalent(n):
    if n == 0:
        return ""
    return binary_equivalent(n // 2) + str(n % 2)

# Test the function
print(binary_equivalent(10))  # Should return '1010'

 # q3
 def count_vowels(s):
    vowels = "aeiouAEIOU"
    if not s:
        return 0
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:])

# Test the function
print(count_vowels("Hello World"))
# q4
def reverse_list(lst):
    if not lst:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

# Test the function
print(reverse_list([1, 2, 3, 4]))
# q5
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

# Test the function
print(power(2, 3))  # Should return 8

# q6
def average(lst, total=0, count=0):
    if not lst:
        return total / count if count != 0 else 0
    return average(lst[1:], total + lst[0], count + 1)

# Test the function
print(average([1, 2, 3, 4, 5]))  # Should return 3.0
# q7
def average(lst, total=0, count=0):
    if not lst:
        return total / count if count != 0 else 0
    return average(lst[1:], total + lst[0], count + 1)

# Test the function
print(average([1, 2, 3, 4, 5]))  # Should return 3.0
#q8
def string_length(s):
    if not s:
        return 0
    return 1 + string_length(s[1:])

# Test the function
print(string_length("Hello"))






    
