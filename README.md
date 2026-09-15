# data-space

data-space 整理 Dataspace 的服務架構、協定流程與 HTTP 端點，涵蓋參與者加入、憑證申請與交付、資料刊登與目錄查詢、合約協商，以及有限資料的 Pull／Push 傳輸。

## 架構圖

[![Dataspace 服務架構：上方為 Federation Services，中央左側為 Provider、右側為 Consumer 的 Participant Agent Services，底部為 Value Creation Services。組織申請者與管理 Client 位於兩側；藍色粗實線表示資料由 Data Source 經雙方 Data Plane 流向 Application。](docs/images/dataspace-architecture.png)](docs/images/dataspace-architecture.png)

## 服務分工

| 服務區 | 元件與用途 |
|---|---|
| Federation Services | Registration System 處理加入申請與治理；Trust Services 群組中的 Issuer Service 簽發及管理 VC。Catalogue Services 支援目錄聚合與發現，Vocabulary Services 支援共用語意，Observability Services 支援交換紀錄與追溯。 |
| Participant Agent Services | 雙方各有 Security Token Service、Credential Service、DID Service（DIDS）、Control Plane 與 Data Plane，分別負責身分 token、VC／VP、DID 文件、協定與政策協調，以及資料流控制與傳輸。 |
| Value Creation Services | 包含 Data Marketplace、Data Analytics Service 與 Cross-Data-Space Artificial Intelligence Service，依使用情境選用。 |

組織申請者透過 Registration System 辦理加入申請，管理 Client 操作所屬組織的服務。Data Source 與 Application 是與 Data Plane 整合的外部系統。此參考架構中的 Catalogue、Vocabulary、Observability 與 Value Creation 為選用支援服務；參與者可直接申請加入，無須經由 Marketplace。服務分類參考 [DSSC Blueprint](https://blueprint.dssc.eu/)，參與者及簽發端邏輯服務依 [DCP 系統模型](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/blob/v1.0.1/specifications/dataspace.ecosystem.md)。

## 流程導覽

| 流程 | 文件 | 內容 |
|---|---|---|
| 1 | [加入治理與 DID 準備](docs/participant-onboarding.md) | 加入申請、治理核准，以及建立或沿用可解析的 DID。 |
| 2 | [憑證申請與交付](docs/credential-issuance.md) | DCP CIP 申請受理、非同步 VC 交付與身分／憑證名詞。 |
| 3 | [資料刊登與目錄存取](docs/catalog-access.md) | 資料刊登、版本與端點探索，以及經 DCP 身分與 VP 驗證的目錄查詢。 |
| 4 | [合約協商](docs/contract-negotiation.md) | Request 至 FINALIZED 的成功路徑。 |
| 5 | [Pull 資料傳輸](docs/transfer-pull.md) | Consumer 使用 Provider 的 DataAddress 請求資料，並通知傳輸完成。 |
| 5 | [Push 資料傳輸](docs/transfer-push.md) | Provider 主動傳送，使用 Consumer 的 DataAddress，由 Provider 通知完成；資料可與啟動通知並行。 |

流程文件說明前置條件、服務責任、訊息順序與實作注意事項。傳輸章節涵蓋有限資料傳輸的成功流程，以及準備與啟動操作的同步回應和非同步回呼。訊息接收確認（ACK）、錯誤處理、重試、暫停、終止與內部驗證要求，請查閱對應規格。

## HTTP 端點設計

[HTTP 端點設計](docs/endpoint-design.md)整理各服務的 Base URL、HTTP method、端點路徑與用途，並區分規格路徑、自訂管理介面及 HTTP 資料傳輸示例。

## 規格基準

文件依據下列規格版本。互通實作須確認雙方共同支援的 binding、DID method 與 profile。

| 規格 | 版本 | 範圍 |
|---|---|---|
| [Dataspace Protocol（DSP）](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/tree/2025-1-err2/specifications) | 2025-1-err2 | 版本與端點探索、目錄、合約協商、傳輸流程訊息及狀態。 |
| [Decentralized Claims Protocol（DCP）](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/tree/v1.0.1/specifications) | 1.0.1 | 參與者身分 token、Credential Issuance Protocol（CIP）及 Verifiable Presentation Protocol（VPP）。 |
| [Data Plane Signaling](https://github.com/eclipse-dataplane-signaling/dataplane-signaling/blob/v1.0-RC4/specifications/signaling.md) | 1.0-RC4（候選版） | Control Plane 與 Data Plane 間的準備、啟動、完成及其他資料流控制。 |
| [DID Core](https://www.w3.org/TR/2022/REC-did-core-20220719/) | 1.0 | DID、DID 文件及邏輯解析；實際解析方式依 DID method。 |

DSP 定義目錄、合約協商與傳輸控制，身分與信任機制可搭配 DCP。此參考架構中的目錄查詢使用 DCP 驗證身分與資格；實際資料傳輸協定由雙方約定的 profile 決定。[DSP 範圍](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/blob/2025-1-err2/specifications/common/scope.md)、[DCP 與 DSP 的關係](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/blob/v1.0.1/specifications/dataspace.ecosystem.md#interrelation-to-the-dataspace-protocol)

## 編輯與匯出圖片

修改架構圖或循序圖時，請參閱[圖片編輯說明](docs/images/README.md)中的原稿位置、環境設定、匯出指令與檢查步驟。
