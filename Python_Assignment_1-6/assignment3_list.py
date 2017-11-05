# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing "OK" when each function is correct.
# The starter code for each function includes a "return"
# which is just a placeholder for your code.
# It"s ok if you do not complete all the functions, and there
# are some additional functions to try in assignment4_list.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    count = 0
    for word in words:
            if(len(word)==0 or len(word)==2):
                 continue
            elif (word[0] == word[-1]):
                count += 1

    return count

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with "x" first.
# e.g. ["mix", "xyz", "apple", "xanadu", "aardvark"] yields
# ["xanadu", "xyz", "aardvark", "apple", "mix"]
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    listX=[]
    listR=[]
    for word in words:
        if(word[0]=='x' or word[0]=='X'):
            listX.append(word)
        else:
            listR.append(word)
    print(listX+listR)
    return sorted(listX)+sorted(listR)


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
#from operator import itemgetter, attrgetter
def sort_last(tuples):
    l= sorted(tuples, key=lambda tuple: tuple[1])
    return l



# Simple provided test() function used in main() 1to print
# what each function returns vs. what it"s supposed to return.
def test(got, expected):
    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print("%s got: %s expected: %s" % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print("match_ends")
    test(match_ends(["aba", "xyz", "aa", "x", "bbb"]), 3)
    test(match_ends(["", "x", "xy", "xyx", "xx"]), 2)
    test(match_ends(["aaa", "be", "abc", "hello"]), 1)

    print()
    print("front_x")
    test(front_x(["bbb", "ccc", "axx", "xzz", "xaa"]),["xaa", "xzz", "axx", "bbb", "ccc"])
    test(front_x(["ccc", "bbb", "aaa", "xcc", "xaa"]),["xaa", "xcc", "aaa", "bbb", "ccc"])
    test(front_x(["mix", "xyz", "apple", "xanadu", "aardvark"]),["xanadu", "xyz", "aardvark", "apple", "mix"])


    print()
    print("sort_last")
    test(sort_last([(1, 3), (3, 2), (2, 1)]),[(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),[(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),[(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == "__main__":
    main()
