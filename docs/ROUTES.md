# API Routes Documentation — 活動報名系統

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| 首頁 | GET | `/` | `index.html` | 顯示熱門或即將到來的活動 |
| 活動列表 | GET | `/events` | `event_list.html` | 顯示所有活動，支援分類篩選 |
| 搜尋活動 | GET | `/search` | `search_results.html` | 依關鍵字搜尋活動 |
| 活動詳情 | GET | `/events/<int:id>` | `event_detail.html` | 顯示單一活動完整資訊與報名按鈕 |
| 報名頁面 | GET | `/events/<int:id>/register` | `registration_form.html` | 顯示報名表單 |
| 提交報名 | POST | `/events/<int:id>/register` | — | 接收報名資料，存入 DB，重導向至成功頁 |
| 報名成功頁 | GET | `/registration/success` | `registration_success.html` | 顯示報名成功訊息與資訊 |
| 活動管理 (列表) | GET | `/admin/events` | `admin/event_list.html` | 主辦方管理活動頁面 |
| 新增活動頁面 | GET | `/admin/events/new` | `admin/event_form.html` | 顯示新增活動表單 |
| 建立活動 | POST | `/admin/events/new` | — | 接收活動資料，存入 DB |
| 編輯活動頁面 | GET | `/admin/events/<int:id>/edit` | `admin/event_form.html` | 顯示編輯活動表單 |
| 更新活動 | POST | `/admin/events/<int:id>/update` | — | 接收更新資料，更新 DB |
| 刪除活動 | POST | `/admin/events/<int:id>/delete` | — | 刪除活動後重導向 |

## 2. 每個路由的詳細說明

### 2.1 首頁 & 搜尋
- **`GET /`**
  - 輸入：無
  - 處理：呼叫 `Event.get_all()` 並依時間排序。
  - 輸出：渲染 `index.html`。
- **`GET /search`**
  - 輸入：URL 參數 `q` (關鍵字)。
  - 處理：在資料庫中搜尋標題或描述包含 `q` 的活動。
  - 輸出：渲染 `search_results.html`。

### 2.2 活動詳情 & 報名
- **`GET /events/<int:id>`**
  - 輸入：活動 ID。
  - 處理：呼叫 `Event.get_by_id(id)`。
  - 輸出：若存在則渲染 `event_detail.html`，否則回傳 404。
- **`POST /events/<int:id>/register`**
  - 輸入：表單欄位 `name`, `email`, `phone`。
  - 處理：驗證名額與期限，呼叫 `Registration.create()`。
  - 輸出：重導向至 `/registration/success`。

### 2.3 管理後台
- **`POST /admin/events/new`**
  - 輸入：活動各項資訊。
  - 處理：呼叫 `Event.create()`。
  - 輸出：重導向至活動詳情或管理列表。

## 3. Jinja2 模板清單
- `base.html`: 基礎佈局（導覽列、頁尾）。
- `index.html`: 首頁。
- `event_list.html`: 活動列表頁。
- `event_detail.html`: 活動詳細頁。
- `registration_form.html`: 報名表單。
- `registration_success.html`: 報名成功通知。
- `admin/event_list.html`: 管理端活動列表。
- `admin/event_form.html`: 管理端新增/編輯表單。

## 4. 路由骨架程式碼
檔案位置：
- `app/routes/main.py`
- `app/routes/event.py`
- `app/routes/registration.py`
- `app/routes/admin.py`
