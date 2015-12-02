import sys
import argparse

#rack_dict contains letters and number of each letter in rack
def get_rack_dict(rack_list):
    rack_dict = {}
    for letter in rack_list:
        rack_dict[letter] = rack_dict.get(letter, 0) + 1
        
    return rack_dict

#creates all word combinations from rack and returns the ones found in the Scrabble word list
#Reference: https://www.youtube.com/watch?v=R4AoNz8BzTQ
def get_valid_words(rack_list, word_list):
    rack = get_rack_dict(rack_list)
    vw, valid_words, i = "", [""], 0
    while len(vw) < len(rack_list):
        vw = valid_words[i]
        tempVW = []
        for w in xrange(len(vw)):
            tempVW.append(vw[w])
            
        temp_rack_dict = dict(rack)
        j = 0
        while j < len(rack_list):
            if rack_list[j] not in tempVW:
                new_word = vw + rack_list[j]
                valid_words.append(new_word)   
                j +=  temp_rack_dict[rack_list[j]]
            else:
                tempVW.remove(rack_list[j])
                num = temp_rack_dict[rack_list[j]] - 1
                temp_rack_dict[rack_list[j]] = num
                j += 1
        i += 1

    final_vw = set(valid_words).intersection(set(word_list))#all valid words in Srabble dictionary
        
    return list(final_vw)


#returns the scores of each possible word 
def get_scores(valid_words):
    #how much each letter is worth
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

    l = []
    for i in valid_words:
        scr = [scores[x] for x in list(i)]#score for each word
        l.append((sum(scr), i))#tuple contains score and word

    l.sort(reverse=True)

    
    #a fast way to print all scores and words at once
    print '\n'.join("%d %s" % (x[0], x[1]) for x in l)


def main():
    #prompts the user to enter rack of letters if missing
    if len (sys.argv) != 2 :
        print "Please supply the rack of letters."
        sys.exit(0)
    
    mynewhandle = open("sowpods.txt", "r")

    wordList = mynewhandle.readlines()   # Try to read next line

    wordList = [x.lower().strip() for x in wordList]#Scrabble dictionary word list
    
    # argument parsing for rack of letters
    parser = argparse.ArgumentParser()
    parser.add_argument("RACK", help="the rack of letters")
    args = parser.parse_args()
    rack = list(args.RACK.lower())
    
    vw = get_valid_words(rack, wordList)#valid words from Scrabble dictionary

    get_scores(vw)
    mynewhandle.close()

if __name__ == "__main__": main()
