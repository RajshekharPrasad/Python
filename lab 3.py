def Vowels(string):
  vowels = "aeiouAEIOU"
  count = 0
  for char in string:
    if char in vowels:
      count += 1
  return count

string = input("Enter a string: ")
print(Vowels(string))

#Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case

def to_lower(string):
  result = ''
  for char in string:
    if 'A' <= char <= 'Z':
      result += chr(ord(char) + 32)
    else:
      result += char
  print(result)

def to_upper(string):
  result = ''
  for char in string:
    if 'a' <= char <= 'z':
      result += chr(ord(char) - 32)
    else:
      result += char
  print(result)

def toggle_case(string):
  result = ''
  for char in string:
    if 'a' <= char <= 'z':
      result += chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
      result += chr(ord(char) + 32)
    else:
      result += char
  print(result)

string = input("Enter a string: ")
to_lower(string)
to_upper(string)
toggle_case(string)
# Accept two strings from user. Check whether one string is there in another string and print output.

def check_substring(str1, str2):
  if str2 in str1:
    print(str2, "is a substring of", str1)
  else:
    print(str2, "is not a substring of", str1)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
check_substring(string1, string2)
def remove_string(onestring, removestring):
    # Use the built-in replace method to remove the removestring
    finalstring = onestring.replace(removestring, "")
    return finalstring

# Example usage:
onestring = "abcdef"
removestring = "cd"
finalstring = remove_string(onestring, removestring)
print(finalstring)  # Output: "abef"
