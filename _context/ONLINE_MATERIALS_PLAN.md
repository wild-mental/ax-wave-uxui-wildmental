# 4-1 온라인 자료 제작 계획 (인쇄본 출력 후 작업용)

> 처음 작성 2026-11-04, 같은 날 강사 결정 반영으로 개정.
> 기준: 인쇄 제출본(컬러판·흑백판)의 원고 `docs/4-1/manuscript/*.md`.
> 작업 저장소: `ax-wave-uxui-wildmental/` (이 프로젝트 루트의 하위 Git 저장소 = GitHub 공개 저장소 `wild-mental/ax-wave-uxui-wildmental`, 2026-11-04 게시. Pages 설정은 강사가 직접). 이 문서의 사본이 그 저장소의 `_context/ONLINE_MATERIALS_PLAN.md`에 있습니다.
> 가이드 이름 재추출: `grep -rn "온라인 가이드" docs/4-1/manuscript` (TEXTBOOK_SPEC §26)

---

## 1. 결론: 먼저 출력해도 되는가

**됩니다.** 출력 전 필수·권장 보완 4건과 아래 강사 결정을 원고에 모두 반영했습니다(2026-11-04).

### 강사 결정 (TEXTBOOK_SPEC §32)

| 항목 | 결정 |
|---|---|
| 온라인 자료실 | 공개 저장소 `wild-mental/ax-wave-uxui-wildmental` 하나에서 경로로 나눠 제공 + GitHub Pages. 주소와 강사 GitHub 아이디 `wild-mental`을 **부록 A 첫 쪽에 인쇄** |
| 문서 템플릿 | 같은 저장소의 `worksheet-template/worksheet.md`. 학생은 비공개 저장소 `axyourbody-worksheet`를 만들고 Copy raw file로 옮겨 쓴 뒤 `wild-mental`을 초대 |
| Figma 템플릿 | 같은 저장소의 `figma-template/` SVG 4장을 학생이 Figma에 끌어다 놓아 만듦 |
| 워크시트 제출 | 워크시트 저장소 링크(비공개·강사 초대) · Figma 링크(강사만 열람) · 배포 링크 · `my-own-DESIGN.md`(워크시트 저장소에 올림) |
| 정적 배포 | GitHub Pages로 일원화(Netlify 삭제). 배포 전용 공개 저장소에 `index.html`·`favicon.svg`만 |
| Claude Code 유료 플랜 | 없으면 다른 회사의 AI 코딩 도구를 써도 됨(교재 앞부분 「쓰는 도구」에 한 번 안내) |
| 화면 녹화 | 만들지 않음. 교재에 녹화를 전제한 곳 없음(발표 3장면은 "배포 링크로 직접 보여 주기"로 표현 정리) |

### 인쇄로 고정되는 약속

| 고정되는 것 | 온라인 쪽에서 지킬 일 |
|---|---|
| 인쇄된 주소·아이디: 자료실 `https://wild-mental.github.io/ax-wave-uxui-wildmental/` · 자료실 저장소 `https://github.com/wild-mental/ax-wave-uxui-wildmental` · 강사 GitHub 아이디 `wild-mental` (부록 A 첫 쪽, A-2) | 계정·저장소·폴더 이름(`worksheet-template`, `figma-template`)을 **바꾸지 않습니다**. 바꾸면 인쇄본 안내가 끊깁니다 |
| 가이드 이름 27개 (교재 30곳) | 가이드 제목을 글자 하나까지 똑같이 씁니다 (§3 표) |
| 워크시트 14종 풀네임, 칸 이름·순서, Figma 페이지 3개 이름 | `worksheet-template/worksheet.md`와 `figma-template/README.md` 그대로 |
| 지시문 이름 12개 | 킷은 `kits/claude-code-prompts.md` 제목 그대로 |
| 파일·폴더 이름 (SPEC §25) | 가이드 예시의 파일 이름도 같은 규칙 |
| 부록 A 번호: A-1 Claude · A-2 GitHub 워크시트 저장소 · A-3 Figma · A-4 Google Stitch · A-5 Claude Code · A-6 GitHub Pages | 가이드에서 부록을 가리킬 때 이 번호 |
| "도구 조작 가이드(A-1~A-6)에는 Mac과 Windows 화면이 나란히 있습니다." | 유형 T 가이드 6개는 두 OS 화면을 나란히 |
| "사전 안내" (교재 3곳) | 사전 안내문을 11/17까지 배포 (GitHub 계정 만들기 포함) |

