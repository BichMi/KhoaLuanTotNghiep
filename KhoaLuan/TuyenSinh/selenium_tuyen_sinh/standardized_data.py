"""
    Tiền xử lý dữ liệu với những từ viết tắt thuộc Tuyển Sinh
"""
import re
arr_old_words = [u'nv',u'NV', u'Nv1', u'nv1',u'NV1', u'nv2',u'NV2', u'nv3',u'NV3',u'đk', u'dk', u'dh', u'đh',u'ĐH',
                 u'DH', u'ts', u'ntn', u'kv', u'KV', u'KV1', u'kv1', u'KV2',u'kv2', u'KV3', u'kv3', u'kí',u'CD', u'CĐ',
                 u'cd', u'KHXH', u'GDĐT', u'GD&ĐT', u'QTKD', u'ĐHQG', u'ĐHQGHN', u'ĐHQGTP.HCM',u'TPHCM', u'HCM', u'hcm',
                 u'HN', u'TP',u'tp',u'Tp', u'THPT', u'GD', u'ĐT', u'ĐKDT', u'DKDT', u'SP', u'LĐ', u'DHNN', u'ĐHNN',
                 u'CNTT', u'ĐHKHXHNV', u'HV', u'ĐHSP', u'ĐHBK', u'ĐHCNTT', u'KHTN', u'CĐSP', u'GDTX', u'TTDN']
arr_new_words = [u'nguyện vọng',u'nguyện vọng', u'nguyện vọng 1',u'nguyện vọng 1', u'nguyện vọng 1', u'nguyện vọng 2',u'nguyện vọng 2',
                 u'nguyện vọng 3',u'nguyện vọng 3',u'đăng ký', u'đăng ký',u'đại học', u'đại học',u'đại học',u'đại học',
                 u'tuyển sinh', u'như thế nào', u'khu vực', u'khu vực', u'khu vực 1',u'khu vực 1', u'khu vực 2', u'khu vực 2',
                 u'khu vực 3',u'khu vực 3', u'ký',u'Cao đẳng', u'Cao đẳng', u'Cao đẳng', u'Khoa học xã hội',
                 u'Giáo dục và đào tạo', u'Giáo dục và đào tạo', u'Quản trị kinh doanh', u'Đại học Quốc gia', u'Đại học Quốc gia Hà Nội',
                 u'Đại học Quốc gia Thành phố Hồ Chí Minh', u'Thành phố Hồ Chí Minh', u'Hồ Chí Minh',u'Hồ Chí Minh',
                 u'Hà Nội', u'Thành phố', u'Thành phố', u'Thành phố', u'Trung học phổ thông', u'Giáo dục',
                 u'Đào tạo', u'đăng ký dự thi', u'đăng ký dự thi', u'Sư phạm', u'Lao động', u'Đại học Ngoại Ngữ',
                 u'Đại học Ngoại Ngữ', u'Công nghệ thông tin', u'Đại học Khoa học Xã hội và Nhân văn', u'Học viện',
                 u'Đại học Sư phạm', u'Đại học Bách khoa', u'Đại học Công Nghệ Thông Tin',
                 u'Khoa học Tự nhiên', u'Cao đẳng Sư Phạm', u'Giáo dục thường xuyên', u'Truyền Thông Doanh Nghiệp']

def format_word(s):
    result = ''
    s = re.findall("""\w+|[,;\-:.!()\[\]\\\"\+\*/?'<>{}]""", s, re.I)# tách từ
    for i in s:
        for j in range(len(arr_old_words)):
            if i == arr_old_words[j]:
                i = arr_new_words[j]
        result += i + ' '

    return result

if __name__ == '__main__':

    s = input('Nhập câu chuỗi s: ')
    print(format_word(s))