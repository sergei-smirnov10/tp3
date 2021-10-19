from rss import words
import random


class App:
    def word_now(self):
        rand_number = random.randint(0, 18)
        word = words.list_words(rand_number)
        return word

    def app_cod(self):
        word_ = self.word_now()
        list_chap = []
        res = 0
        res_ = len(word_)
        for i in word_:
            list_chap.append(i)
        while True:
            chap = input()
            if chap not in list_chap:
                print('Такой буквы нет!')
            if chap in list_chap:
                print('Такая буква есть!')
                res += 1
                list_chap.remove(chap)
            if res == res_:
                return "Победа!"