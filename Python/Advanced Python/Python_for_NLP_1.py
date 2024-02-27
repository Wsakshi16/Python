# -*- coding: utf-8 -*-
"""
Created on Tue May 16 08:30:00 2023

@author: aditya
"""
#Tokenization
#word tokenization
txt = 'welcome to the new year 2023'
x=txt.split()
print(x)
######################################################################
'''
Removing Special Character

Special characters, as you know, 
are non-alphanumeric characters. 
These characters are most often found in comments,
 references, currency numbers etc. 
 These characters add no value to text-understanding
 and induce noise into algorithms.
 For that regex package is used


'''
#imports
import re #function to remove special characters
def remove_special_characters(text):
    #define the pattern to keep
    pat = r'[^a-zA-Z0-9.,!?/:;\"\'\s]' #r- used when we used \(backward slash) inside the bracket
    #^-Except
    return re.sub(pat, '', text)

#call function
remove_special_characters("007 Not sure@ %wha(t to$3435 do?//,;")
########################################
#Removing Numbers
'''
As you saw above, the text is retained. 
But sometimes these might not be required. 
Since we are dealing with text, 
so the number might not add much information 
to text processing. So, numbers can be removed 
from text. We can use regular-expressions (regex) 
to get rid of numbers.
 This step can be combined with above one 
 to achieve in single step.
'''
import re #function to remove special characters
def remove_special_characters(text):
    #define the pattern to keep
    pat = r'[^a-zA-Z.,!?/:;\"\'\s]' #r- used when we used \(backward slash) inside the bracket
    return re.sub(pat, '', text)

#call function
remove_special_characters("007 Not sure@ %wha(t to$3435 do?//,;")
#################################################################
txt = 'welcome: to the, new year; 2023!'
import re
x=re.split(r'(?:,|;|\s)\s',txt)
print(x)
####################################################################
#Remove Punctuation
'''
This can be clubbed with step of removing 
special characters. Removing punctuation 
is fairly easy. It can be achieved by using 
string.punctuation and keeping everything 
which is not in this list.

'''
#imports
import string #function to remove punctuation marks
def remove_punctuation(text):
    text=''.join([c for c in text if c not in string.punctuation])
    return text
remove_punctuation("what{ \is| your name}%$^%")
####################################################################
#Stemming
#Stemming is the process of reducing 
#inflected/derived words to their word stem, 
#base or root form
#These mainly rely on chopping-off ‘s’, ‘es’, ‘ed’, 
#‘ing’, ‘ly’ etc from the end of the words 
#and sometimes the conversion is not desirable. 
#But nonetheless, stemming helps us in standardizing text.

#imports
import nltk #function for stemming
def get_stem(text):
    stemmer = nltk.porter.PorterStemmer()
    text= ''.join([stemmer.stem(word) for word in text.split()])
    return text
get_stem("we are eating and swimming ; we have been eating and swimming ; he eats and swims ; he ate and swam ")
##################################################
'''
Though stemming and lemmatization both generate the root form 
of inflected/desired words, but lemmatization is an advanced 
form of stemming. Stemming might not result in actual word, 
whereas lemmatization does conversion properly with the use of vocabulary
'''

line = 'asdf: fgdk; afed, fjek,asdf, foo'
re.split(r'(?:,|;|\s)\s*', line)
#################################################
pattern=r'(?:,|;|\s)\s*'
x=re.split(pattern,txt)
print(x)
#################################################
#matching text at the start or end of string 
filename='spam.txt'
filename.endswith('.txt')
#################################################
area_name='6 th lane west Andheri'
area_name.endswith('west Andheri')
#####################################################
choices=('http:','ftp:')
url='http://www.python.org'
url.startswith(choices)
#####################################################
#Slicing a string
#If S is a string, the expression S [start : stop : step]
#Return the portion of the string from index 
#at a step size.
S = 'ABCDEFGHI'
print(S[2:7]) #CDEFG
#Note that the item at index 7 'H is not included
#Slice with Negative Indices
S = 'ABCDEFGHI'
print(S[-7:-2]) #CDEFG

