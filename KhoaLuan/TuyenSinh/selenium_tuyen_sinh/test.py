# -*- coding: utf-8 -*-
from underthesea import word_sent

sentence = u"Trường đại học Mở thành phố Hồ Chí Minh thông báo tuyển sinh năm 2018."
word_sent_sentence = word_sent(sentence)
print("Word Segmentation\n", word_sent_sentence)
word_sent_sentence_text = word_sent(sentence, format="text")
print("Word Segmentation format text\n", word_sent_sentence_text)
#Kết quả
# Word Segmentation
#  ['Trường', 'đại học', 'Mở', 'thành phố', 'Hồ', 'Chí', 'Minh', 'thông báo',
#   'tuyển sinh', 'năm', '2018', '.']
# Word Segmentation format text
#  Trường đại_học Mở thành_phố Hồ Chí Minh thông_báo tuyển_sinh năm 2018 .
#
# chunk_sentence = chunk(sentence)
# print("Chunking\n", chunk_sentence)
#
#classify_sentence = classify(sentence)
#print("Text Classification\n", classify_sentence)
#

#ner_sentence = ner(sentence)
#print("Named Entity Recognition\n", ner_sentence)

#



# tag_sentence = pos_tag(sentence)
# print("POS tagging\n", tag_sentence)




