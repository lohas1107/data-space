# Endpoint 設計：方案 A

本文件採用「對外使用單一網域，以路徑區分服務」的方案 A，整理六份流程文件所需的 base URL、HTTP method、endpoint 與接收端用途。管理 API 採資源導向設計；DSP、DCP 與 Data Plane Signaling 保留規格指定的 method 與相對路徑。

範圍以流程文件中的成功路徑與必要準備為主，並補列 DCP CIP 明定必要的 Credential Offer API。本文不展開 request／response 規格，也不是完整協定實作或相容性驗證清單。

## 設計原則與規格基準

| 規格 | 固定版本 | 本文件涵蓋範圍 |
|---|---|---|
| [Dataspace Protocol（DSP）](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/tree/2025-1-err2/specifications) | 2025-1-err2 | 版本探索、目錄、合約協商與傳輸控制 |
| [Decentralized Claims Protocol（DCP）](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/tree/v1.0.1/specifications) | 1.0.1 | 憑證申請、交付、提案與 VP 查詢 |
| [Data Plane Signaling](https://github.com/eclipse-dataplane-signaling/dataplane-signaling/blob/v1.0-RC4/specifications/signaling.md) | 1.0-RC4 | 本地 Control Plane 與 Data Plane 的控制及回呼 |
| [DID Core](https://www.w3.org/TR/2022/REC-did-core-20220719/) | 1.0 | DID 與 DID 文件；公開解析方式依 DID method |

### RESTful 與協定路徑

- **管理 API 自訂**：以資源及 HTTP method 表達操作，例如 `POST /applications/{applicationId}/decisions` 表示建立審核決定；加入治理與憑證簽發各自審核。
- **協定 method 與相對路徑保留**：例如 DSP 發起協商使用 `POST /negotiations/request`，不能直接以自訂的 `POST /negotiations` 取代。DSP HTTPS binding 本身即定義為 RESTful API，仍包含 `/request`、`/start` 等動作路徑。
- **Base URL 依部署設定**：網域與服務前綴可以自訂，並透過相應的探索或設定機制提供給呼叫端。DCP 明確允許 base URL 包含子網域或路徑；Signaling 要求 HTTPS，並允許額外的版本前綴。
- **服務保持邏輯分工**：同一網域可將不同前綴路由至不同後端；Provider 與 Consumer 是互動角色，不固定寫入部署路徑。

依據：[DSP Negotiation HTTPS binding](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/blob/2025-1-err2/specifications/negotiation/contract.negotiation.binding.https.md)、[DCP Issuer Service Base URL](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/blob/v1.0.1/specifications/credential.issuance.protocol.md#issuer-service-base-url)、[Signaling Base URL](https://github.com/eclipse-dataplane-signaling/dataplane-signaling/blob/v1.0-RC4/specifications/signaling.md#base-url)。

下文以「規格路徑」「自訂管理介面」「HTTP 自訂示例」標示各組 endpoint 的性質。

## Base URL 與 Endpoint 組合

### 參與者對外入口

以 `org-a` 代表一個參與組織，所有網域皆為部署示例。每個組織有自己的入口，同一組織可同時扮演 Provider 與 Consumer。

| 代號 | Base URL 示例 | 用途 |
|---|---|---|
| `PARTICIPANT` | `https://org-a.example` | 參與者根入口與 DSP 版本探索 |
| `DSP` | `https://org-a.example/dsp/2025-1` | Control Plane 的 DSP 入口及回呼基底 |
| `CS` | `https://org-a.example/dcp/v1` | Credential Service 的 DCP 入口 |
| `MGMT` | `https://org-a.example/api/v1` | 參與者的 DID 與資料刊登管理入口 |
| `DATA` | `https://org-a.example/data` | HTTP 資料傳輸示例入口 |

### Federation 入口

| 代號 | Base URL 示例 | 用途 |
|---|---|---|
| `REG` | `https://federation.example/registration/api/v1` | Registration System 的申請與治理管理 |
| `ISSUER` | `https://federation.example/issuer/dcp/v1` | Issuer Service 的 DCP 入口 |
| `ISSUER_MGMT` | `https://federation.example/issuer/api/v1` | Issuer Service 的簽發審核管理 |

### 參與者內部入口

STS 與本地 signaling 使用內部服務地址；下列網址同樣為部署示例。

| 代號 | Base URL 示例 | 用途 |
|---|---|---|
| `STS` | `https://sts.org-a.internal/v1` | 取得本組織的身分 token |
| `DP_SIG` | `https://dp.org-a.internal/signaling/v1` | Data Plane 接收本地 Control Plane 控制指令 |
| `CP_SIG` | `https://cp.org-a.internal/signaling/v1` | Control Plane 接收本地 Data Plane 回呼 |

### 組合與探索規則

Endpoint 由「base URL ＋ 表中相對路徑」組成。本文的 base URL 均以不含結尾 `/` 的形式表示；實作組合時須保留 base URL 中的服務前綴。

- `{DSP_P}`、`{DSP_C}` 分別是此次互動中 Provider、Consumer 的 `DSP` base URL；`{DATA_P}`、`{DATA_C}` 同理。
- 其他代號依接收組織或服務代入。例如目錄存取流程的 `{CS}` 是 Consumer 的 Credential Service。
- 若 Provider 為 `org-a`、Consumer 為 `org-b`，`{DSP_P}/catalog/request` 展開為 `https://org-a.example/dsp/2025-1/catalog/request`；`{DSP_C}/negotiations/{consumerPid}/offers` 展開為 `https://org-b.example/dsp/2025-1/negotiations/{consumerPid}/offers`。
- Consumer 的 DSP callback base URL 使用其 `DSP` base URL，例如 `https://org-b.example/dsp/2025-1`；後續接上規格定義的協商或傳輸回呼路徑。
- DSP 版本探索入口位於 `{PARTICIPANT}/.well-known/dspace-version`，維持**不帶版本、免驗證**，並宣告實際可用的 DSP 版本、binding 與端點。
- DCP 的 `CS`、`ISSUER` base URL 分別透過 DID 文件中的 `CredentialService`、`IssuerService` 服務資訊提供；Signaling 的 `DP_SIG`、`CP_SIG` 透過本地設定或規格支援的註冊機制配置。
- URL 中的 `/v1` 與 `/2025-1` 是本案路由命名；規格採用版本以上述固定版本為準，實際能力須與探索及設定資訊一致。

依據：[DSP 版本與端點探索](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/blob/2025-1-err2/specifications/common/common.protocol.md)、[DSP 協商回呼](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/blob/2025-1-err2/specifications/negotiation/contract.negotiation.binding.https.md)、[DCP Credential Service 探索](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/blob/v1.0.1/specifications/verifiable.presentation.protocol.md#credential-service-endpoint-discovery)、[DCP Issuer Service 探索](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/blob/v1.0.1/specifications/credential.issuance.protocol.md#issuer-service-endpoint-discovery)、[Signaling 註冊](https://github.com/eclipse-dataplane-signaling/dataplane-signaling/blob/v1.0-RC4/specifications/signaling.md)。

## Endpoint 清單

### 1. 治理、身分與刊登管理【自訂管理介面】

對應流程：[加入治理與 DID 準備](participant-onboarding.md)、[憑證申請與交付](credential-issuance.md)、[資料刊登與目錄存取](catalog-access.md)。

| Method | Endpoint | 接收端／用途 |
|---|---|---|
| POST | `{REG}/applications` | Registration／提交加入申請 |
| GET | `{REG}/applications/{applicationId}` | Registration／查詢申請與核准狀態 |
| POST | `{REG}/applications/{applicationId}/decisions` | Registration／建立審核決定，若由管理介面操作 |
| POST | `{MGMT}/dids` | DIDS／建立 DID 與必要金鑰 |
| PUT | `{MGMT}/dids/{did}/document` | DIDS／更新、發布 DID 文件 |
| POST | `{STS}/tokens` | STS／取得 Self-Issued ID Token，各流程共用 |
| POST | `{ISSUER_MGMT}/requests/{requestId}/decisions` | Issuer／建立憑證申請審核決定，若採人工審核 |
| POST | `{MGMT}/catalog/datasets` | Provider Control Plane／刊登資料描述與使用政策 |
| PUT | `{MGMT}/catalog/datasets/{datasetId}` | Provider Control Plane／更新刊登內容 |

刊登設計以同一個管理資源承載資料描述與使用政策。DID 管理端點用於組織操作；DID 的公開解析路徑須依選定的 DID method 決定。

### 2. DCP 憑證與 VP【規格路徑】

對應流程：[憑證申請與交付](credential-issuance.md)、[受保護目錄查詢](catalog-access.md#受保護目錄查詢)。路徑採用 [CIP 1.0.1](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/blob/v1.0.1/specifications/credential.issuance.protocol.md) 與 [VPP 1.0.1](https://github.com/eclipse-dataspace-dcp/decentralized-claims-protocol/blob/v1.0.1/specifications/verifiable.presentation.protocol.md)。

| Method | Endpoint | 接收端／用途 |
|---|---|---|
| GET | `{ISSUER}/metadata` | Issuer／查詢可申請的憑證種類 |
| POST | `{ISSUER}/credentials` | Issuer／申請 VC |
| GET | `{ISSUER}/requests/{requestId}` | Issuer／查詢簽發申請狀態 |
| POST | `{CS}/credentials` | Credential Service／接收非同步交付的 VC |
| POST | `{CS}/offers` | Credential Service／接收 Issuer 的憑證提案 |
| POST | `{CS}/presentations/query` | Credential Service／供 Verifier 查詢 VP |

`POST /credentials` 在 Issuer 與 Credential Service 各有不同用途，透過不同 base URL 區分。`POST {CS}/offers` 雖未在六份流程的循序圖中使用，仍是 CIP 1.0.1 明定的必要端點。

### 3. DSP 版本探索與目錄【規格路徑】

對應流程：[資料刊登與目錄存取](catalog-access.md)。路徑採用 [DSP 版本探索](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/blob/2025-1-err2/specifications/common/common.protocol.md) 與 [Catalog HTTPS binding](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/blob/2025-1-err2/specifications/catalog/catalog.binding.https.md)。

| Method | Endpoint | 接收端／用途 |
|---|---|---|
| GET | `{PARTICIPANT}/.well-known/dspace-version` | Control Plane／探索 DSP 版本、binding 與端點；不帶版本、免驗證 |
| POST | `{DSP_P}/catalog/request` | Provider Control Plane／接收 Consumer 的受保護目錄查詢 |

各參與者的 Connector 均提供版本探索入口；文件中的目錄流程由 Consumer 查詢 Provider。

### 4. DSP 合約協商【規格路徑】

對應流程：[合約協商](contract-negotiation.md)。路徑採用 [Negotiation HTTPS binding](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/blob/2025-1-err2/specifications/negotiation/contract.negotiation.binding.https.md)。

| Method | Endpoint | 接收端／用途 |
|---|---|---|
| POST | `{DSP_P}/negotiations/request` | Provider Control Plane／接收 Consumer 發起的 Request |
| POST | `{DSP_C}/negotiations/{consumerPid}/offers` | Consumer Control Plane／接收 Provider 的 Offer |
| POST | `{DSP_P}/negotiations/{providerPid}/events` | Provider Control Plane／接收 Consumer 的 ACCEPTED |
| POST | `{DSP_C}/negotiations/{consumerPid}/agreement` | Consumer Control Plane／接收 Provider 的 Agreement |
| POST | `{DSP_P}/negotiations/{providerPid}/agreement/verification` | Provider Control Plane／接收 Consumer 的協議確認 |
| POST | `{DSP_C}/negotiations/{consumerPid}/events` | Consumer Control Plane／接收 Provider 的 FINALIZED |

此處的 `providerPid`、`consumerPid` 是各方的**協商流程 ID**。ACCEPTED 與 FINALIZED 使用相同的 `/events` 路徑形式，分別由不同角色接收。

### 5. DSP Pull／Push 傳輸控制【規格路徑】

對應流程：[Pull 資料傳輸](transfer-pull.md)、[Push 資料傳輸](transfer-push.md)。路徑採用 [Transfer HTTPS binding](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/blob/2025-1-err2/specifications/transfer/transfer.process.binding.https.md)。

| Method | Endpoint | 接收端／用途 |
|---|---|---|
| POST | `{DSP_P}/transfers/request` | Provider Control Plane／接收 Consumer 發起的 Pull 或 Push 傳輸請求 |
| POST | `{DSP_C}/transfers/{consumerPid}/start` | Consumer Control Plane／接收 Provider 的 TransferStart |
| POST | `{DSP_P}/transfers/{providerPid}/completion` | Provider Control Plane／接收 Consumer 的有限 Pull 完成通知 |
| POST | `{DSP_C}/transfers/{consumerPid}/completion` | Consumer Control Plane／接收 Provider 的有限 Push 完成通知 |

此處的 `providerPid`、`consumerPid` 是各方的**傳輸流程 ID**，與協商流程 ID 分屬不同流程。Pull 與 Push 共用控制端點形式；有限 Pull 由 Consumer 通知 Provider 完成，有限 Push 由 Provider 通知 Consumer 完成。

### 6. Data Plane Signaling【規格路徑】

對應流程：[Pull 資料傳輸](transfer-pull.md)、[Push 資料傳輸](transfer-push.md)。路徑採用 [Signaling 1.0-RC4 Data Flow API](https://github.com/eclipse-dataplane-signaling/dataplane-signaling/blob/v1.0-RC4/specifications/signaling.md#data-flow-api)。

`DP_SIG`、`CP_SIG` 指向同一參與組織內的對應服務。各組織均使用此組路徑，實際接收角色依流程步驟決定。

| Method | Endpoint | 接收端／用途 |
|---|---|---|
| POST | `{DP_SIG}/dataflows/prepare` | Consumer Data Plane／接收本地 Control Plane 的 Prepare |
| POST | `{DP_SIG}/dataflows/start` | Provider Data Plane／接收本地 Control Plane 的 Start |
| POST | `{DP_SIG}/dataflows/{id}/started` | Consumer Data Plane／接收本地 Control Plane 的 Started Notification |
| POST | `{DP_SIG}/dataflows/{id}/completed` | Data Plane／接收本地 Control Plane 的 Completed；Pull 為 Provider，Push 為 Consumer |
| POST | `{CP_SIG}/transfers/{dataFlowId}/dataflow/prepared` | Consumer Control Plane／接收本地 Data Plane 的非同步 Prepared 回呼 |
| POST | `{CP_SIG}/transfers/{dataFlowId}/dataflow/started` | Provider Control Plane／接收本地 Data Plane 的非同步 Started 回呼 |
| POST | `{CP_SIG}/transfers/{dataFlowId}/dataflow/completed` | Control Plane／接收本地 Data Plane 完成回呼；Pull 為 Consumer，Push 為 Provider |

Prepare、Start 採非同步處理時，才使用相應的 Prepared、Started 回呼。`/dataflows/{id}/started` 是送往 Data Plane 的通知，與送往 Control Plane 的 `/transfers/{dataFlowId}/dataflow/started` 回呼不同。

路徑參數沿用規格的 `{id}` 與 `{dataFlowId}` 命名。Control Plane 回呼中的 `dataFlowId` 須對應原 Prepare 或 Start 的資料流識別碼；不假設它等同 DSP 的傳輸 PID。

### 7. 實際資料傳輸【HTTP 自訂示例】

下列 endpoint 僅作選用 HTTP Pull／Push 時的設計示例；須由所選 transfer profile 確認 method、路徑及實際存取方式，再透過 DataAddress 提供可用地址。DSP 本身不定義實際資料傳輸協定。[DSP 範圍](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol/blob/2025-1-err2/specifications/common/scope.md)

| Method | Endpoint | 接收端／用途 |
|---|---|---|
| GET | `{DATA_P}/{dataFlowId}` | Provider Data Plane／接收 Consumer 的資料拉取請求 |
| POST | `{DATA_C}/{dataFlowId}` | Consumer Data Plane／接收 Provider 推送的資料 |

此處以 `dataFlowId` 作為自訂地址的路徑參數，不表示規格要求從 signaling ID 推算資料 URL。Pull 使用 Provider 提供的 DataAddress，Push 使用 Consumer 準備的 DataAddress；Data Source 與 Application 的整合路徑則依既有系統介面決定。

## 範圍與後續相容性驗證

- 本文件採用六份流程的成功路徑，並保留管理介面的實作選擇；完整 binding 中的其他查詢、協商往返、暫停、終止等端點須另行核對。
- Credential Offer API 是本次補列的 CIP 必要端點；其他端點是否必要，仍以各協定及選定 profile 的要求為準。
- Method 與相對路徑符合規格，只能確認路由設計；完整相容性還須驗證協定訊息、狀態轉移、身分與權限，以及選定 binding、DID method、profile 的要求。
- URL 為示例，實際部署地址須與探索資訊、DID 服務資訊及本地服務設定一致。

## 相關流程文件

- [加入治理與 DID 準備](participant-onboarding.md)
- [憑證申請與交付](credential-issuance.md)
- [資料刊登與目錄存取](catalog-access.md)
- [合約協商](contract-negotiation.md)
- [Pull 資料傳輸](transfer-pull.md)
- [Push 資料傳輸](transfer-push.md)
- [README 架構圖與規格基準](../README.md)