#Slice with Positive and Negative Indices
S = 'ABCDEFGHI'
print(S[2:-5]) #CD

#Specify the step of slicing
S = 'ABCDEFGHI'
print(S[2:7:2]) #CEG

S = 'ABCDEFGHI'
print(S[9:3:-2])

S = 'ABCDEFGHI'
print(S[:3])

#Slice last three characters from the string
S = 'ABCDEFGHI'
print(S[6:])

#Reverse a String
S = 'ABCDEFGHI'
print(S[::-1])
##########################################
#Similar operations can be done with slices
filename = 'spam.txt'
filename[-4:]=='.txt'
#########################################
url = 'http://www.python.org'
url[:5] == 'http:' or url[:6] == 'https:' or url == 'ftp:'
##################################################################
##################################################################
from fnmatch import fnmatch,fnmatchcase
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')]
#['Dat1.csv', 'Dat2.csv']
###############################################
from fnmatch import fnmatch
names = ['Andheri East','Parle East','Dadar West']
[name for name in names if fnmatch(name, '* East')]
#['Andheri East', 'Parle East']
####################################################

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
    ]

#you could write list comprehensions like this
#############################################################
text = 'yeah, but no, but yeah, but no, but yeah'
 # Exact match
text == 'yeah'
#False
# Match at start or end
text.startswith('yeah')
#True
text.endswith('no')
#False

#Search for the location of the first occurrence
text.find('no') #10
#############################################################
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
#Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')
#yes

if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')
##############################################################
text = '333-444-55555'
import re
if re.match(r'\d\d\d-\d\d\d-\d\d\d\d\d',text):
    print('yes')
else:
    print('no')
##############################################################
text = '333-444-55555'
import re
if re.match(r'\d{3}-\d{3}-\d{5}',text): #\d{n}-checking the number of digits in string
    print('yes')
else:
    print('no')
######################################################################

#Searching and replacing text

text= 'yeah, but no, but yeah, but no, but yeah'
#Replace yeah with yep
text.replace('yeah','yep')
#################################################
text = 'Today is 17/5/2023 and our exam is start from 5/6/2023'
import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2',text)

import re 
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2',text)

newtext,n=datepat.subn(r'\3-\1-\2',text)
newtext
n

#Searching and replacing case sensitive text
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)
re.sub('python','snake', text,flags=re.IGNORECASE) #It is replacing words irrespective of their case sensitivity
##########################################################

#matched text. If you need to fix this, you might have to use a su  following:
import re
import nltk
text= 'UPPER PYTHON, lower python, Mixed Python'
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
re.sub('python',matchcase('snake'), text, flags = re.IGNORECASE)
#########################################################################

str_pat = re.compile(r'\"(.*)\"')  
text1 = 'Computer says "No."'        
str_pat.findall(text1)

#However we have text below
text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2)

str_pat = re.compile(r'\"(.*?)\"')  
str_pat.findall(text2)
#########################################################################
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/*this is a comment*/'
comment.findall(text1) 
        
text2 = '''/*this is a 
                 multiline comment*/
'''
comment.findall(text2)
#To fix the problem, you can add support for newlines.
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2) 
######################################################
#Removing numbers from the text
def remove_numbers(text):
    result = re.sub(r'\d+','', text)
    return result

input_str = "There are 3 balls in this bag, and 12 in the other bag."

remove_numbers(input_str)
#########################################################################
#To convert numbers into words
import inflect 
p = inflect.engine()

#convert number into words
def convert_number(text):
    #split string into list of words
    temp_str = text.split()
    #initialise empty list
    new_string = []
    for word in temp_str:
        #if word is a digit, covert the digit into numbers 
        #and append into the new_string list
        if word.isdigit():
            temp = p.number_to_words(word)
            new_string.append(temp)
        
        #append the word as it is
        else:
            new_string.append(word)
           
    #join the words of new_string to form a string 
    temp_str = ' '.join(new_string)
    return temp_str

