letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 2, 2, 2, 1, 3, 3, 3, 1, 4, 3, 1, 2, 3, 1, 3, 5, 1, 1, 1, 2, 3, 3, 4, 3, 5]

# combining the two list into a dict
letter_to_points = {key : value for key, value in zip(letters, points)}

# updating letter_to_points to include lower cases 
for letter in letters:
  letter_to_points[letter.lower()] = letter_to_points.get(letter,0)

print(letter_to_points)

# creating a function that score words
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter,0)
  return point_total

# testing the function
brownie_points = score_word("BROWNIE")
print(brownie_points)


# creating a dict for player to words/points map
player_to_words = {"player1":["BLUE","TENNIS","EXIT"], "wordNerd":["EARTH","EYES","MACHINE"], "Lexi Con":["ERASER","BELLY","HUSKY"], "Prof Reader":["ZAP","COMA","PERIOD"]}

player_to_points = {}


# function to add words played to player_to_words
def play_word(player, word):
  if player in player_to_words.keys():
    player_to_words[player].append(word)
  else:
    player_to_words[player] = [word]

# loop function to iterate through items in player_to_word
def update_points_totals():
  global player_to_points
  player_to_points = {}
  for player, words in player_to_words.items():
    # print(f"{player} : {words}".format(player, words))
    # iterate through the word list of each player and sum up the score
    player_points = 0
    for word in words:
      player_points += score_word(word)
      # print(player_points)
    # insert the player and score in dict
    player_to_points[player] = player_points

# checking the updated player_to_points dict
print(player_to_points)




