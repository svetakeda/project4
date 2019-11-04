# This program is a game, where a user has to guess words, given by another user backwards.
# It gives a user 3 tries and if a user doesn't guess it - he loses.
# The given word also should contain from 3 to 8 symbols.
name1 = input("Введите имя первого игрока: ")                      # Program asks a name of a player.
word1 = input("Загадайте слово: ")                                 # Program asks a word and a word backwards.
word2 = input("Слово наоборот: ")
max_counter = 3
counter = 1
while counter < max_counter:                                      # Cycle works while counter less than 3.
    if len(word1) == 3:
        if (word1[0]) == (word2[2]) and word1[1] == word2[1]:
            print("Поздравляем, ", name1, ", Вы угадали!")
            break
    if len(word1) == 4:
        if word1[0] == word2[3] and word1[1] == word2[2]:
            print("Поздравляем, ", name1, ", Вы угадали!")
            break
    if len(word1) == 5:
        if word1[0] == word2[4] and word1[1] == word2[3] and word1[2] == word2[2]:
            print("Поздравляем, ", name1, ", Вы угадали!")
            break
    if (len(word1)) == 6:
        if word1[0] == word2[5] and word1[1] == word2[4] and word1[2] == word2[3]:
            print("Поздравляем, ", name1, ", Вы угадали!")
            break
    if (len(word1)) == 7:
        if word1[0] == word2[6] and word1[1] == word2[5] and word1[2] == word2[4] and word1[3] == word2[3]:
            print("Поздравляем, ", name1, ", Вы угадали!")
            break
    if (len(word1)) == 8:
        if word1[0] == word2[7] and word1[1] == word2[6] and word1[2] == word2[5] and word1[3] == word2[4]:
            print("Поздравляем, ", name1, ", Вы угадали!")
            break
    else:
        counter += 1
        print("Извиние, ", name1, ", Вы не угадали.")
        word3 = input("Попробуйте еще раз: ")
else:                                                             # When a user doesn't guess it, cycle ends.
    counter += 1
    print("Извиние, ", name1, ", Вы не угадали.")

