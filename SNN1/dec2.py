from math import log10

class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        for line in file(ngramfile):
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.itervalues())
        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in xrange(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score
       
0

from pycipher import Vigenere
import re
from itertools import permutations

qgram = ngram_score('quad.txt')
trigram = ngram_score('tr.txt')
ctext = 'BUWCMKJILBMFMCWSNMQOJKXLBHWMUVAJKWZPICMMHPCSVLTLQZUCJXCHKZHJMVSASNQLNWKJLRASFXUFRBXGVGMSLLEYEBNPGPWMHXQAIIIFGOJQSQGUTZBRQPFZLIEBEWEMOLKCJGQGDMKAQNQOFHDOJQGCAFHCEQWHZKTRQBSGSWYYCTMFMMNAEITGRVGRMYJUJEOCJWGCWSYVWJKLJBXVIZUZWWHLFUMFMYFGLGGHKCKWWSYVWVQFVBAYBPWMHXCHRTRQQFMOKLCXZVIMTVYWUENUELFGTVYOJCCZWIBPAVSHZMUMVKMGWABSEIPNZWGYNRBCLLGLYQLRWENQSPJCXPEGOUYGXVQGKPXNIFYQWRVOIGYMZZTFWSPNYMAGAGTFQSHWIGIRWTWOHLANYMUCAGXCMVEYZADYPAXTSWECEIMGVTGCGO'
ctext = re.sub(r'[^A-Z]','',ctext.upper())

# keep a list of the N best things we have seen, discard anything else
class nbest(object):
    def __init__(self,N=1000):
        self.store = []
        self.N = N
        
    def add(self,item):
        self.store.append(item)
        self.store.sort(reverse=True)
        self.store = self.store[:self.N]
    
    def __getitem__(self,k):
        return self.store[k]

    def __len__(self):
        return len(self.store)

#init
N=100
for KLEN in range(2,20):
    rec = nbest(N)

    for i in permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ',3):
        key = ''.join(i) + 'A'*(KLEN-len(i))
        pt = Vigenere(key).decipher(ctext)
        score = 0
        for j in range(0,len(ctext),KLEN):
            score += trigram.score(pt[j:j+3])
        rec.add((score,''.join(i),pt[:30]))

    next_rec = nbest(N)
    for i in range(0,KLEN-3):
        for k in xrange(N):
            for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                key = rec[k][1] + c
                fullkey = key + 'A'*(KLEN-len(key))
                pt = Vigenere(fullkey).decipher(ctext)
                score = 0
                for j in range(0,len(ctext),KLEN):
                    score += qgram.score(pt[j:j+len(key)])
                next_rec.add((score,key,pt[:30]))
        rec = next_rec
        next_rec = nbest(N)
    bestkey = rec[0][1]
    pt = Vigenere(bestkey).decipher(ctext)
    bestscore = qgram.score(pt)
    for i in range(N):
        pt = Vigenere(rec[i][1]).decipher(ctext)
        score = qgram.score(pt)
        if score > bestscore:
            bestkey = rec[i][1]
            bestscore = score       
    print bestscore,'Vigenere, klen',KLEN,':"'+bestkey+'",',Vigenere(bestkey).decipher(ctext)
    

0
