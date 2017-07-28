def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum  # sum puts something back into value


#function that applies discount to total and returns total
def dis(list, discount):
    total = sum_list(numbers)
    total = total - total * discount
    return total

print dis([5,8], .2)


#total = sum_list([1,2,3])
#total = total + total * .15
#print total




#function that takes one word and make it pig latin
#more words
#input from user

name = raw_input("Type a word: ")

def pig_word(word):

    new_word = word[1:]
    new_word = new_word + word[0] + 'ay'
    print 'New word is:' + new_word

    #if a phrase call function

pig_word(name) # call the function out of the function

#word.split('')

#phrase or sentences
def pig_phrase(phrase):

    new_phrase
    return

#movies in terminal
