# coding=utf-8

s = 'I am a programmer'


def reverse_words(s):
    word_list = s.strip('\r\n'). split(' ')
    return ' '.join(word_list[::-1])

if __name__ == '__main__':
    print reverse_words(s)
