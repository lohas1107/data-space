# data-space

本專案以架構圖呈現 Dataspace 的服務分工，並以各流程文件的循序圖說明參與者加入、憑證申請與交付、目錄查詢、合約協商及有限資料傳輸。

## 架構圖

[![Dataspace 服務架構與 13 條階段摘要連線：上方 Federation Services、中央左側 Provider 與右側 Consumer Participant Agent、底部 Value Creation Services。組織申請者與管理 Client 位於兩側；藍色粗實線箭頭由 Data Source 經 Provider、Consumer 的 Data Plane 流向 Application。](docs/images/dataspace-architecture.png)](docs/images/dataspace-architecture.png)

## 服務分工

| 服務區 | 元件與用途 |
|---|---|
| Federation Services | Registration System 處理加入申請與治理；Trust Services 群組中的 Issuer Service 簽發及管理 VC。Catalogue Services 支援目錄聚合與發現，Vocabulary Services 支援共用語意，Observability Services 支援交換紀錄與追溯。 |
| Participant Agent Services | 雙方各有 Security Token Service、Credential Service、Decentralized Identifier Service、Control Plane 與 Data Plane，分別負責身分 token、VC／VP、DID 文件、協定與政策協調，以及資料流控制與傳輸。 |
| Value Creation Services | 保留 Data Marketplace、Data Analytics Service 與 Cross-Data-Space Artificial Intelligence Service，依使用情境選用。 |

組織申請者放在 Registration System 左側，兩個管理 Client 放在各自 Participant Agent 外側。Data Source 與 Application 是既有外部系統，保留在各自 Data Plane 下方。Catalogue、Vocabulary、Observability 與 Value Creation 為選用支援服務，沒有強制串入流程；Marketplace 也不是加入流程的必要入口。服務分類參考 [DSSC Blueprint](https://blueprint.dssc.eu/)，參與者及簽發端邏輯服務依 [DCP 系統模型](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/blob/v1.0.1/specifications/dataspace.ecosystem.md)。

## 流程文件

| 文件 | 內容 |
|---|---|
| [加入治理與 DID 準備](docs/participant-onboarding.md) | 加入申請、治理核准，以及建立或沿用可解析的 DID。 |
| [憑證申請與交付](docs/credential-issuance.md) | DCP CIP 申請受理、非同步 VC 交付與身分／憑證名詞。 |
| [資料刊登與目錄存取](docs/catalog-access.md) | 資料刊登與版本探索、DCP 身分及 VP 驗證後的受保護目錄查詢；包含兩張循序圖。 |
| [合約協商](docs/contract-negotiation.md) | Request 至 FINALIZED 的成功路徑。 |
| [Pull 資料傳輸](docs/transfer-pull.md) | Consumer 請求資料，使用 Provider 的 DataAddress，由 Consumer 通知完成。 |
| [Push 資料傳輸](docs/transfer-push.md) | Provider 主動傳送，使用 Consumer 的 DataAddress，由 Provider 通知完成；資料可與啟動通知並行。 |

每份文件包含前置條件、參與服務、Mermaid 循序圖、必要分支與規格邊界。傳輸流程採有限資料的成功路徑，保留同步／回呼分支，省略例行 ACK、錯誤、重試、暫停、終止及服務內部驗證細節。

## 規格基準

以下為本圖固定採用的版本，實作互通仍須確認共同採用的 binding、DID method 與 profile。

| 規格 | 版本 | 範圍 |
|---|---|---|
| [Dataspace Protocol（DSP）](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/tree/2025-1-err2/specifications) | 2025-1-err2 | 版本與端點探索、目錄、合約協商、傳輸流程訊息及狀態。 |
| [Decentralized Claims Protocol（DCP）](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/tree/v1.0.1/specifications) | 1.0.1 | 參與者身分 token、Credential Issuance Protocol（CIP）及 Verifiable Presentation Protocol（VPP）。 |
| [Data Plane Signaling](https://github.com/eclipse-dataplane-signaling/dataplane-signaling/blob/v1.0-RC4/specifications/signaling.md) | 1.0-RC4（候選版） | Control Plane 與 Data Plane 間的準備、啟動、完成及其他資料流控制。 |
| [DID Core](https://www.w3.org/TR/2022/REC-did-core-20220719/) | 1.0 | DID、DID 文件及邏輯解析；實際解析方式依 DID method。 |

DSP 未限定採用 DCP，也不定義實際資料傳輸協定。本圖選用 DCP 保護目錄互動，並以「Data Transfer Protocol（依 profile）」保留資料傳輸方式的選擇。[DSP 範圍](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/blob/2025-1-err2/specifications/common/scope.md)、[DCP 與 DSP 的關係](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/blob/v1.0.1/specifications/dataspace.ecosystem.md#interrelation-to-the-dataspace-protocol)

## 編輯與匯出圖片

原稿位置、依賴、匯出指令與圖面檢查方式見[圖片編輯說明](docs/images/README.md)。
