# function to compare if a string contains another smaller string
def contains(big_strings, little_strings):
  return little_strings in big_strings

# function to return character present in two strings
def common_letters (string_one, string_two):
  common_list = []
  for character in string_one:
    if (character in string_two) and not (character in common_list):
      common_list.append(character)
  return common_list
