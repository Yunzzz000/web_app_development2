# Flowchart Documentation (流程圖文件)

## 使用者流程圖 (User Flow)
```mermaid
flowchart LR
    A([使用者開啟網站]) --> B[首頁 – 活動列表]
    B --> C{想做什麼？}
    C -->|查看活動| D[活動詳細頁面]
    D --> E{要報名嗎？}
    E -->|是| F[填寫報名表單]
    F --> G[提交報名]
    G --> H[顯示報名成功訊息]
    E -->|否| I[返回活動列表]
    C -->|搜尋活動| J[搜尋結果頁面]
    J --> D
    C -->|依類型篩選| K[分類列表]
    K --> D
```

## 系統序列圖 (System Sequence Diagram)
```mermaid
sequenceDiagram
    participant User as 使用者
    participant Browser as 瀏覽器
    participant Flask as Flask Route
    participant Model as SQLAlchemy Model
    participant DB as SQLite

    User->>Browser: 點擊「報名」按鈕
    Browser->>Flask: POST /register
    Flask->>Model: create_registration(data)
    Model->>DB: INSERT INTO registrations
    DB-->>Model: 成功
    Model-->>Flask: 返回結果
    Flask-->>Browser: 302 Redirect (成功頁面)
    Browser-->>User: 顯示報名成功訊息
```

## 功能清單對照表 (Feature Table)
| 功能 | URL 路徑 | HTTP 方法 |
|------|----------|----------|
| 刊登活動說明及報名連結 | /events/create | POST |
| 查看活動列表 | /events | GET |
| 搜尋活動 | /events/search | GET |
| 查看活動詳細 | /events/<id> | GET |
| 報名活動 | /events/<id>/register | POST |
| 查看報名人數 | /events/<id>/registrations | GET |
| 用戶登入/註冊 (可選) | /auth | POST |

*此文件由 Antigravity AI 產生，根據 PRD 與 Architecture 產出，可直接放入 GitHub 或 Notion 預覽。*
