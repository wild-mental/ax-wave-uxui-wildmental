# 교재 출력본 ↔ 온라인 자료실 1:1 매칭표

교재 출력본(2026-11-05, 컬러판·흑백판 107쪽, 두 판의 쪽 번호 같음)이 가리키는 것과 자료실에서 그것이 있는 곳을 한 줄씩 맞춘 표입니다.
- **강사용입니다.** 학생이 보는 매칭표는 자료실 첫 화면 `README.md`입니다(grip T66, 2026-11-17). 이 표는 상태 추적용이며, 쪽·이름이 바뀌면 두 곳을 함께 고칩니다(RULES §4).
- **쪽:** 인쇄된 쪽 번호입니다(PDF 쪽 = 인쇄 쪽). 표지와 목차 쪽은 빼고 본문에서 처음 가리키는 쪽만 적었습니다.
- **상태:** 2026-11-17 기준입니다. 「초안」은 본문은 있지만 캡처와 화면 확인이 남은 상태를 뜻합니다.
- **자료실 주소 앞부분:** `https://wild-mental.github.io/ax-wave-uxui-wildmental/`

## 1. 자료실 입구 (교재에 인쇄된 주소)

| 교재 쪽 | 교재가 가리키는 것 | 자료실 위치 | 상태 |
|---|---|---|---|
| 4 · 95 | 온라인 자료실 (「이 교재를 쓰는 법」, 부록 A 첫 쪽) | `README.md` (첫 화면 = 공개 매칭표: 교재 쪽·절·가이드·함께 쓰는 자료) | 작성 |
| 95 | 자료실 저장소 · 워크시트 문서 원본 | `worksheet-template/worksheet.md` (저장소 화면에서 열기) | 작성 |
| 95 · 97 | Figma 템플릿 링크 | `figma-template/README.md` → 강사 Figma 파일 (예비 SVG 4장 동봉) | 작성 |
| 95 · 96 | 강사 GitHub 아이디 `wild-mental` | `README.md` 「수업 연락처」 | 작성 |
| 97 (A-3 7단계) | "강사가 수업에서 알려 주는 이메일" | `README.md` 「수업 연락처」 (강사 이메일) | 작성 |
| 67 · 96 · 98 (+ 5쪽 도구 표) | 사전 안내 | `pre-course-notice.md` | 작성 |

## 2. 앞부분 자료

| 교재 쪽 | 교재 | 자료실 위치 | 상태 |
|---|---|---|---|
| 9~11 | 공통 PRD · AX YOUR BODY | `textbook-materials/common-prd.md` | 작성 |
| 12~15 | 핵심 타깃 프로필 4종 (프로필 카드) | `textbook-materials/profile-cards.md` | 작성 |
| 13 | 4주치 기록 데이터셋 안내 | `datasets/README.md` + `datasets/{m-general,f-general,m-athlete,f-athlete}/` CSV 4개씩 | 작성 |
| 63 · 64 · 90 | 샘플 DESIGN.md | `kits/DESIGN-axyourbody-sample.md` (3.3절 항목 순서, 11/24 교체) · `kits/DESIGN-axyourbody-sample-B.md` (이전 샘플, 디자인 B 버전) | 작성 |

## 3. 온라인 가이드 27개 (`→ 온라인 가이드: 「이름」`)

