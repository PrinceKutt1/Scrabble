letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


# combine letters to points into a dictionary to map a letter to its point value

letter_to_points = {key.upper():value for key, value in zip(letters,points)}

# Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    point_total+=letter_to_points.get(letter,0)
  return point_total

  
brownie_points = score_word("BROWNIE") 
print(brownie_points)



player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}
player_to_points = {}


def play_word(player,word):
  player_to_words[player].append(word.upper())
  return player_to_words

def update_point_totals(player_to_words,player_to_points):
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points+= score_word(word)
    player_to_points[player] = player_points
  return player_to_points

print(play_word("player1","brownie"))
print(update_point_totals(player_to_words,player_to_points))

print(letter_to_points)
