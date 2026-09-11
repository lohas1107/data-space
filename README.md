# data-space

本頁以元件架構圖說明 Dataspace 的功能分工與互動流程，並追蹤本專案各流程的實作進度。

元件依功能分成參與者服務、共用／聯邦服務、營運支援服務。圖中組織 A 提供資料，組織 B 使用資料。

[![Dataspace 元件架構與流程：共用／聯邦服務、組織 A（Provider）、組織 B（Consumer）及營運支援服務；藍色為 Pull 資料、紫色為 Push 資料，實際資料皆由 A 流向 B。](docs/images/dataspace-architecture.png)](docs/images/dataspace-architecture.png)

## 流程說明

①～⑫ 對應架構圖的流程順序。⑨～⑪ 分別記錄 Pull 資料與 Push 資料，共十五列。

實作狀態記錄本專案進度：⬜ 未開始、🚧 進行中、✅ 已完成、➖ 不適用。

| 編號 | 流程 | 說明 | 實作狀態 |
|---|---|---|---|
| ① | 申請加入 | 組織透過 Portal / Marketplace 提交申請，由 Onboarding 處理資料與資格審查。 | ⬜ 未開始 |
| ② | 核准並登錄 | 審核通過後，將成員身分、狀態與服務資訊登錄至 Participant & Trust Registry。 | ⬜ 未開始 |
| ③ | 取得憑證 | 組織的 Identity Service 向 Credential Issuer 申請憑證；Issuer 依資格簽發，交由組織持有與出示。 | ⬜ 未開始 |
| ④ | 刊登資料與政策 | 提供者透過 Portal / Marketplace 的授權管理操作，將資料描述、可見性與使用政策設定至自己的 Control Plane。 | ⬜ 未開始 |
| ⑤ | 同步可見目錄 | Federated Catalog 查詢提供者的 Control Plane，聚合其有權取得的 metadata 與資料供應資訊。 | ⬜ 未開始 |
| ⑥ | 搜尋資料 | 消費者透過 Portal / Marketplace 查詢 Federated Catalog，找到資料與提供者。 | ⬜ 未開始 |
| ⑦ | 查詢目錄與驗證資格 | 消費端 Control Plane 查詢提供者目錄；相關互動透過 DCP 出示與驗證憑證，檢查資格及政策條件。 | ⬜ 未開始 |
| ⑧ | 協商合約 | 雙方 Control Plane 透過 DSP 協商資料使用條件，建立協議。 | ⬜ 未開始 |
| ⑨ | Pull 資料 | **準備並請求傳輸：** B 準備資料平面，再由 Control Plane 依協議向 A 提出傳輸請求。 | ⬜ 未開始 |
| ⑨ | Push 資料 | **準備並請求傳輸：** B 準備接收端點，將端點與必要存取資訊隨傳輸請求交給 A。 | ⬜ 未開始 |
| ⑩ | Pull 資料 | **啟動資料平面：** A 啟動資料存取，透過雙方 Control Plane 將 A 的端點與必要存取資訊交給 B 的 Data Plane。 | ⬜ 未開始 |
| ⑩ | Push 資料 | **啟動資料平面：** A 的 Control Plane 將 B 的接收端點與必要存取資訊交給 A 的 Data Plane，協調啟動傳輸。 | ⬜ 未開始 |
| ⑪ | Pull 資料 | **實際傳輸：** B 的 Data Plane 主動向 A 請求資料；A 回傳，B 將資料交給應用。 | ⬜ 未開始 |
| ⑪ | Push 資料 | **實際傳輸：** A 的 Data Plane 主動將資料送至 B 的接收端點，B 將資料交給應用。 | ⬜ 未開始 |
| ⑫ | 查詢交換紀錄 | 組織透過 Portal / Marketplace 查詢 Audit / Clearing House，取得協議、交換事件與執行結果。 | ⬜ 未開始 |

目錄同步、資格驗證與事件留存會在相關互動中持續或重複發生。⑫ 表示查詢紀錄，事件從前面的步驟就開始保存。

Pull 資料由消費端發起實際資料請求；Push 資料由提供端主動送至消費端指定的端點。兩者的傳輸流程都由消費者透過 DSP 提出請求。[DSP 傳輸流程](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/blob/2025-1/specifications/transfer/transfer.process.protocol.md)

各協定負責不同的互動：