| 교재 쪽 | 교재 절 | 가이드 이름 (인쇄본 그대로) | 자료실 파일 (`guides/`) | 상태 |
|---|---|---|---|---|
| 96 | 부록 A-1 | Claude 시작 가이드 | `claude-start-guide.md` | 초안 |
| 96 | 부록 A-2 | GitHub 워크시트 저장소 가이드 | `github-worksheet-repo-guide.md` | 초안 |
| 97 | 부록 A-3 | Figma 템플릿 열기·복제 가이드 | `figma-template-guide.md` | 초안 |
| 97 | 부록 A-4 | Stitch 시작 가이드 | `stitch-start-guide.md` | 초안 |
| 97 | 부록 A-5 | Claude Code 데스크톱 앱 설치 (Mac판 · Windows판) | `claude-code-install-guide.md` | 초안 |
| 99 | 부록 A-6 | GitHub Pages 정적 배포 가이드 | `github-pages-deploy-guide.md` | 초안 |
| 19 | 1.2 | 사례 분석 시트 가이드 | `case-analysis-sheet-guide.md` | 작성 |
| 23 · 28 | 1.4 · 1.5 | 과업·불편 목록 가이드 | `task-pain-list-guide.md` | 작성 |
| 32 | 1.6 | 페르소나 카드 가이드 | `persona-card-guide.md` | 작성 |
| 36 · 43 | 2.2 · 2.4 | 이벤트 보드 사용 가이드 | `event-board-guide.md` | 작성 |
| 46 | 2.5 | 대상 객체 카드 작성 가이드 | `object-card-guide.md` | 작성 |
| 47 | 2.6 | 용어 대조표 작성 가이드 | `term-matching-guide.md` | 작성 |
| 50 | 2.7 | 진입점 선택표 작성 가이드 | `entry-point-guide.md` | 작성 |
| 52 | 2.8 | 서비스 구조 설명서 작성 가이드 | `service-structure-guide.md` | 작성 |
| 52 | 2.9 | 동료 리뷰 진행 가이드 | `peer-review-guide.md` | 작성 |
| 60 | 3.2 | 화면 흐름 순서표 작성 가이드 | `screen-flow-guide.md` | 작성 |
| 64 | 3.4 | 디자인 쇼핑처 둘러보기 가이드 | `design-shopping-guide.md` | 초안 |
| 66 | 3.5 | Stitch 시안 만들기 가이드 | `stitch-draft-guide.md` | 초안 |
| 71 | 3.6 | Claude Code 프로토타이핑 따라 하기 | `claude-code-prototyping-guide.md` | 초안 |
| 74 | 3.7 | AI 판단 화면 신뢰 설계 예시 모음 | `ai-trust-design-examples.md` | 초안 |
| 79 | 4.2 | 여러 버전 통합 가이드 | `version-merge-guide.md` | 초안 |
| 82 | 4.3 | 디자인 스킬 가져오기 가이드 | `design-skill-guide.md` | 초안 |
| 85 | 4.4 | 짝 사용성 테스트 진행 가이드 | `pair-usability-test-guide.md` | 초안 |
| 87 | 4.5 | 파비콘·컬러 샘플 가이드 | `favicon-color-sample-guide.md` | 초안 |
| 90 | 4.6 | 나만의 DESIGN.md 만들기 가이드 | `my-own-design-md-guide.md` | 초안 |
| 92 | 4.7 | 배포 전 점검과 정적 배포 가이드 | `pre-deploy-check-guide.md` | 초안 |
| 93 | 4.8 | 발표·동료 리뷰 진행 가이드 | `presentation-review-guide.md` | 초안 |

## 4. 워크시트 15개

쪽은 그 워크시트의 [실습 안내]가 처음 나오는 쪽입니다.

