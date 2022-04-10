import time
import datetime

def one_input_date():
    input_date =input("請輸入要查詢月份,格視範例為20220101:")

    '''
    判斷輸入資料是否為數字及符合格式
    input_date.isdigit() 判斷輸入的資料是否只包含數字
    len(input_date) 判斷長度是否為 8
    '''
    if input_date.isdigit() == True and len(input_date) == 8:
        #test_date = datetime.datetime.strptime(input_date, '%Y%m%d')
        #print(test_date) #輸出日期格式為 yyyy-mm-dd 00:00:00
        mi= time.strptime(input_date, "%Y%m%d")
        mi_date = datetime.date(mi.tm_year,mi.tm_mon,mi.tm_mday)
        #print(mi_date)
    else:
        print("輸入格式不合法！請按照樣例格式輸入日期！")

    ''' 
    time.strptime 將格式拆分為 mi.tm_year(年)、mi.tm_mon(月)、mi.tm_mday(日)
    datetime.date 輸出日期格式為 yyyy-mm-dd
    '''
    return mi_date


def startend_input_date():
    input_date_start = input("輸入開始日期,格式為20220101:")

    #檢查開始日期格式
    if input_date_start.isdigit() == True and len(input_date_start) == 8:
        start_date = datetime.datetime.strptime(input_date_start, '%Y%m%d')
        #print(start_date) #輸出日期格式為 yyyy-mm-dd 00:00:00
        mi_start= time.strptime(input_date_start, "%Y%m%d")
        mi_date_start = datetime.date(mi_start.tm_year,mi_start.tm_mon,mi_start.tm_mday)
        #print(mi_date_start) #輸出日期格式為 yyyy-mm-dd
    else:
        print("開始日期格式不正確！")
        exit()


    input_date_end = input("輸入結束日期,格式為20220101:")

    #檢查結束日期格式
    if input_date_end.isdigit() == True and len(input_date_end) == 8:
        end_date = datetime.datetime.strptime(input_date_end, '%Y%m%d')
        #print(end_date) #輸出日期格式為 yyyy-mm-dd 00:00:00
        mi_end= time.strptime(input_date_end, "%Y%m%d")
        mi_date_end = datetime.date(mi_end.tm_year,mi_end.tm_mon,mi_end.tm_mday)
        #print(mi_date_end) #輸出日期格式為 yyyy-mm-dd
    else:
        print("結束日期格式不正確！")
        exit()

    if input_date_end<=input_date_start:
        print("結束日期不能小於等於開始日期")
    else:
        print("正確")
        return mi_date_start,mi_date_end

    