| 規格 | 互動範圍 | 規範內容 |
|---|---|---|
| [DSP — Dataspace Protocol](https://eclipse-dataspace-protocol-base.github.io/DataspaceProtocol/2025-1/) | 雙方 Control Plane | 目錄查詢、合約協商、傳輸流程訊息與狀態。 |
| [DCP — Decentralized Claims Protocol](https://eclipse-dataspace-dcp.github.io/decentralized-claims-protocol/v1.0.1/) | 憑證簽發者、持有者與驗證者 | 組織身分、憑證申請與出示。 |
| [Data Plane Signaling](https://github.com/eclipse-dataplane-signaling/dataplane-signaling/blob/main/specifications/signaling.md) | Control Plane 與 Data Plane | 資料流準備、啟動、暫停、恢復與結束的控制介面。 |

實際資料使用雙方約定的傳輸協定交換，例如 HTTP 或 MQTT。[DSP 規格範圍](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/blob/2025-1/specifications/common/scope.md)

## 參與者服務

參與者側元件代表組織執行身分驗證、合約協商與資料交換。以下依 [IDS-RAM](https://kb.internationaldataspaces.org/external/ram/) 與 [DSSC Blueprint](https://blueprint.dssc.eu/) 整理功能分工。

| 名稱 | 用途與邊界 | 相關文件連結 |
|---|---|---|
| Control Plane | 管理資料資產與本地目錄、評估政策、協商合約及協調傳輸流程。 | [DSP：互通流程](https://eclipse-dataspace-protocol-base.github.io/DataspaceProtocol/2025-1/)、[DCAT：資料目錄模型](https://www.w3.org/TR/vocab-dcat-3/)、[ODRL：使用政策模型](https://www.w3.org/TR/odrl-model/)、[DRP：資料權利與授權證據](https://github.com/eclipse-dataspace-drp/DataRightsProfile/blob/main/Data%20Rights%20Policy%20Profile.md) |
| Data Plane | 執行實際資料傳輸與傳輸端授權，串接來源或接收端點，依約定進行 Pull 資料或 Push 資料。 | [Data Plane Signaling：資料流控制](https://github.com/eclipse-dataplane-signaling/dataplane-signaling/blob/main/specifications/signaling.md) |
| Identity Service | 管理組織識別、持有的憑證與憑證出示，支援身分及資格驗證。 | [DCP：憑證互動流程](https://eclipse-dataspace-dcp.github.io/decentralized-claims-protocol/v1.0.1/)、[DID：識別碼與識別文件](https://www.w3.org/TR/did-core/)、[VC：可驗證憑證模型](https://www.w3.org/TR/vc-data-model-2.0/) |

圖中的 Data Source 與 Application 是既有資料來源及應用。

## 共用／聯邦服務

共用／聯邦元件協助參與者建立信任、發現資料、共用語意與查詢交換紀錄。

| 名稱 | 用途與邊界 | 相關文件連結 |
|---|---|---|
| Portal / Marketplace | 提供申請加入、刊登、搜尋及交換操作入口，串接相關元件。 | [DSSC Blueprint：資料供應與發現](https://blueprint.dssc.eu/) |
| Onboarding | 管理加入申請、文件審查、核准與退出流程，協調成員登錄及憑證申請資格。 | [IDSA Rulebook：角色、治理與成員管理](https://kb.internationaldataspaces.org/external/rulebook/001_Introduction/) |
| Participant & Trust Registry | 管理成員、狀態、服務端點、受信任簽發者及信任設定，提供查詢。 | [IDSA Rulebook：信任框架與參與資格](https://kb.internationaldataspaces.org/external/rulebook/001_Introduction/) |
| Credential Issuer | 依資格簽發成員或其他資格憑證，管理憑證狀態及撤銷。 | [DCP：憑證申請與簽發](https://eclipse-dataspace-dcp.github.io/decentralized-claims-protocol/v1.0.1/)、[VC：憑證模型](https://www.w3.org/TR/vc-data-model-2.0/)、[CAP：符合性政策與憑證語意](https://eclipse-dataspace-cap.github.io/) |
| Federated Catalog | 聚合有權取得的資料與服務 metadata，提供跨組織搜尋。參與者亦可直接查詢提供者目錄。 | [DCAT：目錄與資料服務描述](https://www.w3.org/TR/vocab-dcat-3/)、[DSP：目錄查詢](https://eclipse-dataspace-protocol-base.github.io/DataspaceProtocol/2025-1/) |
| Vocabulary & Schema | 管理與發布共用詞彙、資料模型、schema 及版本，供參與者描述與解讀資料。 | [DSSC Blueprint：資料模型與語意](https://blueprint.dssc.eu/) |
| Audit / Clearing House | 接收並保存協議與交換事件，提供追溯、稽核及爭議查證。 | [IDSA Rulebook：可觀測性與治理](https://kb.internationaldataspaces.org/external/rulebook/001_Introduction/)、[DSSC Blueprint：來源追溯與交換紀錄](https://blueprint.dssc.eu/) |

Federated Catalog 保存搜尋所需的 metadata；實際資料依協議在參與者之間交換。目錄同步與搜尋結果亦須遵守相應的可見性與存取政策。

## 營運支援服務

營運支援元件提供登入、秘密管理、狀態保存與監控能力，可整合各組織既有的基礎設施。

| 名稱 | 用途與邊界 | 相關文件連結 |
|---|---|---|
| IAM | 管理使用者登入、角色與管理操作授權；Identity Service 則負責組織身分及資格憑證。 | — |
| Secrets / KMS | 保存或管理金鑰、API 秘密與資料來源存取資訊，提供受控存取及金鑰操作。 | — |
| Database | 保存元件所需的資產 metadata、協議、流程狀態、成員及憑證等資料。 | — |
| Observability | 收集日誌、指標與追蹤資訊，支援健康監控及故障排查。 | [DSSC Blueprint：可觀測性](https://blueprint.dssc.eu/) |

「—」表示尚未選定對應技術文件。Observability 支援系統運作，Audit / Clearing House 保存資料交換的業務紀錄。
