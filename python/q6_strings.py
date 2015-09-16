# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count >= 10:
        print 'Number of donuts: many'
    else:
        print 'Number of donuts: ' + str(count)

    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    """

donuts(4)

donuts(9)

donuts(10)

donuts(99)

def both_ends(s):
    if len(s) < 2:
        print ''
    else:
        print s[:2] + s[-2:]

    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    """

both_ends('spring')

both_ends('Hello')

both_ends('a')

both_ends('xyz')


def fix_start(s):
    first_char = s[:1]
    length = len(s)
    remaining_char = s[(-length+1):]
    temp_find = remaining_char.find(first_char)
    if temp_find == -1:
        print s
    else:
        print first_char + remaining_char.replace(first_char, '*')

    """
    #Given a string s, return a string where all occurences of its
    #first char have been changed to '*', except do not change the
    #first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    #string is length 1 or more.
    """

fix_start('babble')

fix_start('aardvark')

fix_start('google')

fix_start('donut')


def mix_up(a, b):
    first_a = a[:2]
    first_b = b[:2]
    remaining_a = a[-len(a)+2:] 
    remaining_b = b[-len(b)+2:]
    new_a = first_b + remaining_a
    new_b = first_a + remaining_b
    print new_a + " " + new_b
    
    """
    #Given strings a and b, return a single string with a and b
    #separated by a space '<a> <b>', except swap the first 2 chars of
    #each string. Assume a and b are length 2 or more.
    """

mix_up('mix', 'pod')

mix_up('dog', 'dinner')

mix_up('gnash', 'sport')

mix_up('pezzy', 'firm')


def verbing(s):
    if len(s) >= 3:
        if s[-3:] == "ing":
            print s + "ly"
        else:
            print s + "ing"
    else:
        print s

    """
    #Given a string, if its length is at least 3, add 'ing' to its end.
    #Unless it already ends in 'ing', in which case add 'ly' instead.
    #If the string length is less than 3, leave it unchanged. Return
    #the resulting string.
    """

verbing('hail')

verbing('swiming')

verbing('do')


def not_bad(s):
    not_loc = s.find("not")
    bad_loc = s.find("bad")
    if int(not_loc) == -1:
        print s
    elif int(not_loc) < int(bad_loc):
        print s[:not_loc]+ "good"+ s[bad_loc+3:]
    else:
        print s

    """
    #Given a string, find the first appearance of the substring 'not'
    #and 'bad'. If the 'bad' follows the 'not', replace the whole
    #'not'...'bad' substring with 'good'. Return the resulting string.
    #So 'This dinner is not that bad!' yields: 'This dinner is
    #good!'
    """

not_bad('This movie is not so bad')

not_bad('This dinner is not that bad!')

not_bad('This tea is not hot')

not_bad("It's bad yet not")

def front_back(a, b):
    a_length = len(a)
    b_length = len(b)
    total_length = int(a_length)+int(b_length)
    if a_length%2 == 0:
        a_front = a[:int(a_length)/2]
        a_back = a[-int(a_length)/2:]
    else:
        a_front = a[:(int(a_length)/2)+1]
        a_back = a[-(int(a_length)/2):]
    if b_length%2 == 0:
        b_front = b[:int(b_length)/2]
        b_back = b[-int(b_length)/2:]
    else:
        b_front = b[:(int(b_length)/2)+1]
        b_back = b[-(int(b_length)/2):]
    print a_front + b_front + a_back + b_back


    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    """

front_back('abcd', 'xy')

front_back('abcde', 'xyz')

front_back('Kitten', 'Donut')
