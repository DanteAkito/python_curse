""" String-1 > make_tags

The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'



def make_tags(tag, word):
'<' + tag + '>' + word + '<' + '/' + tag '>' 

"""
"""

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
"""
def missing_char(str, n):
    front = str[:n]   # up to but not including n
    back = str[n+1:]  # n+1 through end of string
    return front + back


Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'

"""
"""

Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc

def front3(str):
  if len(str) <= 3 : 
    return str * 3
  else:
    return str[:3]*3
    """
"""
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'  

def front_back(str):
  if len(str) <= 1:
    return str
  else:
    x = str[1:-1]
    f = str[0]
    b = str[-1]
    return  b + x + f
"""
"""
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.


first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False


def first_last6(nums):
  for num in nums:
    x = nums[0]
    y = nums[-1]
  if x == 6 or y == 6:
    return True
  else:
    return False


"""

""" same_first_last
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True


def same_first_last(nums):
  for num in nums:
    x = nums[0]
    y = nums[-1]
  if len(nums) >=1 and x == y:
    return True
  else:
    return False
    
""" 
"""  String-1 > make_out_word


Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'


def make_out_word(out, word):
  x = out[:2]
  y = out[-2:]
  return x + word + y
"""
"""
List-1 > make_pi

Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

def make_pi():
  return [3, 1, 4]
  """


"""

List-1 > sum3

Given an array of ints length 3, return the sum of all the elements.

sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7

def sum3(nums):
    return sum(nums)



"""

"""
List-1 > rotate_left3
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
    

    def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

"""

"""


List-1 > reverse3
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
def reverse3(nums):
  return [nums[2], nums[1], nums[0]]
  """

  