---

## 2. 출력 전 보완 (모두 반영함)

| # | 위치 | 반영 내용 |
|---|---|---|
| ① | Part 4 4.3 | "(저장 위치는 부록 A-4)" 끊긴 참조 → "(저장 위치와 확인 방법은 온라인 가이드 「디자인 스킬 가져오기 가이드」)" |
| ② | 「이 교재를 쓰는 법」 4번 | 자료실 한 곳 안내 + "주소는 부록 A 첫 쪽" |
| ③ | 부록 A-2 신설 | 문서 템플릿 사본 = GitHub 비공개 저장소 만들기·강사 초대·쓰기·이미지 올리기 |
| ④ | 부록 A 머리말 | Mac·Windows 약속을 "도구 조작 가이드(A-1~A-6)"로 한정 |
| 추가 | 부록 A-6 | GitHub Pages 정적 배포 설정 전체(저장소 만들기 → 올리기 → Pages 켜기 → 확인 → 다시 올리기 → 404 대처 → 공개 저장소 주의) |
| 추가 | 원고 전반 | 굵게 표시가 조사 앞에서 풀리던 9곳 수정 |

---

## 3. 만들어야 할 것 전체

### 3-1. 가이드가 아닌 배포물

| # | 배포물 | 상태 | 만들 수준 | 마감 |
|---|---|---|---|---|
| ① | 사전 안내문 (Mac판 · Windows판) | 자리표시 (`pre-course-notice.md`) | 수업 전에 끝낼 일: GitHub 계정(아이디가 배포 주소에 들어감)과 워크시트 저장소(강사 `wild-mental` 초대) · Claude 계정 · Claude Code 데스크톱 앱 설치·로그인(유료 플랜이 없으면 다른 AI 코딩 도구) · Figma 무료 계정 · Google 계정(Stitch) · 자료실 주소 · 설치 확인 방법 | **11/17(화)** |
| ② | 온라인 자료실 (허브) | 뼈대 완료 (`README.md` = 첫 화면) | Day별 가이드 목록 + 배포물 링크. GitHub Pages로 공개 | 11/17 |
| ③ | 문서 템플릿 | **완료** (`worksheet-template/`) | `worksheet.md` + 시작 안내 `README.md`. 학생은 github.com 화면에서 복사 | 완료 |
| ④ | Figma 템플릿 SVG | **완료** (`figma-template/*.svg` 4장 + README) | 학생이 Figma에 끌어다 놓아 만드는 SVG. Figma에서 글자가 편집 가능하게 들어오는지 수업 전 확인 | 11/17 확인 |
| ⑤ | 데이터셋 | 원본 복사 완료 (`datasets/`) | 프로필별 폴더 4개 × CSV 4개. 필요하면 프로필별 압축 파일 추가 | 11/21 |
| ⑥ | 지시문 킷 | 원본 복사 완료 (`kits/claude-code-prompts.md`) | 지시문 12개. 복사하기 쉽게 코드 블록 유지 | 11/21 |
| ⑦ | 샘플 DESIGN.md | 원본 복사 완료 (`kits/DESIGN-axyourbody-sample.md`) | 그대로 | 11/21 |

### 3-2. 온라인 가이드 27개