input_str = 'There are 3 balls in this bag, and 12 in the other bag'
convert_number(input_str)
############################################################
############################################################
#Excercise 1: Reverse each word of a string 
str = 'My Name is Jessa'
def reverse_words(sentence):
    #Split string on whitespace
    words = sentence.split(" ")

    new_word_list = [word[::-1] for word in words]
    
    res_str = " ".join(new_word_list)
    return res_str
reverse_words(str)
#############################################################
#Exercise 2: Read text file into a variable and replace all newline

with open('c:/1-Python/sample.txt') as file_object:
    content=file_object.read()
print(content)
x = content.replace('\n',' ')
print(x)
#############################################################
#############################################################

#Normalizing Unicode text to representation
#You're working with unicode String, but need to make sure
#that all of the strings have
#the same underlying representaton.
s1 = 'Spacy Jalape\u00f1o'
s2 = 'Spacy Jalapen\u0303o'
print(s1)
print(s2)
s1==s2
#False

import unicodedata
t1 = unicodedata.normalize('NFC', s1) #Normalizing form of canonical composition
t1
t2 = unicodedata.normalize('NFC', s2)
t2
t1==t2
#True

#Normalization using NFD
print(ascii(t1))
t3 = unicodedata.normalize('NFD', s1) #Normalizing form of canonical composition
t3
t4 = unicodedata.normalize('NFD', s2)
t4
t3 == t4
#True
print(ascii(t3))

t1 = unicodedata.normalize('NFD', s1)
''.join(c for c in t1 if not unicodedata.combining(c))
#Spacy Jalapeno
#####################################################################
import re
num = re.compile('\d+')
#Ascii digits
num.match('123')
#<re.Match object; span=(0, 3), match='123'>

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
pat.match(s)
#<re.Match object; span=(0, 6), match='straße'>
###########################################################################
#stripping unwanted characters from the string
s = '    hello world \n'
s.strip()
#'hello world'
s.lstrip()
#'hello world \n'
s.rstrip()
#'    hello world'

    #Character stripping
t = '--------******hello======='
t.lstrip('-')
#'******hello======='
t.strip('-=*')
#hello

s = '   Hello World  \n'
s.strip()
s
#Hello World

s = '   Hello    World   \n'
a=s.replace(' ','')
a.replace('\n','')
#helloWorld

import re
re.sub('\s+',' ', s)
##############################################

s = 'pýtĥöñ\fis\tawesome\r\n'
s
#'pýtĥöñ\x0cis\tawesome\r\n'

#The first step is to clean up the whitespace. To do this, make a small tra and use translate():
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None #Deleted
    }
a = s.translate(remap)
a
a.replace('\n','')
####################################################################
#As you can see here, whitespace characters 

import unicodedata
import sys
a = 'pýtĥöñ is awesome'
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD',a)
b
#'pýtĥöñ is awesome'
b.translate(cmb_chrs)
#'python is awesome'

#Yet another technique for cleaning up text
#involves I/O decoding and encoding functions.
#The idea here is to first do some priliminary
#cleaup of the text, and then run it
#through a combination of encode() or decode() operations
#to strip or alter it.
a = 'pýtĥöñ is awesome\n'
b = unicodedata.normalize('NFD',a)
b.encode('ascii', 'ignore').decode('ascii')
#'python is awesome\n'
#################################################################
#Aligning the text string
text =            'Hello World'
text.ljust(20)
#'Hello World         '
text.rjust(20)
#'         Hello World'
text.center(20)
#'    Hello World     '
########################################################################
#All of these methods accept an optional characters & fill character as well
text.rjust(20,'=')
#'=========Hello World'
text.ljust(20,'*')
#'Hello World*********'
text.center(20,'%')
# '%%%%Hello World%%%%%'
######################################################################
format(text, '>20') #Also using format method we can shift the string by using symbol 
                    #'>'-shift towards right hand side
#'         Hello World'
format(text, '<20') #'<'-shift towards left hand side
#'Hello World         '
format(text, '^20') #'^'-shift at the center alignment
#'    Hello World     '
#################################################
#Here you can add characters to fill the apace at the left, right or center
#as above but if you want to include a fill characters other than a space,
#character:
format(text, '=>20s')
#'=========Hello World'

