# # 1. Write a function called shout that takes in a string as an argument and returns it in all caps.
# def shout(string):
#     return string.upper()
#
#
# # 2. Write a function called whisper that takes in a string as an argument and returns it in all lowercase.
# def whisper(string):
#     return string.lower()
#
#
# # 3. Write a function called how_many_letters that takes in a string as an argument and returns the number of letters in that string.
# def how_many_letters(string):
#     return len(string)
#
#
# # 4. Write a function called work_it that takes in a string as an argument and returns it backwards and with the first letter capitalized.
# #    For example, work_it("I put my thing down flip it and reverse it") would return "Ti esrever dna ti pilf nwod gniht ym tup i"
def work_it(string):
    return string[::-1].capitalize()
#
#
# # 5. Write a function called repeat_it that takes in a word and a number, and returns the word that many times.
# #    For example, repeat_it("Banana", 3) would return "BananaBananaBanana"
def repeat_it(word, number):
    return word * number
#
#
# # 6. Write a function called will_it_nametag that takes in a name and a number, and tells you whether the name can be printed on a nametag that size.
# #    For example, will_it_nametag("Peter", 10) will return True, but will_it_nametag("Peter", 4) will return False, because "Peter" is 5 letters long, and needs at least 5 spaces to fit on a nametag.
# def will_it_nametag(name, number):
#     return len(name) <= number
#
#
# # 7. Write a function called add_liar that takes in two numbers and prints out a lie like "Sorry, I don't know how to add ___ and ___."
# #    BUT even though it *prints* that it doesn't know the answer, have the function return the correct answer anyways.
# def add_liar(x1, x2):
#     print(f"Sorry, I don't know how to add {x1} and {x2}.")
#     return x1 + x2
#
#
# # 8. CHALLENGE: Now that you've written all these functions, try combining them. what would happen if you tried to call repeat_it(work_it("Stressed"), 3) ?
print(repeat_it(work_it("Stressed"), 3))

# 9. MEGA CHALLENGE: Write a function called doubler that takes in a string and returns it with every letter doubled.
#    For example, doubler("Lost in the Woods") would return "LLoosstt iinn tthhee WWooooddss"
# def doubler(string):
#     return "".join([letter * 2 for letter in string])
#
# def doubler_2(str):
#     new_str = ""
#     for letter in str:
#         new_str += letter * 2
#     return new_str
#
# # 10. SUPER MEGA CHALLENGE: Head to https://codingbat.com/python/String-2 and attempt some of the challenges there!
#
# print(doubler("Lost in the Woods"))

# def count_code(str):
#     count = 0
#     for i in range(len(str) - 3):
#         if str[i] == "c" and str[i + 1] == "o" and str[i + 3] == "e":
#             count += 1
#     return count
#
# print(count_code("c"))
#
# def end_other(a, b):
#     a = a.lower()
#     b = b.lower()
#     return a.endswith(b) or b.endswith(a)
#
# def xyz_there(str):
#     for i in range(len(str) - 2):
#         if str[i] != "." and str[i + 1] == "x" and str[i + 2] == "y" and str[i + 3] == "z":
#             return True
#     return False
#
# print(xyz_there("xyz"))


# Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value,
# ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may
# assume that the array is length 3 or more.
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
    nums.sort()
    nums = nums[1:-1]
    return sum(nums) // len(nums)

print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))