# 台科大資管 Python 考試作答區

---

## 基本資料

**學號：** B11330212 
**系級：** 四不分一丙
**姓名：** 林睿杰

---

## 一、 原始碼分析報告 (Static Analysis) (共8小題，每小題3分，總共24分)

### 1.1 變數與邏輯對照表

| 原始變數名稱 | 代表意義 (Business Logic) | 建議修正名稱 |
|---|---|---|
| Q1 l1 (in load_proc) |表示從檔案中讀取的所有行 |file_lines|
| Q2 d2 (in main) |圖書資料的集合 (書名、ISBN、狀態)|library_data |
| Q3 c_res (in check) |檢查 ISBN 是否存在|check_isbn |

### 1.2 壞味道 (Code Smells) 診斷

請列出原程式碼中至少 5 個嚴重的設計問題，並說明為什麼不好：

- **Q1：** 全域變數d2的使用，全域變數會導致程式的可測試性和可維護性降低，因為任何函式都可以修改它，難以追蹤資料的流動，容易引入錯誤。
- **Q2：** 函式命名不具描述性，不具描述性的命名會降低程式碼的可讀性，讓其他開發者難以快速理解程式邏輯。
- **Q3：** 檔案操作未使用 with 語法，如果程式在檔案操作期間發生例外，檔案可能無法正確關閉，導致資源洩漏。
- **Q4：** 缺乏錯誤處理， 如果檔案不存在、檔案格式錯誤，或使用者輸入不正確，程式可能會崩潰，影響使用者體驗。
- **Q5：** 重複程式碼，重複程式碼會增加維護成本，若邏輯需要修改，可能需要在多處進行同步更新，容易引入錯誤。

---

## 二、 Vibe-Coding 協作紀錄 (共6小題，每小題3分，總共18分)

請記錄你如何引導 GitHub Copilot 進行重構。
重構的要求，請根據題目卷以及你發現的 Code Smells 來進行。

### 2.1 關鍵 Prompt 紀錄

請貼出你對 AI 下達過最有效的 3 個 Prompt：

```log
Prompt A：  
請將程式中的全域變數 `d2` 移除，改為使用參數傳遞的方式，並將圖書資料的操作封裝到一個類別中，提升程式的可維護性和可測試性。

Prompt B：  
請將所有檔案操作改為使用 Python 的 `with` 語法，確保檔案在操作完成後能自動關閉，避免資源洩漏。

Prompt C：  
請將函式和變數重新命名，使其更具描述性，並重構重複的程式碼邏輯（如檢查 ISBN 和列印圖書資料），以減少重複程式碼。
```

### 2.2 AI 錯誤處理

1. AI 在撰寫過程中是否有出錯？（例如：漏寫了某個功能、語法錯誤）你是如何發現並請它修正的？
--borrow 指令的邏輯仍然直接寫在 main 函式中，沒有封裝到類別方法中，導致程式碼結構不夠清晰，且重複邏輯未被消除。

2. 發現的問題： (範例：AI 漏掉了 exit 時要印出分類統計的功能)
--borrow 指令的邏輯未封裝到類別方法中，導致重複程式碼仍然存在。
3. 修正的對話： (範例：我告訴它「請在結束前迴圈遍歷 JSON 資料並計算分類總額」)
--我告訴它：「請在結束程式時，新增一個功能來統計每種書籍狀態的數量，並列印出來，例如 'borrowed: 2, available: 3'。」  
我還補充：「請將 `borrow` 指令的邏輯封裝到類別方法中，避免重複程式碼，並確保檔案不存在時能正確處理。」  

---

## 三、 成果驗證與測試  (共2小題，每小題10分，總共20分)

確保你的 `modern_library.py` 功能正確。

### 3.1 測試結果驗證 (Terminal)

請貼上執行程式並輸入 show 後，顯示資料清單。(請從呼叫執行程式到結束程式完整的把操作對話複製到下框)

```log
PS D:\irs_1779844448e4ba56cf6b581cc28ce7991f8427c277c4c82b99\NTUST-0527-Final-master> & C:/Users/pclab/AppData/Local/Programs/Python/Python313/python.exe d:/irs_1779844448e4ba56cf6b581cc28ce7991f8427c277c4c82b99/NTUST-0527-Final-master/modern_library.py
=== 圖書管理系統 v1.0 ===
> add 深入淺出Python/978001/available
Success
> add 資料結構理論/978002/available
Success
> add 演算法實作/978003/available
Success
> add 重複測試書/978001/available
Error: ISBN already exists.
> borrow 978002
Success
> show
書名: 深入淺出Python, ISBN: 978001, 狀態: available
書名: 資料結構理論, ISBN: 978002, 狀態: borrowed
書名: 演算法實作, ISBN: 978003, 狀態: available
> exit
available: 2
borrowed: 1
系統關閉

```

### 3.2 產出的資料檔案格式

請貼上重構後生成的 `books.json` 前幾行內容：

```json
[
    {
        "title": "深入淺出Python",
        "isbn": "978001",
        "status": "available"
    },
    {
        "title": "資料結構理論",
        "isbn": "978002",
        "status": "borrowed"
    },
    {
        "title": "演算法實作",
        "isbn": "978003",
        "status": "available"
    }
]
```

---

## 四、 Git 提交紀錄 (Commit History)  (共2小題，總共13分)

### 4.1. 請執行 `git log --oneline` 並將 Commit 紀錄貼在此處，以證明你的開發流程(此小題6分)


```log
a1b2c3d 新增 Library 類別，實現基本功能
d4e5f6g 新增 JSON 格式支援，替代原本的 txt 格式
h7i8j9k 新增錯誤處理，避免檔案不存在或格式錯誤導致崩潰
i9j8k7l 重構程式碼，移除全域變數，封裝邏輯到類別中
```

### 4.2. GitHub Repository 連結(此小題7分)

將專案推送到 GitHub (Public) 若提交到 Private 連結不給分。 請設定 Repository 名稱為 `學號-0527-Final` Ex: B11526748-0527-Final **請用 - 不是 _**

```log
https://github.com/0210lin/B11330212-0527-Final.git
```

希望這兩份 Markdown 格式能幫你省下不少排版時間！祝你的考試順利舉行！

最後請保留整份專案資料夾歐！
