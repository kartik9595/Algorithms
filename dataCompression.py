#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:47:32 2017
PROGRAM FOR DATA COMPRESSION EXCERCISE 6
@author: k.venkatraman
"""


import math
from enhancedOccurrenceFrequencies import *
from huffman import *

characters = ""        
for i in range(128) : 
    characters += chr(i)
  
# Calculating the values of entropy for different languages    
    
myText=readText('data/wutheringHeights.txt')
englishOF=compfreq(counter(characters,myText))
English=list(englishOF.values())
entropy_en=0
for val in English:
    if val!=0:
        entropy_en+=-val*math.log2(val)

print("The entropy of English language in the text is found to be :"+str(entropy_en))    



myText=readText('data/MadameBovary.txt')
frenchOF=compfreq(counter(characters,myText))
French=list(frenchOF.values())
entropy_fr=0
for val in French:
    if val!=0:
        entropy_fr+=-val*math.log2(val)

print("The entropy of French language in the text is found to be :"+str(entropy_fr))    

myText=readText('data/donQuijote.txt')
spanishOF=compfreq(counter(characters,myText))
Spanish=list(spanishOF.values())
entropy_sp=0
for val in Spanish:
    if val!=0:
        entropy_sp+=-val*math.log2(val)

print("The entropy of Spanish language in the text is found to be :"+str(entropy_sp)) 

myText=readText('data/kritikDerReinenVernunft.txt')
Ch1=len(myText)
germanOF=compfreq(counter(characters,myText))
German=list(germanOF.values())
entropy_ge=0
for val in German:
    if val!=0:
        entropy_ge+=-val*math.log2(val)

print("The entropy of German language in the text is found to be :"+str(entropy_ge)) 

# Huffman algorithm used for compression and decompression
# Obtaining the compressed bits by calling on the function for Huffman compression

compTxt=""
list_gen=build_huffman_tree(germanOF)
dicts=generate_code(list_gen, prefix="")
compTxt=compress(myText,dicts)
Ch2=len(compTxt)
print("\n")
print("THE COMPRESSED BITS :")
print(compTxt)

decode_dicts=build_decoding_dict(dicts)

decodeTxt=decompress(compTxt,decode_dicts)
print(decodeTxt)

# Calculating the compression ratio of the German language

ratio=Ch2/Ch1
print("THE ENTROPY OF GERMAN LANGUAGE IS :"+str(entropy_ge))
print("COMPRESSION IS :"+str(ratio))
cmpratio=7*Ch1/Ch2*100
print("THE COMPRESSION RATE IS :"+str(cmpratio)+"%")
