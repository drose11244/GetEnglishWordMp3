# 自動製作 Anki 英文單字卡

我們在用Anki背英文單字的時候，可能會需要自己製作屬於自己的單字卡，而這往往在初期花了很多時間。
所以我寫了個程式來幫忙，他會自動到 [劍橋詞典(Cambridge Dictionary)](https://dictionary.cambridge.org/zht/)，來爬他的解釋與發音的聲音檔。

使用方式：
#### 第一步驟：先到input.txt，將要輸入即將查詢的單字。
![](https://i.imgur.com/jJfmlKJ.png)

---

#### 第二步驟：按下主程式 makeAnkiCard_linux，等待下載。
![](https://i.imgur.com/ieJFCYM.png)

---


#### 第三步驟：結束後，output資料夾有兩個檔案，一個是csv，一個語音檔。
![](https://i.imgur.com/qxHa5K3.png)
![](https://i.imgur.com/nHPEHwf.png)
![](https://i.imgur.com/8TarURi.png)

---


#### 第四步驟：按下 左上角 檔案 => 匯入 （將CSV 匯入至Anki）
![](https://i.imgur.com/WpZPzed.png)
![](https://i.imgur.com/QPhSB4B.png)

---

#### 第五步驟：將語音檔放到指定的位置。（將聲音檔放至Anki）
![](https://i.imgur.com/1JembNh.png)

```bash=
Mac路徑：/Users/{{computer's user}}/Library/Application Support/Anki2/{{anki's user}}/collection.media 
```

---

#### 第六步驟：同步資料到Anki，按下右邊的同步。
![](https://i.imgur.com/aA4WFiF.png)

---


### 例外
如果有單字沒有查詢到，會顯示檔名會多加一個error，並放著查詢有問題的單字。

![](https://i.imgur.com/sRkaWzv.png)

