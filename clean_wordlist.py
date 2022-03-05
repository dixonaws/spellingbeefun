import re

file_wordlist=open('wordlist.txt', 'r')
lst_words=file_wordlist.read().splitlines()
file_wordlist.close()

# remove trailing spaces
lst_tmp_clean_words=[]
for word in lst_words:
    word=word.rstrip()
    lst_tmp_clean_words.append(word)

lst_words=lst_tmp_clean_words

int_lst_words_length=len(lst_words)
print("lst_words has " + str(int_lst_words_length))

lst_removed_dups=[]
for word in lst_words:
    # print("Evaluating " + word + "... ", end="")

    try:
        spaces=word.index(" ")
        if(spaces)>0:
            print("Removing " + word + " because of space.")
            lst_words.remove(word)
            continue    # go to the next iteration
    except ValueError:
        pass;

    # get rid of junk with dashes, quotes, commas
    junk = re.findall("[-'`,#]", word)

    if junk:
        lst_words.remove(word)
        print("Removing " + word + " because of junk character(s).")
        continue    # go to the next iteration
    else:
        # print("ok.")
        pass

    # add the word to a new list if it is greater than 4 letters
    if len(word) >= 4:
        if word not in lst_removed_dups:
            lst_removed_dups.append(word)

    if("/" in word):
        lst_words.remove(word)
        print("Removing " + word + " because of junk character(s).")
        continue  # go to the next iteration

print("Clean word list has " + str(len(lst_removed_dups)) + " words.")

str_results_filename="clean_wordlist.txt"
print("Writing results to " + str_results_filename + "... ", end="")
file_new_clean_wordlist=open(str_results_filename, "w")
for word in lst_removed_dups:
    file_new_clean_wordlist.write(word)
    file_new_clean_wordlist.write("\n")

print("done.")

file_new_clean_wordlist.close()



