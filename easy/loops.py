# Prepare > Python > Introduction > Loops

# Task
# The provided code stub reads and integer, , 
# from STDIN. For all non-negative integers , print .
# Print the square of each number on a separate line.
# n = 3
# output [0, 1, 4] # on separete line

def fn(n):

    for i in range(0, n):
        print(i**2)


if __name__ == '__main__':

    a = fn(3)
