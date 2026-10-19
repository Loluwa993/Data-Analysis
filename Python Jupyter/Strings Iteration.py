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




# function generates password from username by shifting the input to the right, and starting with last character
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password


# this second function turns the input upside down
def password_generator_2 (user_name):
  password = ""
  for i in range(0, len(user_name)):
    password += user_name[(len(user_name) - 1) - i ]
  return password

new_password = password_generator_2 ("loluwa")
print(new_password)
