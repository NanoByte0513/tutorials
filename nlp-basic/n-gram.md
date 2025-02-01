# What is  N-gram
Split the sentence into several sub-seq with length N, the probability of each word is only affected by its previous N-1 words.
+ Unigram(N=1): I wish you a good day -> (I) (wish) (you) (a) (good) (day)
+ Bigram(N=2): I wish you a good day -> (I wish) (wish you) (you a) (a good) (good day)
+ Trigram(N=3): I wish you a good day -> (I wish you) (wish you a) (you a good) (a good day)  
The prob of the N-th word: $P(W_i|W_{i-1}, W_{i-2}, ..., W_{i-n+1})$

# What is Gram
A gram can be a word or a character, also known as **token**.

# Tokenizer
Split a sentence into a sequence of tokens. NLTK, SpaCy for Eng, Jieba for Cn.