| 교재 쪽 | 교재 절 | 워크시트 | 자료실 위치 | 상태 |
|---|---|---|---|---|
| 19 | 1.2 | 익숙한 서비스의 사용 경험을 과업 관점으로 뜯어본 사례 분석 시트 | `worksheet.md` Part 1 | 작성 |
| 23 | 1.4 · 1.5 | 타깃 사용자의 해야 할 일과 불편을 정리한 과업·불편 목록 | `worksheet.md` Part 1 | 작성 |
| 31 | 1.6 | 설계 판단의 기준이 되는 타깃 사용자 페르소나 카드 | `worksheet.md` Part 1 | 작성 |
| 36 | 2.2 · 2.4 | 고객 여정 위에 사건과 대상 객체를 붙인 이벤트 보드 | Figma 템플릿 01 (`figma-template/README.md` §01) | 작성 |
| 46 | 2.5 | 서비스가 다루는 대상 객체·속성·관계를 정리한 대상 객체 카드 | `worksheet.md` Part 2 | 작성 |
| 47 | 2.6 | 시스템 내부 용어와 사용자 용어를 맞춘 용어 대조표 | `worksheet.md` Part 2 | 작성 |
| 50 | 2.7 | 메뉴·진입점·위치 표시를 정한 길찾기 진입점 선택표 | `worksheet.md` Part 2 | 작성 |
| 51 | 2.8 | Claude에 넘길 서비스 구조 설명서 | `worksheet.md` Part 2 | 작성 |
| 59 | 3.2 | 과업별 화면 흐름 순서표와 화면 목록 | Figma 템플릿 02 (`figma-template/README.md` §02) | 작성 |
| 63 | 3.4 | 참고할 AI 디자인 가이드(DESIGN.md) 후보 쇼핑 목록 | `worksheet.md` Part 3 | 작성 |
| 65 | 3.5 | Google Stitch로 만든 테마별 화면 시안 비교표 | Figma 템플릿 03 (`figma-template/README.md` §03) | 작성 |
| 71 | 3.6 ~ 4.8 | 테마별로 만든 첫 프로토타입과 버전 기록 | `worksheet.md` Part 3 | 작성 |
| 84 | 4.4 | 사용자 과업으로 시험한 사용성 테스트 기록표 | `worksheet.md` Part 4 | 작성 |
| 90 | 4.6 | 나만의 디자인 가이드(DESIGN.md)와 점검표 | `worksheet.md` Part 4 | 작성 |
| 92 | 4.7 | 공개 전 개인정보·품질을 확인한 배포 전 점검표와 배포 링크 | `worksheet.md` Part 4 | 작성 |

## 5. 지시문 킷

### Part 1·2 지시문 7개 (`kits/claude-prompts-part-1-2.md`, 2026-11-17 추가)

교재에는 이름 없이 [실습 안내] 안에 인쇄된 지시문입니다. 자료실에서 붙인 이름으로 찾습니다. `_context/gen_part12_kit.py`가 원고에서 다시 만듭니다.

| 교재 쪽 | 교재 절 | 지시문 (자료실 이름) | 상태 |
|---|---|---|---|
| 19 | 1.2 | 사례 분석 메모 정리 지시문 | 작성 |
| 27 | 1.5 | 과업 후보 넓히기 지시문 | 작성 |
| 31 | 1.6 | 페르소나 카드 초안 지시문 | 작성 |
| 36 | 2.2 | 흐름이 바뀌는 날 찾기 지시문 | 작성 |
| 43 | 2.4 | 빠진 사건 찾기 지시문 | 작성 |
| 46 | 2.5 | 대상 객체 카드 점검 지시문 | 작성 |
| 51 | 2.8 | 서비스 구조 설명서 점검 지시문 | 작성 |

### Part 3·4 지시문 12개 (`kits/claude-code-prompts.md`)

| 교재 쪽 | 교재 절 | 지시문 | 자료실 위치 | 상태 |
|---|---|---|---|---|
| 65 | 3.5 | Stitch 테마별 시안 생성 지시문 | 같은 이름의 `##` 절 | 작성 |
| 70 | 3.6 | 서비스 구조를 넘기고 첫 프로토타입을 만드는 지시문 | 〃 | 작성 |
| 70 · 71 | 3.6 | 테마별 프로토타입 추가 생성 지시문 | 〃 | 작성 |
| 71 · 73 | 3.6 · 3.7 | 빈 상태·오류 등 상태 화면과 신뢰 요소 추가 지시문 | 〃 | 작성 |
| 78 · 79 | 4.2 | 여러 테마 버전 통합 지시문 | 〃 | 작성 |
| 81 | 4.3 | 외부 디자인 요소 보강 지시문 | 〃 | 작성 |
| 83 · 84 | 4.4 | 사용성 테스트 결과 반영 개선 지시문 | 〃 | 작성 |
| 86 | 4.5 | 컬러 샘플·파비콘·흑백 보기 리소스 추출 지시문 | 〃 | 작성 |
| 89 | 4.6 | 테마 일체감 통합 지시문 | 〃 | 작성 |
| 89 · 90 | 4.6 | 나만의 DESIGN.md 명세 추출 지시문 | 〃 | 작성 |
| 89 · 90 | 4.6 | 나만의 DESIGN.md 단독 문서 보강 지시문 | 〃 | 작성 |
| 91 · 99 | 4.7 · A-6 | 배포 전 개인정보 점검·정적 배포 준비 지시문 | 〃 | 작성 |

