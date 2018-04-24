'''
    Tính độ tương đồng dựa vào câu hỏi
'''
# -*- coding: utf-8 -*-
import math
import re
import numpy
import search_index


def format_data(results):
    """
    :param results: list các tài liệu được tìm thấy
    :return: list các từ không trùng
    """
    kq_for_tfi = []
    data_out = []
    kq = []  # mảng lưu các từ đã tách của tất cả các tài liệu
    for item_result in results:
        i_of_item_result = search_index.word_separation(item_result)
        i_of_item_result = search_index.clearn_stop_word(i_of_item_result)
        data_out.append(i_of_item_result)
        i_of_item_result = re.findall('\w+', i_of_item_result)
        print(i_of_item_result)
        kq += i_of_item_result
        kq_for_tfi.append(i_of_item_result)
    print(kq)
    kq_set = set(kq)  # mảng lưu từ sau khi loại bỏ từ trùng
    return (kq_set, data_out, kq_for_tfi)
# tfi
def calculated_tfi(kq_set, kq_for_tfi):
    tfi = []
    for word in kq_set:
        tfi.append(word)
        kq_index = []
        for k in kq_for_tfi:
            sl = k.count(word)
            kq_index.append(sl)
        tfi.append(kq_index)
    # cấu trúc tfi bao gồm [từ,[số lượng từ trong tài liệu kể cả câu truy vấn]]'
    return tfi
# dfi
def calculated_dfi(tfi):
    dfi = []
    for word_count in range(0, len(tfi)):
        if (word_count % 2 != 0):
            sum = 0
            for counts in range(1, len(tfi[word_count])):
                if tfi[word_count][counts] > 0:
                    sum += 1
            dfi.append(sum)
    print('dfi: số lượng từ xuất hiện trong tài liệu')
    return dfi
# idfi
def calculated_idfi(dfi, data_out):
    # idfi  = log(n/dfi)
    idfi = []
    for item_dfi in range(0, len(dfi)):
        kq = ((len(data_out) - 1) * 1.0) / dfi[item_dfi]
        kq1 = math.log10(kq)
        idfi.append(round(kq1,4))
    return idfi
# wi
def calculated_wi(idfi, tfi):
    # wi = tfi x idfi
    wi = []
    tmp = []
    tmp_wi = []
    for item_tfi in range(1, len(tfi), 2):
        tmp.append(tfi[item_tfi])
    tmp_wi = numpy.array(tmp)
    for item_idfi in range(len(idfi)):
        wi_kq = tmp_wi[item_idfi] * idfi[item_idfi]
        wi.append(wi_kq)
    wi = numpy.array(wi)

    items_wi = []  # chứa các mảng có các giá trị của wi theo cột(từng tài liệu)
    shape_wi = wi.shape
    x_shape_wi = shape_wi[0]  # 10
    y_shape_wi = shape_wi[1]  # 4
    for j_wi in range(y_shape_wi):
        item_wi = []  # chứa giá trị của tung tài liệu
        for i_wi in range(x_shape_wi):
            tmp_kq = wi[i_wi][j_wi]
            item_wi.append(tmp_kq)  # giá trịiệu theo tài liệu
        items_wi.append(item_wi)
    return items_wi

# similarity
def similarity(wi, results):
    ''' Tính độ tương đồng của câu'''
    if len(wi) <= 0:
        print("Array WI NO data!")
        return 0
    else:
        arr = []
        arr_qd = []
        cosin = []
        for i in wi:
            a = 0.0
            for j in i:
                a += math.pow(j,2)
            arr.append(round(math.sqrt(a), 4))# tinh q2 va d2
        for k in range(1,len(wi)):#tinh q * d
            sum_qd = 0.0
            for h in range(len(wi[0])):
                sum_qd += wi[0][h] * wi[k][h]
            arr_qd.append(sum_qd)

        for m in range(len(arr_qd)):# tinh goc cosin = q*d / (q2 * d2)
            tmp = []
            rs = arr_qd[m] / (arr[0] * arr[m + 1])
            tmp.append(results[m + 1])
            tmp.append(round(rs, 4))
            cosin.append(tmp)
        # format arr cosin : [['câu hỏi', giá trị cosin], ['câu hỏi', giá trị cosin]]
        return cosin
def choose_document(cosin):
    rs = sorted(cosin, key=lambda cosin: cosin[1], reverse=True)
    i_of_rs = 0
    kq_choose = []
    while i_of_rs <= math.ceil(len(rs) / 2):
        kq_choose.append(rs[i_of_rs])
        i_of_rs += 1
    return kq_choose

def print_document(choose_doc):
    for i in choose_doc:
        for j in i:
            print(j)
def output():
    results = search_index.search_index_main()
    if results == 0:
        print("Không có kết quả phù hợp với câu hỏi!")
    elif len(results) <= 2:
        for j in range(len(results)):
            if j == 0:
                print('Tiền xử lý câu truy vấn: ', results[j])
            else:
                print(results[j])
    else:
        print('Số lượng document sau khi tìm kiếm là: %d' % (len(results) - 1))
        print(results)
        kq_set, data_out, kq_for_tfi = format_data(results)
        print('kq_set')
        print(kq_set)
        print('data_out: mang luu tru du lieu cua tung tai lieu ke ca query')
        print(data_out)
        print('DO DAI MANG DATA OUT')
        print(len(data_out))
        tfi = calculated_tfi(kq_set, kq_for_tfi)
        print('tfi')
        print(tfi)
        dfi = calculated_dfi(tfi)
        print('dfi')
        print(dfi)
        print(len(dfi))
        idfi = calculated_idfi(dfi, data_out)
        print('idfi')
        print(idfi)
        wi = calculated_wi(idfi, tfi)
        print('wi')
        print(len(wi))
        print(wi)
        cosin = similarity(wi, results)
        print(cosin)
        choose_doc = choose_document(cosin)
        print('Các Document được chọn là: ')
        print_document(choose_doc)
#GUI
def format_output(query):
    results = search_index.search_index_main(query)
    if results == 0:
        print("Không có kết quả phù hợp với câu hỏi!")
        return 0
    elif len(results) <= 2:
        for j in range(len(results)):
            if j == 0:
                print('Tiền xử lý câu truy vấn: ', results[j])
            else:
                print(results[j])
    else:
        print('Số lượng document sau khi tìm kiếm là: %d' % (len(results) - 1))
        print(results)
        kq_set, data_out, kq_for_tfi = format_data(results)
        tfi = calculated_tfi(kq_set, kq_for_tfi)
        dfi = calculated_dfi(tfi)
        idfi = calculated_idfi(dfi, data_out)
        wi = calculated_wi(idfi, tfi)
        cosin = similarity(wi, results)
        choose_doc = choose_document(cosin)
        print('Các Document được chọn là: ')
        print_document(choose_doc)
        return choose_doc

if __name__ == '__main__':
    #Quy chế tuyển sinh 2017 vừa được Bộ Giáo dục Đào tạo ban hành có những điểm gì mới so với năm trước ?
    # Cho em hỏi là điểm thi đại học của em dưới điểm sàn thì có được nộp nguyện vọng 2 vào các trường cao đẳng không ?
    output()