'''
    Rút trích dữ liệu từ trang tuyển sinh câu hỏi thường gặp đại học Hoa Sen
    http://tuyensinh.hoasen.edu.vn/cau-hoi-thuong-gap-950.html
'''
# -*- coding: utf-8 -*-
from selenium import webdriver
from pymongo import MongoClient
import standardized_data as sd
import time
class SelTSHS:
    def __init__(self, driver):
        self.driver = driver
    def crawl_tuyen_sinh_hs(self):
        list_questions = []
        list_answers = []
        list_dates = []
        index_page = 0
        while index_page <= 8:
            driver.get("http://tuyensinh.hoasen.edu.vn/cau-hoi-thuong-gap-950.html?page=" + str(index_page))
            print(driver.title)
            question_list = driver.find_elements_by_xpath('//*[@id="block-views-list-with-title-faq"]/div/div/div[1]/ul/li')
            q = []
            for i in question_list:
                q.append(i.text)
            for j in q:
                question_link = driver.find_element_by_link_text(str(j))
                question_link.location_once_scrolled_into_view
                time.sleep(3)
                question_link.click()
                time.sleep(2)
                question = driver.find_element_by_class_name("question")
                answer = driver.find_element_by_class_name("field-items")
                date = "Ngày đang cập nhật"
                print("***************Câu hỏi*********")
                list_questions.append("Đại học Hoa Sen - " + question.text)
                print(question.text)
                print("***************Trả lời*********")
                list_answers.append(answer.text)
                print(answer.text)
                list_dates.append(date)
                driver.back()
            index_page += 1
        client = MongoClient('mongodb://localhost:27017/')  # kết nối MongoDB
        db = client.DBTuyenSinh  # tao ket noi tới DB
        collection = db.AnswerQuestion
        for question, answer, date in zip(list_questions, list_answers, list_dates):
            print("********Câu hỏi:******\n\t" + question)
            question = sd.format_word(question)
            print("********Tiền xử lý câu hỏi :******\n\t" + question)
            print("********Trả lời:******\n\t" + answer)
            answer = sd.format_word(answer)
            print("********Tiền xử lý trả lời:******\n\t" + answer)
            print(date)
            document = collection.insert([{"questions": question, "answers": answer, "dates": date}])


if __name__ == '__main__':
    chrome_path = r"D:\chromedriver_win32\chromedriver.exe"
    chrome_opptions = webdriver.ChromeOptions()
    chrome_opptions.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_path, chrome_options=chrome_opptions)
    tuyen_sinh = SelTSHS(driver)
    tuyen_sinh.crawl_tuyen_sinh_hs()
    driver.quit()

