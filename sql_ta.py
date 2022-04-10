from re import T
from tkinter import S
import sql_data_input
import sqlapi
from tabulate import tabulate

month = input("想查詢單月還雙月,單月or雙月:")
if month == "單月":
    one_month_date = sql_data_input.one_input_date()
elif month == "雙月":
    startend_month_date= sql_data_input.startend_input_date()
else:
    print("錯誤")
    exit()

Campaign_Obj_text = input("輸入類型")
tr_s =""
Campaign_Obj_lis = ["all","VIDEO_VIEWS","REACH","PRODUCT_CATALOG_SALES","POST_ENGAGEMENT","LINK_CLICKS","CONVERSIONS"]

print (Campaign_Obj_lis)
for campaign_text in Campaign_Obj_lis:
    if campaign_text == Campaign_Obj_text:
        tr_s = campaign_text
        break

if tr_s !="":
    Campaign_Obj_data = tr_s
else:
    print("輸入的類型不正確")
    exit()

if one_month_date != "" :
    re_date = sqlapi.one_select_table(one_month_date,Campaign_Obj_data)
    #for r in re_date:
        #print(r)
elif startend_month_date !="":
    re_date = sqlapi.startend_select_table(startend_month_date[0],startend_month_date[1],Campaign_Obj_data)
    for r in re_date:
        print(r)
else:
    print("沒有查詢日期")



print(tabulate(re_date, headers=re_date[0]))



print("變更")