유형: **T** 도구 조작 · **W** 워크시트 작성 · **P** 실습 따라 하기 · **F** 진행 · **R** 참고 모음 (§4).
우선: **P0** 사전 안내와 함께(11/17) · **P1** 그날 아침까지 표준 수준 · **P2** 그날까지 최소 수준, 이후 보강.
상태: 작성(표준 수준 초고 완료) · 자리표시(목차 초안·작성 계획만).

| # | 가이드 이름 (인쇄본 그대로) | 파일 (`guides/`) | 쓰는 곳 | 유형 | 우선 | 상태 |
|---|---|---|---|---|---|---|
| 1 | Claude 시작 가이드 | `claude-start-guide.md` | 부록 A-1 · Day 1~4 | T | P0 | 자리표시 |
| 2 | GitHub 워크시트 저장소 가이드 | `github-worksheet-repo-guide.md` | 부록 A-2 · Day 1~4 | T | P0 | 자리표시 |
| 3 | Figma 템플릿 만들기 가이드 | `figma-template-guide.md` | 부록 A-3 · Day 2~3 | T | P0 | 자리표시 |
| 4 | Stitch 시작 가이드 | `stitch-start-guide.md` | 부록 A-4 · Day 3 | T | P0 | 자리표시 |
| 5 | Claude Code 데스크톱 앱 설치 (Mac판 · Windows판) | `claude-code-install-guide.md` | 부록 A-5 · Day 3~4 | T | P0 | 자리표시 |
| 6 | GitHub Pages 정적 배포 가이드 | `github-pages-deploy-guide.md` | 부록 A-6 · Day 4 | T | P1 | 자리표시 |
| 7 | 사례 분석 시트 가이드 | `case-analysis-sheet-guide.md` | Part 1 · 2절 | W | P2 | 작성 |
| 8 | 과업·불편 목록 가이드 | `task-pain-list-guide.md` | Part 1 · 4절, 5절 | W | P1 | 작성 |
| 9 | 페르소나 카드 가이드 | `persona-card-guide.md` | Part 1 · 6절 | W | P2 | 작성 |
| 10 | 이벤트 보드 사용 가이드 | `event-board-guide.md` | Part 2 · 2-2, 2-4 | W+T | P1 | 작성 |
| 11 | 대상 객체 카드 작성 가이드 | `object-card-guide.md` | Part 2 · 2-5 | W | P2 | 작성 |
| 12 | 용어 대조표 작성 가이드 | `term-matching-guide.md` | Part 2 · 2-6 | W | P2 | 작성 |
| 13 | 진입점 선택표 작성 가이드 | `entry-point-guide.md` | Part 2 · 2-7 | W | P2 | 작성 |
| 14 | 서비스 구조 설명서 작성 가이드 | `service-structure-guide.md` | Part 2 · 2-8 | W | P1 | 작성 |
| 15 | 동료 리뷰 진행 가이드 | `peer-review-guide.md` | Part 2 · 2-9 | F | P2 | 작성 |
| 16 | 화면 흐름 순서표 작성 가이드 | `screen-flow-guide.md` | Part 3 · 3.2 | W+T | P1 | 작성 |
| 17 | 디자인 쇼핑처 둘러보기 가이드 | `design-shopping-guide.md` | Part 3 · 3.4 (2곳) | R | P1 | 자리표시 |
| 18 | Stitch 시안 만들기 가이드 | `stitch-draft-guide.md` | Part 3 · 3.5 | P | P1 | 자리표시 |
| 19 | Claude Code 프로토타이핑 따라 하기 | `claude-code-prototyping-guide.md` | Part 3 · 3.6 | P | **P1 · 가장 중요** | 자리표시 |
| 20 | AI 판단 화면 신뢰 설계 예시 모음 | `ai-trust-design-examples.md` | Part 3 · 3.7 | R | P2 | 자리표시 |
| 21 | 여러 버전 통합 가이드 | `version-merge-guide.md` | Part 4 · 4.2 | P | P1 | 자리표시 |
| 22 | 디자인 스킬 가져오기 가이드 | `design-skill-guide.md` | Part 4 · 4.3 | P | P1 | 자리표시 |
| 23 | 짝 사용성 테스트 진행 가이드 | `pair-usability-test-guide.md` | Part 4 · 4.4 | F | P1 | 자리표시 |
| 24 | 파비콘·컬러 샘플 가이드 | `favicon-color-sample-guide.md` | Part 4 · 4.5 | P | P2 | 자리표시 |
| 25 | 나만의 DESIGN.md 만들기 가이드 | `my-own-design-md-guide.md` | Part 4 · 4.6 | P | P1 | 자리표시 |
| 26 | 배포 전 점검과 정적 배포 가이드 | `pre-deploy-check-guide.md` | Part 4 · 4.7 | P | P1 | 자리표시 |
| 27 | 발표·동료 리뷰 진행 가이드 | `presentation-review-guide.md` | Part 4 · 4.8 | F | P2 | 자리표시 |

