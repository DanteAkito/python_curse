"""
def make_tags(tag, word):
'<' + tag + '>' + word + '<' + '/' + tag '>' 

#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.


#extra_end('Hello') → 'lololo'
#extra_end('ab') → 'ababab'
#extra_end('Hi') → 'HiHiHi'




def extra_end(str):
  return str[-2:] * 3  #mine


def extra_end(str):
end = str[-2:]
return end + end + end


#Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".


def first_two(str):
  if len(str) >= 2:
    return str[:2]
  else:
    return str


def first_two(str):
if len(str) < 2:
    return str
else:
    return str[:2]  #mine

#Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).    

    def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  else:
    return a + b + a


#Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

    
  def non_start(a, b):
  return a[1:] + b[1:]  


#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  else:
    return False



#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


#not_string('candy') → 'not candy'
#not_string('x') → 'not x'
#not_string('not bad') → 'not bad'


#def not_string(str):
 #   if len(str) >= 3 and str[:3] == "not":
  #      return str
   # else: 
    #    return "not " + str

!!! 
"""
def missing_char(str, n):
    front = str[:n]   # up to but not including n
    back = str[n+1:]  # n+1 through end of string
    return front + back


Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'