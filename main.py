# Mad Libs Game

# Getting user inputs for the Mad Libs
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
adjective1 = input("Enter an adjective: ")
adverb1 = input("Enter an adverb: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb: ")
adjective2 = input("Enter another adjective: ")

# Story template
story = f"""
Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} {adverb1}.
One day, the {noun1} found a {adjective2} {noun2} and decided to {verb2} it.
Everyone in the town was amazed at how {adjective1} the {noun1} was. 
And so, the {adjective1} {noun1} and the {adjective2} {noun2} became the best of friends.
"""

# Print the final Mad Libs story
print("\nHere is your Mad Libs story:")
print(story)
