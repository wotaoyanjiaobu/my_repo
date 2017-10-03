#!/usr/bin/python
# coding:utf-8


from __future__ import unicode_literals
import pyltp


class LTPSegmentor(object):
    def __init__(self):
        self.segmentor = pyltp.Segmentor()
        cws_model_path = '/home/skywalker/PycharmProjects/crf_crm/ltp_model/cws.model'
        my_dict_path = '/home/skywalker/PycharmProjects/crf_crm/ltp_model/my_dict.txt'
        self.segmentor.load_with_lexicon(cws_model_path.encode('utf-8'), my_dict_path.encode('utf-8'))

    def segment(self, text):
        if isinstance(text, unicode):
            text = text.encode('utf-8')
            words = self.segmentor.segment(text)
            return [w.decode('utf-8') for w in words]
        else:
            return self.segmentor.segment(text)


ltp_segmentor = LTPSegmentor()


if __name__ == '__main__':
    ltp_segmentor_new = LTPSegmentor()
    result = ltp_segmentor_new.segment('嗯妈妈您好，我是掌门一对一这边的教务老师，我看到您是帮孩子预约了一个三年级的数学课是吗？')
    print(' '.join(result))
