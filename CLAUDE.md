# ax-wave-uxui-wildmental — 작업 안내

4-1 「웹서비스 UX/UI 기획」 교재(인쇄본)와 함께 쓰는 **온라인 자료실** 저장소입니다. 이 파일은 사이트에 나오지 않습니다(`_config.yml` exclude). 이 저장소에서 일을 시작할 때 이 파일과 `_context/RULES.md`, `_context/ONLINE_MATERIALS_PLAN.md`를 먼저 읽습니다.

## 배경 (2026-11-04)

- 교재는 이 자료실보다 **먼저 인쇄**되었습니다. 교재는 가이드를 이름으로만 가리키고(`→ 온라인 가이드: 「이름」` 30곳, 27개), 부록 A 첫 쪽에 아래를 인쇄했습니다. 그래서 **계정 이름, 저장소 이름, 폴더 이름(`worksheet-template`, `figma-template`), 가이드 제목은 바꿀 수 없습니다.**
  - 자료실: `https://wild-mental.github.io/ax-wave-uxui-wildmental/` (이 저장소의 GitHub Pages)
  - 자료실 저장소: `https://github.com/wild-mental/ax-wave-uxui-wildmental` (문서 템플릿 `worksheet-template/worksheet.md`)
  - 강사 GitHub 아이디: `wild-mental` (학생이 비공개 워크시트 저장소에 초대)
- 강사 결정 (상위 프로젝트 `docs/4-1/TEXTBOOK_SPEC.md` §32):
  - 자료실·문서 템플릿·Figma 템플릿 안내는 **이 저장소 하나**에서 경로로 나눠 제공합니다.
  - 학생은 비공개 저장소 `axyourbody-worksheet`를 새로 만들고, `worksheet-template/worksheet.md`를 Copy raw file로 복사해 붙여 넣은 뒤 `wild-mental`을 초대합니다. 이미지는 그 저장소 맨 위에 올립니다.
  - Figma 템플릿은 강사 계정의 Figma 파일(https://www.figma.com/design/m1TCwCzHWB0oVgRuekyCeT/AX-MY-BODY-Figma-Template)을 학생이 Duplicate to your drafts로 복제해서 씁니다. `figma-template/` SVG는 예비입니다.
  - 정적 배포는 GitHub Pages로 일원화(학생의 배포 전용 공개 저장소). Claude Code 유료 플랜이 없으면 다른 회사의 AI 코딩 도구 허용. 화면 녹화는 만들지 않습니다.
- 수업: 2026-11-24(화) ~ 27(금), Day 1~4 = 교재 Part 1~4.

## 폴더

| 경로 | 무엇 | 사이트에 공개 |
|---|---|---|
| `README.md` | 자료실 첫 화면 (Day별 가이드 목록) | 예 |
| `guides/` | 온라인 가이드 27개. 10개는 표준 수준 초고, 17개는 자리표시(목차 초안 + 작성 계획). 캡처는 `guides/images/` | 예 |
| `pre-course-notice.md` | 사전 안내 (자리표시, 11/17 마감) | 예 |
| `figma-template/README.md` | Figma 템플릿 안내 (기준 문서: 페이지·레인·칸·체크리스트) | 예 |
| `datasets/` | 프로필 4명 × CSV 4개 (가상 데이터) + 열 이름 안내 | 예 |
| `kits/` | 지시문 킷, 샘플 DESIGN.md | 예 |
| `worksheet-template/` | 문서 템플릿 (기준 문서). 학생은 github.com 화면에서 열어 복사 | 아니오 (저장소 화면에서 봄) |
| `_context/` | 작업 맥락: 규칙, 제작 계획, 교재 원문 발췌, 생성·동기화 스크립트 | 아니오 (저장소에는 공개) |

## 가이드 하나를 쓰는 순서

1. `guides/<파일>.md`의 「목차 초안」과 「작성 계획」을 읽습니다.
2. `_context/textbook-excerpts/<같은 파일 이름>`에서 교재가 그 가이드를 가리키는 원문을 읽습니다. 교재에 있는 내용은 되풀이하지 않습니다.
3. 칸·체크리스트는 `worksheet-template/worksheet.md`, Figma 페이지는 `figma-template/README.md`를 따릅니다.
4. 이미 쓴 가이드(예: `guides/event-board-guide.md`)의 구성과 말투를 참고합니다.
5. 본문을 쓰고, 「준비 중」 안내와 작성자용 주석·작성 계획을 지웁니다. 제목 줄은 그대로 둡니다.
6. `_context/RULES.md` §8 점검 명령을 돌립니다.
7. `_context/ONLINE_MATERIALS_PLAN.md` §3-2의 상태를 「작성」으로 바꿉니다. (상위 프로젝트 `docs/4-1/ONLINE_MATERIALS_PLAN.md`도 같이 고칩니다.)

## 절대 하지 않을 것

- 강사용 내용(평가, 데이터셋 정답, 운영 시간표, 설계 의도)을 넣지 않습니다. 이 저장소는 공개입니다.
- 실제 개인 데이터(신체·검진 수치, 증상, 대화)를 넣지 않습니다.
- 인쇄된 이름·주소·폴더 이름을 바꾸지 않습니다.
- 강사의 확인 없이 저장소 설정을 바꾸지 않습니다.

## 교재가 바뀌었을 때

상위 프로젝트(`../docs/4-1/`)가 원고·킷·데이터셋의 원본입니다. 바뀌면 저장소 맨 위에서 `sh _context/sync-from-textbook.sh`를 실행해 사본과 교재 원문 발췌를 다시 만듭니다. 자리표시 상태의 가이드만 다시 만들어지고, 본문을 쓴 가이드는 그대로입니다. 문서 템플릿과 Figma 템플릿 안내는 이 저장소가 원본입니다.

## 공개 상태

- 2026-11-04 공개 저장소 `wild-mental/ax-wave-uxui-wildmental`로 올림(main).
- GitHub Pages 설정은 강사가 직접: Settings → Pages → Deploy from a branch → `main` · `/ (root)` → Save. 인쇄된 자료실 주소가 열리는지 확인합니다.
