# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
a = float(input("введіть число а: "))
b = float(input("введіть число b: "))
c = float(input("введіть число c: "))
if a > b:
    max = a
    print("max={0}".format(max))
else:
    max = b
    print("max={0}".format(max))
if b > c:
    min = c
    print("min={0}".format(min))
else:
    min = b
    print("min={0}".format(min))
R = min*min
print("R={0}".format(R))
S=R+max
print("S={0}".format(S))
