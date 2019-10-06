""" Assignment Five: Lab Assignment 5 - Reversing a List with Recursion - Shaotong Wen """
# import string library function
import string


def reverse_a_list(my_list):
    """ reverse the order of my_list """
    print(len(my_list))
    length = len(my_list)
    if length == 1:
        return my_list
    else:
        return reverse_a_list(my_list[1:]) + [my_list[0]]


def main():

    """using list comprehension to fill the list of letters"""
    alphabet = [alphabet_list[0] for alphabet_list in string.ascii_lowercase]

    print(alphabet)
    print(reverse_a_list(alphabet))
    print(alphabet)


if __name__ == "__main__":
    main()

""" ----- SAMPLE RUN -----

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j',
'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


"""