## 6. 자료실에만 있는 것 (교재가 가리키지 않음)

| 자료실 위치 | 내용 |
|---|---|
| `help/stuck-guide.md` · `help/other-coding-tools.md` · `help/windows-notes.md` | 도움말 3개 (막혔을 때 모음 · 다른 AI 코딩 도구 대응 · Windows 메모, grip T64) |
| `guides/day2-at-a-glance.md` | Day 2 한눈에 보기 — IA 3층 8키워드 개념 그림(`guides/images/day2-at-a-glance-1.png`, GPT 이미지 생성), 김도현·이서연 여정 단계 표(교재 36쪽) (2026-11-25) |
| `guides/layout-first-theme-guide.md` | 화면 배치 먼저 정하고 테마 입히기 — 교재 3.6절 67~70쪽 사이에 끼우는 Day 3 실습 흐름. Plan 모드 배치안 2~3개 → grip-it 결정(`context/screen-layout.md` · `context/grip-register.md`) → 배치 뼈대 `prototype-layout.html` → 지킬 것만 지키고 배치·요소 유형을 바꿔도 되는 테마 입히기. 교재 70쪽 1·3단계 지시문 대신. 예시는 가이드 안에 넣은 예시 서비스 구조 설명서(운동 관리 앱, 네 프로필 밖) (2026-11-26) |
| `guides/goal-polish-guide.md` | 프로토타입 결과물을 goal 프롬프트로 일괄 완성도 높이기 — Day 4 시작, 교재 4.2절 79쪽 앞에 끼우는 흐름. 원칙 문서를 먼저 자세히 넣는 이유와 AI 생산성 레시피(상세 지시 → `/goal` 핸즈오프 → `/goal-setting` → aztks 두 번 → grip-it), AI 슬롭 점검 목록 다섯 영역(참고: Scalr 「20 Signs a Website Was Made by AI」). `-before-goal` 복사본 → `context/ai-slop-checklist.md` · `context/polish-principles.md` → goal 프롬프트(`context/goals/`) → `/goal`(결과 `context/goal-report.md` · `context/goal-questions.md`) → grip-it(`context/grip-register.md`). 스킬은 `wild-mental/goal-setting-skill` · `wild-mental/aztks-skill`(aztks-agent 포함) (2026-11-27) |
| `guides/react-app-upgrade-guide.md` | 최종 프로토타입을 React 앱 프로토타입으로 고도화하기 — 수업 뒤 자료. PRD 최종본 틀 6부분(개요·목표 / 페르소나 / 사용자 스토리·AC / FR MoSCoW / NFR / 데이터·인터페이스)과 칸별 워크시트 출처, Claude Code PRD 초안 지시 → grip-it으로 빈칸 확정 → 프론트엔드 원칙 문서 `docs/frontend-principles.md`(토스 앱인토스 컨슈머 UX 가이드의 다크패턴 방지·UX 라이팅·그래픽·탭바·해상도, 토스 전용 브랜딩·SDK·그래픽 자산 제외 + Frontend Fundamentals 코드 품질 4기준과 전략·트레이드오프) → Plan 모드 계획(MUST만, WON'T 금지) → 작은 단위로 React · Vite · SQLite 앱 → 원칙 점검. 예시는 운동 관리 앱(네 프로필 밖) (2026-11-27) |
| `README.md` 「가이드 고침 이력」 | 수업 중 가이드를 고친 날짜와 한 줄 |
| `guides/images/` | 가이드 캡처 자리 12곳 (아직 비어 있음, grip T58) |
| `_context/` | 작성 규칙, 제작 계획, 교재 원문 발췌, 생성·동기화 스크립트, 이 매칭표 (사이트에는 안 보임) |

쪽 번호를 뽑은 방법: 출력본 PDF에서 각 이름을 찾아 쪽을 기록했습니다(`→ 온라인 가이드: 「이름」` 줄은 정확히 일치). 원고가 바뀌어 다시 출력하면 이 표의 쪽도 다시 맞춥니다.
