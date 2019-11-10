#! python3
# coding=UTF-8
import requests
import bs4
import csv


# 開啟輸出的 CSV 檔案
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    mp3_file = 'hello'
    writer.writerow(['單字', '音標', '[sound:'+mp3_file+'.mp3]','解釋'])





if __name__== "__main__":
    main()