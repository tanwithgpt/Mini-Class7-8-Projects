d = {'Mature':'fully grown or fully developed','Obliged':'having no problems with doing a task',
     'Ruby':'this is a noun(or a name)'}
a = input('Enter the word which you want to know the meaning of:').capitalize()
if a in d:
    print('The meaning of',a,'is', d[a])
elif a not in d:
    own_word = input('This word is not in the dictionary, want to enter your meaning and develop this, do it here')
    d[a] = own_word
    print('Your word has been added to the dict.!',d[a])