# data-space

## Dataspace 規格索引

### 簡介

本索引用於查找與比較 Dataspace 相關規格，整理各項文件的用途、維護組織、官方閱讀入口與發布狀態。協定定義系統之間的互動流程；基礎標準提供共用的資料與身分模型；參考架構、治理規範及建置指引則協助設計與營運資料空間。

Dataspace 的相關文件由多個組織分工維護：Eclipse Foundation 負責互通協定與政策規格專案，IDSA 提供架構與治理文件，Gaia-X 定義其生態系統的架構與信任要求，W3C 提供共用基礎標準。此外，Catena-X 提供產業規範，ISO/IEC 制定國際標準，DSSC 提供建置指引。

### 規格總表

Eclipse Dataspace 的五個規格專案如下。各專案團隊負責開發與維護，Eclipse Dataspace Working Group（EDWG）依 Eclipse 規格流程審核專案建立與發布。[官方分工說明](https://dataspace.eclipse.org/faq/)

| 規格／文件 | 用途 | 維護組織 | 發布狀態 |
|---|---|---|---|
| [DSP — Dataspace Protocol](https://eclipse-dataspace-protocol-base.github.io/DataspaceProtocol/2025-1/) | 互通協定：資料目錄查詢、合約協商與傳輸流程管理。 | Eclipse Foundation／DSP 專案 | 已發布 |
| [DCP — Decentralized Claims Protocol](https://eclipse-dataspace-dcp.github.io/decentralized-claims-protocol/v1.0.1/) | 身分與憑證協定：組織身分識別、可驗證憑證的申請與出示。 | Eclipse Foundation／DCP 專案 | 已發布 |
| [Data Plane Signaling](https://eclipse-dataplane-signaling.github.io/dataplane-signaling/HEAD/) | 傳輸控制協定：控制平面與資料平面之間的訊息、狀態及 API。 | Eclipse Foundation／Data Plane Signaling 專案 | 草案（RC） |
| [CAP — Conformity Assessment Policy and Credential Profile](https://eclipse.dev/dataspace-cap/) | 政策與憑證規格：以共用語意、政策與可驗證憑證表達及檢查符合性要求。 | Eclipse Foundation／CAP 專案 | 未確認 |
| [DRP — Data Rights Policies Profile](https://github.com/eclipse-dataspace-drp/DataRightsProfile/blob/main/Data%20Rights%20Policy%20Profile.md) | 資料權利規格：表達權利持有者的政策與授權證據，銜接信任框架要求。 | Eclipse Foundation／DRP 專案 | 未確認 |

DSP 的早期版本由 International Data Spaces Association（IDSA）維護；後續版本移至 Eclipse Foundation 治理下的 DSP 專案。[官方版本沿革](https://github.com/eclipse-dataspace-protocol-base/DataspaceProtocol#about-versions)

其他相關規格與文件如下，依維護組織排列。每份文件獨立列出；Catena-X Standards 為產業標準集合入口。

| 規格／文件 | 用途 | 維護組織 | 發布狀態 |
|---|---|---|---|
| [IDS-RAM — IDS Reference Architecture Model](https://kb.internationaldataspaces.org/external/ram/) | 參考架構：提供資料空間的架構原則、設計模式與建置建議。 | IDSA／相關工作小組 | 草案（RC） |
| [IDSA Rulebook](https://kb.internationaldataspaces.org/external/rulebook/001_Introduction/) | 治理文件：定義參與角色、治理原則、信任與功能要求。 | IDSA／相關工作小組 | 已發布 |
| [Gaia-X Architecture Document](https://docs.gaia-x.eu/technical-committee/architecture-document/25.11/) | 架構規格：說明 Gaia-X 信任框架、資料交易與技術互通要求。 | Gaia-X Association（AISBL） | 已發布 |
| [Gaia-X Compliance Document](https://docs.gaia-x.eu/policy-rules-committee/compliance-document/3.1.0/) | 符合性規範：定義參與者、服務與信任錨點的要求及評估規則。 | Gaia-X Association（AISBL） | 已發布 |
| [Gaia-X Identity, Credential and Access Management Document（ICAM）](https://docs.gaia-x.eu/technical-committee/identity-credential-access-management/25.11/) | 身分與存取規格：定義數位身分、憑證、授權與存取管理要求。 | Gaia-X Association（AISBL） | 已發布 |
| [Gaia-X Data Exchange Document](https://docs.gaia-x.eu/technical-committee/data-exchange/25.07/) | 資料交換規格：定義資料產品、交換服務、目錄、存取紀錄與使用協議。 | Gaia-X Association（AISBL） | 已發布 |
| [Data Catalog Vocabulary（DCAT）— Version 3](https://www.w3.org/TR/vocab-dcat-3/) | 資料目錄標準：提供描述資料集、資料服務與目錄的共用詞彙。 | W3C | 已發布 |
| [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/) | 政策模型標準：表達資料使用的許可、禁止、義務與限制。 | W3C | 已發布 |
| [Decentralized Identifiers（DIDs）v1.0](https://www.w3.org/TR/did-core/) | 身分識別標準：定義去中心化識別碼、文件模型與驗證方式的表示。 | W3C | 已發布 |
| [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) | 憑證模型標準：定義可驗證憑證與出示資料的結構及角色關係。 | W3C | 已發布 |
| [Catena-X Standards](https://catenax-ev.github.io/docs/standards/overview) | 產業標準集合：規範汽車產業資料空間的資料模型、API、流程與互通要求。 | Catena-X Automotive Network e.V. | 持續更新 |
| [ISO/IEC FDIS 20151-1 — Dataspaces: Concepts and characteristics](https://www.iso.org/standard/86589.html) | 國際標準草案：定義 Dataspace 的基本概念與必要特性。 | ISO/IEC JTC 1/SC 38 | 草案（FDIS） |
| [DSSC Blueprint](https://blueprint.dssc.eu/) | 建置指引：提供資料空間的功能構件、治理方法與規格選用建議。 | Data Spaces Support Centre（DSSC）專案聯盟 | 已發布 |

### 資料來源與更新

最後查核日期：2026-09-10（UTC）。

規格名稱直接連到官方閱讀版；無獨立閱讀版時，使用官方規格版本庫或專案頁。發布狀態描述查核當日所連文件的狀態，不另追蹤最新版本號；正式名稱中的版本與標準編號予以保留。部分連結包含官方版本路徑，部分入口會隨官方更新。

- **已發布**：官方已發布的規格、標準或指引，例如正式 Release 或 W3C Recommendation。
- **草案**：官方標示為 Draft、Release Candidate（RC）或 Final Draft International Standard（FDIS）等尚未定版的文件。
- **持續更新**：官方持續維護的文件或標準集合入口；個別文件的狀態仍須各自確認。
- **未確認**：所連文件的官方資訊不足以確認規格發布狀態，不推定為已發布或草案。

CAP 與 DRP 的所連文件未明確提供可確認的規格發布狀態，因此標為「未確認」。Eclipse 專案的 Incubating 描述專案生命週期，不直接代表規格的發布狀態。IDS-RAM 的 RC 狀態依 [IDSA Knowledge Base 發布說明](https://kb.internationaldataspaces.org/#version-2026-2) 判定。

更新索引時，應逐項核對官方文件、維護組織、發布狀態與連結，再更新整份索引的查核日期。
