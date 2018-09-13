"""
#coding: utf-8
PROGRAM FOR CALCULATING THE PROBABILITY DISTRIBUTION AND LANGUAGE DETECTION  EXERCISE 5
KARTIK VENKATRAMAN  K.VENKATRAMAN 
In[12]:
"""
import math
from math import log,fabs

# Defining the functions required 

def readText(filename):
   infile = open(filename,'r')
   myText=infile.read()
   myText=myText.lower()
   return myText
   
# Function to remove punctuation
def remove_punc(text):
    punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`0123456789\n '
    for marker in punctuation:
        text = text.replace(marker, "")
    return text

def counter(word,list_to_search):                 
    counts = {}    
    for ch in word:
        counts[ch]=0
    for word in list_to_search:              
        if word in counts:                   
            counts[word] = counts[word] + 1  
        else:                                
            counts[word] = 1                 
    return counts   

def freqcounter(s,text):
    words = text.split()
    item_to_count=s
    number_of_hits = 0
    for word in words:
      if word == item_to_count:
        number_of_hits += 1
    return number_of_hits

def compfreq(dict):
    su=sum(dict.values())
    for key, value in dict.items():
        dict[key] = dict[key]/su
    return dict    

# Computing the distribution frequencies for different languages

myText=remove_punc(readText('data/wutheringHeights.txt'))
englishOF=compfreq(counter("abcdefghijklmnopqrstuvwxyz",myText))
print(sum(englishOF.values()))
print(englishOF)

myText=remove_punc(readText('data/MadameBovary.txt'))
frenchOF=compfreq(counter("abcdefghijklmnopqrstuvwxyz",myText))
print(sum(frenchOF.values()))
print(frenchOF)

myText=remove_punc(readText('data/donQuijote.txt'))
spanishOF=compfreq(counter("abcdefghijklmnopqrstuvwxyz",myText))
print(sum(spanishOF.values()))
print(spanishOF)

myText=remove_punc(readText('data/kritikDerReinenVernunft.txt'))
germanOF=compfreq(counter("abcdefghijklmnopqrstuvwxyz",myText))
print(sum(germanOF.values()))
print(germanOF)

 # Converting the dictionary values of probability distribution to the list to calculate divergence
English=list(englishOF.values())
French=list(frenchOF.values())
Spanish=list(spanishOF.values())
German=list(germanOF.values())

# Function to compute the K-L divergence 
def kl(p, q):
    s=0
    for dist in range(0,len(p)):
        if q[dist]!=0 and p[dist]!=0:
            s+=p[dist]*math.log2(p[dist]/q[dist])
    return s

# calculating absolute average of divergences between different languages
kl_divergence_en_fr=(abs(kl(English,French)+kl(French,English)))/2
kl_divergence_en_ge=(abs(kl(English,German)+kl(German,English)))/2
kl_divergence_fr_ge=(abs(kl(French,German)+kl(German,French)))/2
kl_divergence_en_sp=(abs(kl(English,Spanish)+kl(Spanish,English)))/2
kl_divergence_fr_sp=(abs(kl(French,Spanish)+kl(Spanish,French)))/2
kl_divergence_ge_sp=(abs(kl(German,Spanish)+kl(Spanish,German)))/2
                    
print("\n")
print("The divergence between English and French is "+ str(kl_divergence_en_fr))
print("The divergence between English and German is "+ str(kl_divergence_en_ge))
print("The divergence between French and German is "+ str(kl_divergence_fr_ge))
print("The divergence between English and Spanish is "+ str(kl_divergence_en_sp))
print("The divergence between French and Spanish is "+ str(kl_divergence_fr_sp))
print("The divergence between German and Spanish is "+ str(kl_divergence_ge_sp))

# Function to detect the language of the text
def langdetector(filename):
    myText=remove_punc(readText(filename))
    langOF=compfreq(counter("abcdefghijklmnopqrstuvwxyz",myText))
    lang=list(langOF.values())
    kl_divergence_en_lang=(abs(kl(English,lang)+kl(lang,English)))/2
    kl_divergence_fr_lang=(abs(kl(French,lang)+kl(lang,French)))/2
    kl_divergence_sp_lang=(abs(kl(lang,Spanish)+kl(Spanish,lang)))/2 
    kl_divergence_ge_lang=(abs(kl(German,lang)+kl(lang,German)))/2
    Language=min(kl_divergence_en_lang,kl_divergence_fr_lang,kl_divergence_sp_lang,kl_divergence_ge_lang)
    if Language==kl_divergence_en_lang:
        print("The language of the text is found to be closed to :"+"English")
    elif Language==kl_divergence_fr_lang:
        print("The language of the text is found to be closed to :"+"French")
    elif Language==kl_divergence_ge_lang:
        print("The language of the text is found to be closed to :"+"German")
    elif Language==kl_divergence_sp_lang:
        print("The language of the text is found to be closed to :"+"Spanish")
        
print("\n")        
langdetector('data/kritikDerReinenVernunft.txt')

