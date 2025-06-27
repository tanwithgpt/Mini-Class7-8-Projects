d = {'Mature':'fully grown or fully developed','Obliged':'to do what somebody asks; to be helpful',
     'Ruby':'ruby is a lustrous, deep red stone'}
a = input('Enter the word which you want to know the meaning of:').capitalize()
if a in d:
    print('The meaning of',a,'is', d[a])
elif a not in d:
    own_word = input('This word is not in the dictionary, want to enter your meaning and develop this, enter:')
    d[a] = own_word
    print('Your word has been added to the dictionary!',d[a])
