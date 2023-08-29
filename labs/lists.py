# As you may know, an anagram is a new word created by reorganizing all the letters in a word.
# This list of anagrams are all based on the word "Stop"
anagrams = ["plots", "post", "stop", "puts", "tops"]

# Run this program after you try each step and see if it worked.
# At the very bottom of this file is a line of code that prints out the list after your code is run.
# You're welcome to print additional debugging statements if you need.

# 1. Print out the third word in the list using bracket notation.
# print(anagrams[2])

# 2. The word "opts" is also an anagram of the word "stop". Find a way to add "opts" to the end of the list.
anagrams.append("opts")

# 3. The word "puts", on the other hand, is not an anagram of the word "stop". Find a way to replace it with the word "pots".


# 4. Use the documentation to figure out what the method ".pop()" does.
#   Now use it to remove the word "plots" (which isn't a correct anagram of "stop") from our list.
anagrams.pop(0)

# 5. Put the final list of anagrams in alphabetical order, and SAVE it.
# (If you encounter an error here, it's probably because Python is sorting it temporarily, but then immediately restoring it to the original order.)
anagrams.sort()

# This code prints the list after you've manipulated it above.
# print(anagrams)

# LEVEL 2: At this point, the tasks will get more challenging, because you'll work with datasets too large to handle by just looking at it and reading it.
# The lists used in the second half of this lab will be stored in a neighboring file called "other_lists.py".
# If you'd like to look at that file, you certainly may, but do your work here.
# This line of code connects the data.
import other_lists

# Pro-tip: to make this easier, comment out the line "print(anagrams)" above so that you aren't printing extra information.
#
#     The first list is called "fortunes" and contains fortune-cookie style fortunes.
#     Remeber to access the list with "other_lists.fortunes" because is is in a different file.
#
#  6. Print out the 10th fourtune from the list.
# print(other_lists.fortunes[9])
#
#
# #  7. Print out fortunes 12, 13, and 14 from the list. There are several ways to do this, and any way is totally fine.
# print(other_lists.fortunes[11:14])

import random     # You're going to need a method from the random library for this next part.
# 8. Print out a random fortune from the list.
# print(random.randint(0, len(other_lists.fortunes)-1))
#
# # 9. This list is huge, so it'd be helpful to know how many fortunes are listed. Find a way to print out the number of fortunes in the list.
# print(len(other_lists.fortunes))

# 10. Challenge: Out of all the fotunes that are there, it'd mess up the program if some were listed twice, but with a list that big, it could happen.
# Find a way to check and see whether any of the fortunes are duplicates - make a separate list of those fortunes. 
# # Once you have the list of duplicated fortunes, find a way to delete those duplicates.
# duplicate_fortunes = []
# for i in range(len(other_lists.fortunes)):
#     for j in range(i+1, len(other_lists.fortunes)):
#         if other_lists.fortunes[i] == other_lists.fortunes[j]:
#             duplicate_fortunes.append(other_lists.fortunes[i])
# print(duplicate_fortunes)
#
# for fortune in duplicate_fortunes:
#     other_lists.fortunes.remove(fortune)
# print(len(other_lists.fortunes
class_names = ['Alison', 'Anushka', 'Audrey', 'Mashrafi', 'Mauricio', 'Maxime', 'Nhaomi', 'Praveena', 'Raekwon', 'Sanila', "Ta'Ziyah", 'Taher', 'Taralynn', 'Thessaly', 'Vi', 'Zanggar']
print(f'${class_names}')