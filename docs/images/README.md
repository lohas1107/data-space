# 圖片編輯與匯出

## 原稿與產物

| 檔案 | 用途 |
|---|---|
| [dataspace-services.html](dataspace-services.html) | 主圖唯一原稿；包含可編輯、自含樣式的 SVG 與架構說明，可直接在瀏覽器開啟並水平捲動。 |
| [dataspace-architecture.png](dataspace-architecture.png) | 由原稿匯出的主圖，供 [README](../../README.md#架構圖) 使用。 |
| [render_architecture.py](render_architecture.py) | 讀取 HTML 內的 SVG，以 CairoSVG 匯出 PNG。 |

七張循序圖直接維護於[六份流程文件](../../README.md#流程文件)的 `mermaid` 區塊，各圖獨立編號。分區底色、字型與排版設定都在區塊內；Participant／Provider／Consumer 使用淡米色、Federation Services 使用淡綠色、外部系統使用淡灰色。循序圖由支援 Mermaid 的 Markdown 閱讀器呈現，不加入循序圖 PNG 或圖片匯出流程。

## 依賴與執行目錄

主圖匯出需要 Python 3、`CairoSVG==2.9.1`、系統 libcairo 與 **Noto Sans CJK TC** 字型。字型取自本機，不依賴網路字型。

例如在 Debian／Ubuntu 安裝系統依賴（需要套件管理權限）：

```bash
sudo apt-get install python3-venv libcairo2 fonts-noto-cjk
```

從專案根目錄執行以下指令，將 Python 匯出依賴安裝在專案外的環境：

```bash
python3 -m venv /tmp/dataspace-image-export-venv
/tmp/dataspace-image-export-venv/bin/python -m pip install CairoSVG==2.9.1
fc-match 'Noto Sans CJK TC'
```

`fc-match` 的結果應為 Noto Sans CJK TC。已有符合版本與字型要求的 Python 環境時可直接使用。

## 匯出主圖

先修改 HTML 內的 SVG，再從**專案根目錄**執行：

```bash
/tmp/dataspace-image-export-venv/bin/python docs/images/render_architecture.py
```

工具以預設 2 倍解析度覆寫 `docs/images/dataspace-architecture.png`。原稿為 1600 × 1460，預設產物為 **3200 × 2920**。輸入原稿與預設輸出位置以腳本所在目錄解析；從其他目錄執行時，請改用腳本的絕對路徑。

若需先檢查暫存 PNG，可指定輸出位置及倍率：

```bash
/tmp/dataspace-image-export-venv/bin/python docs/images/render_architecture.py --output /tmp/dataspace-architecture-check.png --scale 1
```

## 圖面與文件檢查

- 以瀏覽器開啟 HTML，並檢查匯出的 PNG；確認中文、換行、文字邊界與箭頭端點完整，沒有標籤遮擋。
- 主圖須保留全部服務及 13 條摘要連線：加入治理 1、憑證申請與交付 2、管理操作 2、雙方 Control Plane 間 3、資料流控制 2、資料內容 3。圖例不計入連線數。
- 資料內容使用藍色粗實線，方向為 Data Source → Provider Data Plane → Consumer Data Plane → Application。主圖以活動名稱標示階段。
- 以支援 Mermaid 的 Markdown 閱讀器檢查正式文件中的七個區塊，確認各圖從 1 編號、Provider 在左、Consumer 在右、分區底色與中文換行正確，資料內容箭頭為實線。
- 檢查憑證非同步交付、Prepare／Start 同步與回呼分支、Push 的 `par` 區塊，以及 Pull／Push 不同的完成方向。
- 檢查 README 的替代文字、圖例、流程連結、章節錨點與 HTML 說明。提交正式文件及主圖資產；暫存預覽與用於預覽的渲染依賴留在專案外。