format(text, '=<20s')
#'Hello World========='

format(text, '*^20s')
#'****Hello World*****'

#These format codes are also be used in the format() method when formatting
#values. for example:

'{:>10s} {:>10s}'.format('Hello','World')
#'     Hello      World'

#one benefit

x = 1.2345
format(x, '>10')
x
#'    1.2345'
format(x, '^10.2f')
#'   1.23   '
########################################################
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)
#'Is Chicago Not Chicago?'
','.join(parts)
#'Is,Chicago,Not,Chicago?'
''.join(parts)
#'IsChicagoNotChicago?'
########################################################
#If you join very few strings then you can use + operator
a = 'Is Chicago'
b = 'Not Chicago?'
a + ' ' + b
#'Is Chicago Not Chicago?'
####################################
print('{} {}'.format(a,b))
#Is Chicago Not Chicago?
print(a + ' ' + b)
#Is Chicago Not Chicago?
####################################################
a = 'Hello' 'World'
a
#############################################
a = 'Hello' ' ' 'World' #Contamination
a
###########################################
#Interpolating variables in strings
#You want to create a string in which embedded variable names are sub
#string representation of a variable's value.
s = '{name} has {n} messages.'
s.format(name='Guido',n=39)
##############################################
s = '{name} has {n} messages.'
name = 'Guido'
n = 89
s.format_map(vars())
#'Guido has 89 messages.'
##############################################
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    not around the eyes, don't look around the eyes, don't look around the ayes, \
        look into my eyes, you're under."
#Here's how you can use the textwrap madule to reformat it in various 
import textwrap
print(textwrap.fill(s, 10))
#############################################################
 
print(textwrap.fill(s, 40, initial_indent=' '))
################################################
 
print(textwrap.fill(s, 40, subsequent_indent=' '))
################################################################
################################################################
#The sentence tokenization, seperating sentences from document
import nltk
nltk.download('punkt')

sentence_data = "This is Data Science Class. We have to come earlier for that."
nltk_tokens = nltk.sent_tokenize(sentence_data)
print(nltk_tokens)
####################################################################
#Non-English Tokenization
import nltk
german_tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens = german_tokenizer.tokenize('Wir geht es ihenen? Gut, danke.')
print(german_tokens)
#####################################################################
#word tokenization
import nltk

word_data = "It originated from the idea that there are readers who prefer "
nltk_tokens = nltk.word_tokenize(word_data)
print(nltk_tokens)
#############################################
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stopwords.words('english')
#The various language other than English which has these stopwords are as 

from nltk.corpus import stopwords
print(stopwords.fileids())
######################################################################
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))

all_words  = ['There', 'is', 'a', 'three', 'near', 'the', 'river']
for word in all_words:
    if word not in en_stops:
        print(word)
####################################################################
import nltk
nltk.download('omw-1.4')
from nltk.corpus import wordnet
nltk.download('wordnet')

synonyms = []

for syn in wordnet.synsets("soil"):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print(set(synonyms))
###################################################################
nltk.download('omw-1.4')
from nltk.corpus import wordnet
antonyms = []
 
for syn in wordnet.synsets("ahead"):
    for lm in syn.lemmas():
        if lm.antonyms():
            antonyms.append(lm.antonyms()[0].name())
print(set(antonyms))
#############################################################



text ="one 🐘 and three 🐋"
print(text)
print(len(text))

'''
We encode the string into a byte type using the 
utf8 encoding and print the bytes.
We count the number of bytes in this encoding type.
'''

e= text.encode('utf8')
print(e)
print(len(e))

e= text.encode('utf16')
print(e)
print(len(e))
#################################################

fname='data.txt'
with open(fname, mode='rb') as f:
    #by default it encode in utf-8
    contents = f.read()
    
    print(type(contents))
    print(contents)
    print(contents.decode('utf8'))
    print(contents.decode('utf16'))
    
#######################################################
#NFC and NFD

#there is no difference bet NFC And NFD

































