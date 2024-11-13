number_1: int = 12

number_2 = 15.15

a: int = 5
b: int = 10
c = [2, 5, 1, 3, 6]

print(
    number_1,
    number_2,
)

string_1 = 'hello "world"'
string_2 = "hello 'world'"
string_3 = "hello \\ \"world\" \\"
string_4 = "\n"
my_st = "Can I take some cookies?"

print(
    string_1,
    string_4,
    string_2,
    string_4,
    string_3,
)

def add_numbers(a, b):
    return a + b

def sum_of_list(c):
    return sum(c)

def join_strings(string_1, string_2):
    return "_".join((string_1, string_2))

def split_string(my_st):
    return my_st.split(" ")

d1 = add_numbers(a, b)
d2 = sum_of_list(c)
d3 = join_strings(string_1, string_2)
d4 = split_string(my_st)

print(d1)
print(d2)
print(d3)
print(d4)