각 자리표시 파일에 목차 초안, 채울 내용, 교재 원문 위치가 들어 있습니다. 교재에서 그 가이드를 가리키는 [실습 안내] 원문은 `_context/textbook-excerpts/<같은 파일 이름>`에 있습니다.

이름이 비슷한 가이드는 이름을 합치지 않고 역할을 나눕니다.
- 「Stitch 시작 가이드」(조작) ↔ 「Stitch 시안 만들기 가이드」(실습 흐름)
- 「Claude Code 데스크톱 앱 설치」(조작) ↔ 「Claude Code 프로토타이핑 따라 하기」(실습 흐름)
- 「GitHub Pages 정적 배포 가이드」(올리는 조작) ↔ 「배포 전 점검과 정적 배포 가이드」(점검 흐름, 마지막에 앞 가이드로 연결)
- 「동료 리뷰 진행 가이드」(Day 2, 용어 리뷰) ↔ 「발표·동료 리뷰 진행 가이드」(Day 4, 발표)
- 「GitHub 워크시트 저장소 가이드」(비공개, 워크시트) ↔ 「GitHub Pages 정적 배포 가이드」(공개, 배포)

---

## 4. 유형별 수준 기준

모든 가이드는 수업일까지 **최소 수준**을 갖춥니다. 화면 녹화는 만들지 않습니다.

| 수준 | 기준 |
|---|---|
| 최소 | 인쇄본과 같은 제목 · 교재 절 번호 · 템플릿에서 쓰는 위치 · 핵심 3줄 · 막혔을 때 볼 곳 |
| 표준 | 최소 + 아래 유형별 내용 |

| 유형 | 해당 | 표준 수준의 내용 | 분량 |
|---|---|---|---|
| **T** 도구 조작 | 1~6 | 로그인부터 저장·공유까지 단계별 정지 화면 캡처. **Mac·Windows 나란히**. 단계당 한 줄, 막힘 FAQ 3~5개, 화면 확인 날짜 | 캡처 6~10장 × 2 OS |
| **W** 워크시트 작성 | 7~14, 16 | 템플릿의 어느 칸에 쓰는지, 자주 하는 실수와 고친 예 3~5개, 체크리스트 항목별 확인 방법. 교재의 칸 설명·예시·지시문은 반복하지 않고 절을 가리킴 | A4 1쪽 이내 |
| **P** 실습 따라 하기 | 18·19·21·22·24·25·26 | 지시 → 결과 → 확인 → 수정 한 사이클을 단계별로. "이렇게 나오면 정상" 캡처, 결과가 다를 때 다시 지시하는 문장, 되돌리기(복사본) | 캡처 6~12장, 막힘 대처 5개 이상 |
| **F** 진행 | 15·23·27 | 진행 순서와 시간, 역할별 대본, 기록 예 1개 | 1화면 |
| **R** 참고 모음 | 17·20 | 17: 다섯 곳 × (가는 길·고르는 법·내려받기·주의) / 20: 요소 다섯 개 × (좋은 예·고칠 예) | 각 화면 예 10장 내외 |

---

## 5. 모든 온라인 자료에 적용할 규칙

