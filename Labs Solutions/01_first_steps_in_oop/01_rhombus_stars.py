"""
n = 3
  *             # i: 2 spaces, (n -1 - i spaces), 1 star
 * *            # i: 1space, (n -1 - i spaces), 1 space, 1 star
* * *           # i: 0 spaces, 1 star, 1 space, 1 star, 1 space
 * *
  *

n = 4
   *
  * *
 * * *
* * * *
 * * *
  * *
   *

"""


# def get_line(i, n):
#     spaces_count = n - 1 - i
#     stars_count = i + 1
#     return " " * spaces_count + "* " * stars_count
#
# def print_line(n):
#     print(get_line(n - 1, n - 1))
#
# def print_rhombus(n):
#     for i in range(0, n, 1):
#         print(get_line(i, n))
#     for j in range(n - 2, - 1, - 1):
#         print(get_line(i, n))
#
# print_rhombus(3)
# print_rhombus(4)


def print_row(figure_size, row_size):
    print(" " * (figure_size - row_size), end="")
    for col in range(1, row + 1):
        print("* ", end="")
    print()


n = int(input())

for row in range(1, n + 1):
    print_row(n, row)

for row in range(n - 1, -1, -1):
    print_row(n, row)
