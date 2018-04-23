'''
    Tách từ
'''
# -*- coding: utf-8 -*-
import underthesea as uts
from pymongo import MongoClient

class DataExport:
    """
    Tách từ tiếng việt từ Data đã có va luu vao database moi
    """
    def __init__(self, q, a, d):
        self.question = q
        self.answer = a
        self.date = d

    def get_data(self):
        """
        lấy data đã được làm sạch từ csdl lên
        :return:
        """
        client = MongoClient()
        db = client.DBTuyenSinh
        col = db.AnswerQuestion
        select_table = col.find({}, {"_id": 0, "questions": 1, "answers": 1, "dates": 1})
        for i in select_table:
            self.question.append(i['questions'])
            self.answer.append(i['answers'])
            self.date.append(i['dates'])

        return self

    def segmentation(self):
        """
        tách từ từ cơ sở dữ liệu đã được đưa lên
        :return:
        """
        for i in range(len(self.question)):
            result_question = uts.word_sent(self.question[i], format='text')
            print("*********Segmentation Question*************")
            print(result_question)
            self.question[i] = result_question
        for j in range(len(self.question)):
            result_answer = uts.word_sent(self.answer[j], format='text')
            print("*********Segmentation Answer*************")
            print(result_answer)
            self.answer[j] = result_answer
        for k in range(len(self.question)):
            result_date = uts.word_sent(self.date[k], format='text')
            print("*********Segmentation Date*************")
            print(result_date)
            self.date[k] = result_date
        return self

    def import_data(self):
        """
        lưu dữ liệu  tách từ vào một csdl mới
        :return:
        """
        client = MongoClient('mongodb://localhost:27017/')  # kết nối DB
        db = client.DBTuyenSinh  # tao ket noi tới DB
        collection = db.WordSegmentation
        print('bat dau luu du lieu vao database')
        for question, answer, date in zip(self.question, self.answer, self.date):
            document = collection.insert([{"questions": question, "answers": answer, "dates": date}])
        client.close()


if __name__ == '__main__':
    list_question = []
    list_answer = []
    list_date = []
    word_data = DataExport(list_question, list_answer, list_date)
    a = word_data.get_data()
    for i in a.question:
        print(i)
    for j in a.answer:
        print(j)
    for k in a.date:
        print(k)
    b = word_data.segmentation()
    print('**********************************************************************************')
    for l in b.question:
        print(l)
    for m in b.answer:
        print(m)
    for n in b.date:
        print(n)
    word_data.import_data()
    print('Da luu du lieu vao database')