1. **학생에게 하는 말만** 씁니다. 설계 의도·평가·운영 시간·정답은 강사 가이드(`docs/4-1/instructor-guide.md`, 비공개)에만 둡니다. "여러분" + 합니다체.
2. **정답을 싣지 않습니다**(T32). 데이터셋의 빠진 날·튀는 날 목록, 네 프로필 과업 단서 표, 다른 프로필의 완성 예시는 넣지 않습니다. 데이터셋 CSV를 열어 결과를 뽑아 적지 않습니다. 예시는 교재의 주 예제를 가리키거나 관통 예제 밖(배달앱·도서관 앱 등)에서 씁니다.
3. **실제 개인 데이터를 쓰지 않습니다.** 캡처와 예시는 가상 프로필 데이터만.
4. **코드 이름을 쓰지 않습니다**(T41). W01·K02·v1-b·H1·T1 대신 풀네임과 지시문 이름.
5. **이름을 인쇄본과 똑같이** 씁니다(가이드 제목, 워크시트·지시문·파일 이름).
6. 도구 화면은 바뀝니다. T 유형과 17번은 **화면 확인 날짜**를 적고 수업 전주에 다시 확인합니다.
7. 외부 사이트의 이름·로고·고유 그림을 가져오지 않습니다.
8. 같은 말은 한 곳에만 둡니다. 교재에 있는 칸 설명·예시·지시문 전문은 반복하지 않고 절 번호로 가리킵니다.
9. 표준 마크다운만 씁니다(GitHub 표·체크리스트 포함). 자료실 저장소는 **공개**이므로 강사용 내용은 `_context/`에도 넣지 않습니다.

---

## 6. 일정 (수업 11/24 기준 역산)

| 날짜 | 할 일 |
|---|---|
| 11/04(수) | 원고 반영 → PDF 재빌드 → 출력 제출 · 자료실 저장소 게시(가이드 27개: 초고 10 · 자리표시 17, 문서 템플릿, Figma 템플릿 안내) |
| 11/04(수) 이후 | 강사가 GitHub Pages 켜기(Settings → Pages → main · / (root)) → 인쇄된 자료실 주소가 열리는지 확인 |
| ~11/17(화) | **사전 안내문 배포** · 도구 조작 가이드 6개 표준 수준 |
| ~11/21(금) | 27개 전부 최소 수준 이상 · P1 표준 수준 · 리허설로 19번 따라 하기 직접 검증 |
| 11/23(월) | 도구·사이트 화면 재확인(1~6, 17), 외부 주소 재확인 |
| 11/24~27 | 수업 중 막힌 곳을 해당 가이드에 바로 보강 |

---

## 7. 남은 확인 사항

| # | 확인할 것 | 메모 |
|---|---|---|
| 1 | GitHub Pages 켜기 | 강사가 직접. 켠 뒤 인쇄된 주소와 `figma-template/`, `datasets/` 링크가 열리는지 확인 |
| 2 | 학생 수만큼의 초대 수락 | 강사 계정 `wild-mental` 알림에서 수락. 30명 내외면 첫날 쉬는 시간에 일괄 처리 |

---

## 8. 원천 파일

| 배포물 | 원천 (이 프로젝트) | 자료실 저장소 안 |
|---|---|---|
| 문서 템플릿 | — | `worksheet-template/` (원본) |
| Figma 템플릿 안내 | — (`docs/4-1/templates/figma-template-spec.md`는 안내 파일로 옮김) | `figma-template/README.md` (원본) |
| 지시문 킷 · 샘플 DESIGN.md | `docs/4-1/kits/` | `kits/` (사본) |
| 데이터셋 | `docs/4-1/dataset/` | `datasets/` (사본) |
| 사본 맞추기 | — | `_context/sync-from-textbook.sh` |
| 정답·운영 정보 (넣지 않을 것) | `docs/4-1/instructor-guide.md` | 없음 (공개 저장소에 넣지 않음) |
