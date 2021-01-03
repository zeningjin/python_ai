import os
from collections import Counter
# 1. 准备一个词库（莎士比亚全集）
chars = 'abcdefghijklmnopqrstuvwxyz'
def get_dict(dir_path):
    words = []
    for f in os.listdir(dir_path):
        with open(os.path.join(dir_path,f)) as r:
            for word in  r.read().strip().lower().split():
                for c in word:
                    if not c.isalpha():
                        word = word.replace(c,'')
                if len(word)>1:
                    words.append(word)
    return dict(Counter(words).most_common())

# 2. 用户输入单词，判断单词是否在莎士比亚全集里面，如果存在输出，如果不存在呢？
def get_right_word(word,words):
    if word in words.keys():
        return word
    # 3. 根据输入的单词，生成所有的编辑距离为1的单词
    wrong_words = edit2(word)
    # 	ave：[have,five,fave.....]
    # 4. 遍历所有单词，看哪个单词在词库里面出现，并且取出在词库中出现最多的那个。
    count = 0
    right_word = ''
    for w in wrong_words:
        if w in words.keys():
            if words[w]>count:
                right_word = w
                count = words[w]
    return right_word


# def edit(word):
#     words = []
#     # 1.少一个字母
#     for c in chars:
#         for i in range(len(word)+1):
#             words.append(word[:i]+c+word[i:])
#     # 2.多一个字母
#     for i in range(len(word)):
#         words.append(word[:i]+word[i+1:])
#     # 3.相邻的字母颠倒
#     for i in range(len(word)-1):
#         words.append(word[:i]+word[i+1]+word[i]+word[i+2:])
#     # 4.错一个字母
#     for c in chars:
#         for i in range(len(word)):
#             words.append(word[:i]+c+word[i+1:])
#     return words

def edit2(word):
    return [word[:i]+c+word[i:] for c in chars for i in range(len(word)+1)]+[word[:i]+word[i+1:] for i in range(len(word))]+[word[:i]+word[i+1]+word[i]+word[i+2:] for i in range(len(word)-1)]+[word[:i]+c+word[i+1:] for c in chars for i in range(len(word))]


if __name__ == '__main__':
    dir_path = 'E:\AI精英2001\代码\day5\WILLIAM SHAKESPEARE'
    words = get_dict(dir_path)
    word = input('请输入一个错误单词：')
    result = get_right_word(word,words)
    print(result)