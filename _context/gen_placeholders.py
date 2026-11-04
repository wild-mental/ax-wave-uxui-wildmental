#!/usr/bin/env python3
"""자료실 저장소의 가이드 자리표시와 교재 원문 발췌를 만든다.

사용: python3 _context/gen_placeholders.py  (상위 프로젝트 docs/4-1/manuscript 가 있어야 함)
- _context/textbook-excerpts/*.md 는 항상 다시 만든다 (원고가 바뀌면 다시 실행).
- guides/*.md 는 자리표시 상태인 것만 다시 만들고, 본문을 쓴 가이드는 건드리지 않는다.
"""
import os, re, sys

HUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MS = os.path.join(os.path.dirname(HUB), 'docs', '4-1', 'manuscript')  # 상위 프로젝트의 인쇄본 원고
PLACEHOLDER_MARK = '준비 중인 가이드입니다'
# 이미 본문을 쓴 가이드(자리표시 표시가 없는 파일)는 덮어쓰지 않는다
WRITTEN = {f[:-3] for f in os.listdir(os.path.join(HUB, 'guides')) if f.endswith('.md')
           and PLACEHOLDER_MARK not in open(os.path.join(HUB, 'guides', f), encoding='utf-8').read()} if os.path.isdir(os.path.join(HUB, 'guides')) else set()

TYPE_DESC = {
 'T': ('도구 조작', '로그인부터 저장·공유까지 단계별 정지 화면 캡처, **Mac·Windows 화면을 나란히**(부록 A 머리말의 인쇄된 약속). 단계당 한 줄 설명, 막힘 FAQ 3~5개, 맨 아래 "화면 확인 날짜". 캡처 6~10장 × 2 OS.'),
 'W': ('워크시트 작성', '템플릿의 어느 칸에 쓰는지, 자주 하는 실수와 고친 예 3~5개, 체크리스트 항목별 확인 방법. 교재의 칸 설명·예시·지시문은 반복하지 않고 절을 가리킴. A4 1쪽 이내.'),
 'P': ('실습 따라 하기', '지시 → 결과 → 확인 → 수정 한 사이클을 단계별로. 단계마다 "이렇게 나오면 정상" 정지 화면 캡처, 결과가 다를 때 다시 지시하는 문장 예, 되돌리기(복사본) 방법. 캡처 6~12장, 막힘 대처 5개 이상.'),
 'F': ('진행', '진행 순서와 시간, 역할별로 말할 문장(대본), 기록 예 1개. 1화면.'),
 'R': ('참고 모음', '항목별 정지 화면 예 10장 내외, 항목마다 고르는 법·주의.'),
}
DUE = {'P0': '11/17(화) 사전 안내와 함께', 'P1': '쓰는 날 아침까지 표준 수준 (늦어도 11/21)', 'P2': '쓰는 날까지 최소 수준, 이후 보강'}

# slug, title, source-file, anchor regex for marker/section, location label, type, priority, toc list, fill list
G = [
 ('claude-start-guide','Claude 시작 가이드','appendix-a-tools.md','## A-1','부록 A-1 · Claude (웹·데스크톱 앱) · Day 1~4','T','P0',
  ['웹에서 로그인하기 / 데스크톱 앱에서 로그인하기 (Mac · Windows)','새 대화를 열고 교재 지시문 붙여 넣기 (`{ }` 바꾸기)','CSV·이미지 파일 첨부하기','결과를 워크시트로 옮기기 ("마크다운 표로 줘")','대화가 길어질 때 새 대화로 나누고 결론만 요약해 넘기기','넣지 말아야 할 정보 (실제 수치 범위는 스스로, 타인 정보 금지)','막혔을 때 (FAQ)','화면 확인 날짜'],
  ['교재 A-1 네 단계를 실제 화면으로 보여 주기','파일 첨부 위치와 CSV 첨부 시 주의(내 기록이면 범위 정하기)','결과를 워크시트 `worksheet.md` 표로 옮기는 요령 — 「GitHub 워크시트 저장소 가이드」와 연결','무료·유료 플랜 차이는 쓰지 않음(사전 안내 소관)']),
 ('github-worksheet-repo-guide','GitHub 워크시트 저장소 가이드','appendix-a-tools.md','## A-2','부록 A-2 · GitHub 워크시트 저장소 · Day 1~4','T','P0',
  ['GitHub 계정 만들기 (아이디 고르기: Day 4 배포 주소에 들어감)','New repository → 이름 `axyourbody-worksheet` → 공개 범위 Private → Create repository','자료실 저장소의 `worksheet-template/worksheet.md`에서 Copy raw file로 복사','내 저장소에서 creating a new file → 파일 이름 `worksheet.md` → 붙여 넣기 → Commit changes','강사 `wild-mental` 초대하기 (Settings → Collaborators → Add people)','`worksheet.md` 고치고 Commit changes로 저장하기','Preview로 표 확인, 체크리스트 `[x]` 표시','표 행 늘리기와 칸 쓰기 규칙 (`|` 금지, 쉼표나 " · "로 나누기)','이미지 올리고 연결하기 (저장소 맨 위, `![설명](파일이름.jpg)`)','Claude와 주고받기 (편집 화면 글 복사, "마크다운 표로 줘")','`my-own-DESIGN.md` 올리기와 Day 4 제출 링크 확인','막혔을 때 (Public으로 만들었을 때 Change visibility, 초대가 안 보일 때 등)','화면 확인 날짜'],
  ['교재 A-2 전체를 화면으로','자료실 저장소 주소: https://github.com/wild-mental/ax-wave-uxui-wildmental (인쇄된 주소), 문서 템플릿은 `worksheet-template/worksheet.md`','강사 GitHub 아이디 `wild-mental` (인쇄됨)','실수로 Public으로 만들었을 때 Settings → Danger Zone → Change visibility','저장 이력(Commits)으로 지난 내용 되돌려 보는 법 한 단락']),
 ('figma-template-guide','Figma 템플릿 열기·복제 가이드','appendix-a-tools.md','## A-3','부록 A-3 · Figma · Day 2~3','T','P0',
  ['Figma 무료 계정으로 로그인','템플릿 링크 열기 (원본은 보기 전용)','파일 이름 옆 메뉴 → Duplicate to your drafts (내 초안에 복제)','Drafts에 둘 것: 무료 계정 팀 프로젝트는 파일당 페이지 3개 제한','복제한 파일 이름 `axyourbody_이름_프로필ID`로 바꾸기','워크시트 페이지 세 개 찾기','칸 이름 상자·레인 띠 잠그기 (Lock)','「복사해서 쓰는 카드」 견본 복사해 늘리기 (Option/Alt 끌기)','강사만 볼 수 있게 공유하기 (초대 또는 링크 범위 제한)','공유 링크를 `worksheet.md` 맨 위 「Figma 파일 링크」에 붙이기','FigJam과 헷갈리지 않기 · 링크가 열리지 않을 때 SVG로 만드는 법','화면 확인 날짜'],
  ['교재 A-3 일곱 단계를 화면으로 (Mac · Windows)','템플릿 원본: https://www.figma.com/design/m1TCwCzHWB0oVgRuekyCeT/AX-YOUR-BODY-Figma-Template — 강사 계정 파일. 공유 설정 "링크가 있는 누구나 보기" 확인','Duplicate to your drafts 메뉴 위치 정지 화면 1장','예비: figma-template/ SVG 4장 (FigJam이 아니라 Design 파일에)']),
 ('stitch-start-guide','Stitch 시작 가이드','appendix-a-tools.md','## A-4','부록 A-4 · Google Stitch · Day 3','T','P0',
  ['Google 계정으로 stitch.withgoogle.com 로그인','새 프로젝트, 플랫폼은 웹(데스크톱)','지시문 킷의 「Stitch 테마별 시안 생성 지시문」 붙여 넣기','DESIGN.md 내용 붙여 넣기 또는 파일 첨부','변경 지시는 한 번에 한 가지','시안을 이미지로 내보내기 → Figma 시안 비교표에 붙이기','막혔을 때 (생성 한도, 첨부 실패 등)','화면 확인 날짜'],
  ['교재 A-4 다섯 단계를 화면으로','실습 흐름(테마별 비교)은 「Stitch 시안 만들기 가이드」가 맡음 — 여기서는 조작만']),
 ('claude-code-install-guide','Claude Code 데스크톱 앱 설치 (Mac판 · Windows판)','appendix-a-tools.md','## A-5','부록 A-5 · Claude Code 데스크톱 앱 · Day 3~4 (설치는 수업 전)','T','P0',
  ['Mac판: 내려받기 · 설치 · 처음 실행','Windows판: 내려받기 · 설치 · 처음 실행','Claude 계정으로 로그인, 코드 작업(Claude Code) 화면 들어가기','작업 폴더 `axyourbody-prototype` 만들기와 하위 폴더(context · design · data)','작업 폴더 열기','허락 요청 화면 읽는 법, 작업 폴더 밖 수정 거절','설치 확인 체크 (수업 전에 여기까지)','유료 플랜이 없을 때: 다른 회사의 AI 코딩 도구로 같은 일 하기 (폴더 열기, 파일 가리키기, 지시문은 그대로)','막혔을 때','화면 확인 날짜'],
  ['사전 안내문(`pre-course-notice.md`)과 같은 내용을 단계 화면으로','교재 앞부분 「쓰는 도구」: Claude Code 유료 플랜이 없으면 다른 회사의 AI 코딩 도구 허용 — `@` 파일 지정 등 사용법만 도구에 맞춤','작업 폴더 구조는 교재 A-5 그대로(SPEC §25 파일 이름)']),
 ('github-pages-deploy-guide','GitHub Pages 정적 배포 가이드','appendix-a-tools.md','## A-6','부록 A-6 · GitHub Pages 정적 배포 · Day 4','T','P1',
  ['준비: 배포 전 점검표 끝내기, `deploy` 폴더에 두 파일만','배포 전용 공개 저장소 만들기 (New repository → Public)','두 파일 올리기 (Upload files, 폴더째 올리지 않기)','Pages 켜기 (Settings → Pages → Deploy from a branch → main · / (root) → Save)','공개 주소 확인과 Actions 탭 초록 체크','휴대폰·시크릿 창으로 확인, 주소 기록','고쳐서 다시 올리기와 강력 새로 고침','404일 때','잘못 올렸을 때: 저장소 지우고 새로 만들기','워크시트 저장소(비공개)와 헷갈리지 않기','화면 확인 날짜'],
  ['교재 A-6 전체를 화면으로 (교재가 이미 단계를 다 씀 — 가이드는 화면과 FAQ)','무료 계정은 공개 저장소에서만 Pages','주소 형식 `https://아이디.github.io/저장소이름/`']),
 ('case-analysis-sheet-guide','사례 분석 시트 가이드','part-1.md','사례 분석 시트 가이드','1.2절 UX와 UI는 무엇이 다른가','W','P2',[],[]),
 ('task-pain-list-guide','과업·불편 목록 가이드','part-1.md','과업·불편 목록 가이드','1.4절(머리칸), 5절(본표)','W','P1',[],[]),
 ('persona-card-guide','페르소나 카드 가이드','part-1.md','페르소나 카드 가이드','1.6절','W','P2',[],[]),
 ('event-board-guide','이벤트 보드 사용 가이드','part-2.md','이벤트 보드 사용 가이드','2.2절, 2.4','W','P1',[],[]),
 ('object-card-guide','대상 객체 카드 작성 가이드','part-2.md','대상 객체 카드 작성 가이드','2.5절','W','P2',[],[]),
 ('term-matching-guide','용어 대조표 작성 가이드','part-2.md','용어 대조표 작성 가이드','2.6절','W','P2',[],[]),
 ('entry-point-guide','진입점 선택표 작성 가이드','part-2.md','진입점 선택표 작성 가이드','2.7절','W','P2',[],[]),
 ('service-structure-guide','서비스 구조 설명서 작성 가이드','part-2.md','서비스 구조 설명서 작성 가이드','2.8절','W','P1',[],[]),
 ('peer-review-guide','동료 리뷰 진행 가이드','part-2.md','동료 리뷰 진행 가이드','2.9절','F','P2',[],[]),
 ('screen-flow-guide','화면 흐름 순서표 작성 가이드','part-3.md','화면 흐름 순서표 작성 가이드','3.2절','W','P1',[],[]),
 ('design-shopping-guide','디자인 쇼핑처 둘러보기 가이드','part-3.md','디자인 쇼핑처 둘러보기 가이드','3.4절 디자인 쇼핑으로 DESIGN.md 2~3종 고르기 (본문 1곳 + 실습 안내 1곳)','R','P1',
  ['다섯 쇼핑처 한눈에 (무엇을 사나 · 주소 · 가져올 단위) — 교재 표를 가리키기만','UXSnaps: 가는 길 · 사례 고르는 법 · 메모해 올 것','21st.dev: 부품 찾기 · 저장 목록 · 지시문(프롬프트) 복사','getdesign.md: DESIGN.md 고르기 · 내려받기 · 파일 이름 바꿔 저장 (`DESIGN-테마이름.md`)','Logo System: 형태 아이디어만, 로고는 가져오지 않기','KRDS: 입력 양식·오류 안내 규칙 찾기, 필요한 규칙만 옮겨 적기','가져오면 안 되는 것 (실제 서비스 이름·로고·고유 그림)','부품·색만 가져올 때 "추가 규칙" 제목으로 덧붙이기','화면 확인 날짜'],
  ['사이트 화면 변동이 커서 교재가 이 가이드로 넘김 — 수업 전주에 반드시 재확인','교재 주소 표기: uxsnaps.com · 21st.dev · getdesign.md · logosystem.co · krds.go.kr','예시 테마 이름은 교재 김도현 예(bright-coaching · neat-basic · activity-record)만 언급 가능']),
 ('stitch-draft-guide','Stitch 시안 만들기 가이드','part-3.md','Stitch 시안 만들기 가이드','3.5절 Stitch로 테마별 시안 비교하기','P','P1',
  ['준비: 쇼핑 목록의 DESIGN.md 2~3개와 화면 설명 한 번 쓰기','첫 테마로 시안 뽑기 (데스크톱 1장 · 모바일 1장)','DESIGN.md만 바꿔 다음 테마 시안 뽑기','한 번에 한 가지씩, 테마당 2~3번까지만 고치기','흑백으로 바꿔 보기','시안 이미지를 Figma 비교표에 붙이고 세 기준(과업 수행 쉬움 · 정보 위계 · 프로필 적합성) 적기','결과가 이상할 때 다시 지시하는 문장','막혔을 때'],
  ['조작은 「Stitch 시작 가이드」 — 여기서는 비교 실습 흐름','"이렇게 나오면 정상" 예시는 교재 김도현 "오늘" 화면 설명 기준','DESIGN.md에 없는 색이 나올 때의 재지시 예']),
 ('claude-code-prototyping-guide','Claude Code 프로토타이핑 따라 하기','part-3.md','Claude Code 프로토타이핑 따라 하기','3.6절 Claude Code로 테마별 첫 프로토타입 만들기','P','P1',
  ['준비물 확인: 작업 폴더, `context/service-structure.md`, `context/screen-flow.md`, `design/DESIGN-<테마이름>.md` 2~3개, `data/` CSV 4개','1단계: 「서비스 구조를 넘기고 첫 프로토타입을 만드는 지시문」 보내기','브라우저로 열어 확인 목록 네 가지 점검','2단계: 한 번에 한 가지씩 수정 지시','3단계: 「테마별 프로토타입 추가 생성 지시문」으로 두 번째 테마','큰 변경 전 복사본 만들기 (`prototype-first-<테마이름>-before-states.html`)','4단계: 상태 화면(빈 · 오류 · 로딩 · 이상치)과 상태 미리 보기','버전 기록에 한 줄씩 쓰기','막혔을 때 (지시와 다른 결과 · 파일 망가짐 · 폴더 밖 수정 요청 · 사용량 한도)','다른 회사의 AI 코딩 도구를 쓸 때 달라지는 점'],
  ['**가장 중요한 가이드** — 11/21 리허설에서 처음부터 끝까지 직접 따라 하며 검증','단계마다 "이렇게 나오면 정상" 정지 화면(가상 데이터)','파일 이름은 SPEC §25 규칙 그대로','화면 녹화는 만들지 않음']),
 ('ai-trust-design-examples','AI 판단 화면 신뢰 설계 예시 모음','part-3.md','AI 판단 화면 신뢰 설계 예시 모음','3.7절 AI 판단 화면의 신뢰 설계','R','P2',
  ['다섯 요소 한눈에: 판단 · 근거 · 한계 · 전문가 확인 권장 · 사용자의 선택','판단: 결론 한 문장 — 좋은 예 / 고칠 예','근거: 기록의 종류·기간·값 — 좋은 예 / 고칠 예','한계: 빠진 기간·다른 측정 조건 — 좋은 예 / 고칠 예','전문가 확인 권장: 필요한 경우에만, 라벨·아이콘·테두리 — 좋은 예 / 고칠 예','사용자의 선택: "다른 안 보기" — 좋은 예 / 고칠 예','한 줄 → 펼치기 패턴 ("근거 자세히")','색 없이 구분하기'],
  ['예시 화면은 가상 데이터만 (참고 사례 AX MY BODY 캡처 재사용 가능, 교재 캡처와 같은 가상 프로필)','고칠 예는 관통 예제 밖 일반 사례로 써도 됨','다른 프로필의 완성 화면을 정답처럼 보여 주지 않음']),
 ('version-merge-guide','여러 버전 통합 가이드','part-4.md','여러 버전 통합 가이드','4.2절 여러 버전 조합하기','P','P1',
  ['사전 단계: 영역 지도만 받기 (조사만, 고치지 않기)','영역 지도와 줄 번호 읽는 법','장점 찾기 표로 영역별 가져올 버전 정하기','「여러 테마 버전 통합 지시문」 보내기 (뼈대 기준 파일 · 영역 순서 · 줄 번호)','옮기지 않은 콘텐츠 목록 처리하기 (답하기 전에는 고치지 않게)','색·글꼴이 섞여도 지금은 두기 (통일은 4.6)','버전 기록에 통합 프로토타입 행 추가','막혔을 때 (줄 번호가 어긋남 · 상태 화면이 빠짐 등)'],
  ['줄 번호는 예시일 뿐 — 각자 받은 영역 지도 번호를 쓰게 강조','버전이 두 개일 때의 지시 예']),
 ('design-skill-guide','디자인 스킬 가져오기 가이드','part-4.md','디자인 스킬 가져오기 가이드','4.3절 외부 디자인 요소로 보강하기','P','P1',
  ['보강할 영역 하나 고르기 (내 과업에 필요한데 첫 프로토타입에 없던 것)','출처 사이트에서 요소 고르고 지시문 복사, 출처 주소 기록','**스킬로 저장하기: Claude Code에서 저장 위치와 저장 확인 방법**','영역 하나에만 적용하고 바뀐 줄 범위 받기','버전 기록에 "통합 프로토타입 + 디자인 스킬" 행 추가','다음에 이름만 불러 다시 쓰기','다른 회사의 AI 코딩 도구일 때 (지시문을 파일로 저장해 두고 가리키기)','막혔을 때'],
  ['**교재 4.3이 스킬 저장 위치의 유일한 출처로 이 가이드를 지정함** — 반드시 최신 Claude Code 기준 저장 위치와 확인 방법을 화면으로','출처 예는 교재와 같은 21st.dev','원래 지시문의 상품·사진 문구를 내 내용으로 바꾸는 요령']),
 ('pair-usability-test-guide','짝 사용성 테스트 진행 가이드','part-4.md','짝 사용성 테스트 진행 가이드','4.4절 사용성 점검: 과업으로 시험하고 고치기','F','P1',
  ['60분 진행표 (시나리오 10 · 내 테스트 15 · 역할 바꾸기 15 · 휴리스틱 평가 10 · 우선순위 10)','과업 시나리오 쓰기 (찾기 과업 1개 이상)','테스트하는 나: 시작할 때 하는 말 · 도와주지 않는 말 · 끝맺는 말','써 보는 짝: 혼잣말로 생각 말하기 안내','초시계 기록, 3분 넘으면 중단 → 실패','휴리스틱 7가지 점검 순서 (교재의 쉬운 이름 그대로)','우선순위 정하기: 막힘 > 헤맴 > 거슬림, 찾기 과업 먼저','기록표 예 1개 (관통 예제 밖 일반 사례)'],
  ['역할 이름은 교재 그대로 "테스트하는 나 / 써 보는 짝"','휴리스틱 이름은 교재 4.4절의 쉬운 이름만']),
 ('favicon-color-sample-guide','파비콘·컬러 샘플 가이드','part-4.md','파비콘·컬러 샘플 가이드','4.5절 리소스 마무리: 파비콘·컬러 샘플·흑백 점검','P','P2',
  ['「컬러 샘플·파비콘·흑백 보기 리소스 추출 지시문」 보내기','`brand-resources.html` 읽는 법 (파일별 색 견본)','기본 색 하나 고르기','파비콘 고르기: 16px에서도 알아보이는가','흑백 보기에서 걸린 곳을 라벨·기호·무늬로 고치는 지시 예','고른 색 값과 파비콘을 버전 기록 "다음에 할 일"에 적기','`favicon.svg`로 저장해 두기 (배포 때 씀)'],
  ['결과 화면 정지 캡처 2~3장']),
 ('my-own-design-md-guide','나만의 DESIGN.md 만들기 가이드','part-4.md','나만의 DESIGN.md 만들기 가이드','4.6절 나만의 DESIGN.md 만들기','P','P1',
  ['세 지시의 순서: 테마 일체감 통합 → 명세 추출 → 단독 문서 보강','다섯 가지 내용이 다 들어갔는지 확인','단독 문서인지 확인 (다른 파일·스킬·작업 이력 언급 찾기)','재현 시험: 새 대화에 파일 하나만 넘겨 새 화면 만들기','(가능하면) Stitch로도 재현해 보기','점검표 여섯 항목 확인 방법','샘플 `DESIGN-axyourbody-sample.md`와 비교하는 법','`my-own-DESIGN.md`와 재현 시험 화면을 워크시트 저장소에 올리기'],
  ['샘플 DESIGN.md는 자료실 `kits/`에 있음','재현 시험이 "부분"일 때 고치는 예']),
 ('pre-deploy-check-guide','배포 전 점검과 정적 배포 가이드','part-4.md','배포 전 점검과 정적 배포 가이드','4.7절 정적 배포: 공개하기 전에 지우기','P','P1',
  ['「배포 전 개인정보 점검·정적 배포 준비 지시문」: 점검만 먼저','점검 결과 표 읽기 (실명 · 연락처 · 실제 수치 · 주석 · 숨긴 요소 · 링크)','확인 후 "고쳐" 지시, `deploy` 폴더 만들기','HTML 주석과 숨긴 요소를 직접 확인하는 법 (페이지 소스 보기: Mac · Windows 단축키)','배포 전 점검표 일곱 항목 채우기','올리기: 「GitHub Pages 정적 배포 가이드」로','실제 주소에서 다시 확인 (휴대폰 · 시크릿 창) → 배포 후 재확인 행','공개 저장소는 이력까지 공개 — 잘못 올렸을 때'],
  ['점검 흐름 담당. 올리는 클릭은 「GitHub Pages 정적 배포 가이드」로 넘김']),
 ('presentation-review-guide','발표·동료 리뷰 진행 가이드','part-4.md','발표·동료 리뷰 진행 가이드','4.8절 발표·동료 리뷰와 4일 회고','F','P2',
  ['다섯 장면 5분 구성 (교재 표를 가리키기)','발표 전 10분 준비: 열어 둘 화면 · 워크시트 · 배포 링크','"배포 링크로 직접 보여 주기": 현장에서 핵심 과업을 눌러 보이는 순서','동료 리뷰: 비교 관점 넷 중 둘 고르기, 좋았던 점 · 질문 · 제안 대본','받은 의견을 버전 기록 "다음에 할 일"에 적기','4일 회고 칸 쓰기','제출 확인: 워크시트 저장소 링크 · Figma 링크 · 배포 링크 · `my-own-DESIGN.md`'],
  ['녹화 영상 발표가 아님 — 현장 시연','제출 확인 체크리스트를 이 가이드 끝에']),
]


def excerpt(src, anchor):
    lines = open(f'{MS}/{src}', encoding='utf-8').read().split('\n')
    out = []
    if anchor.startswith('## '):
        s = next(i for i, l in enumerate(lines) if l.startswith(anchor))
        e = next((i for i in range(s + 1, len(lines)) if lines[i].startswith('## ')), len(lines))
        return '\n'.join(lines[s:e]).strip()
    idxs = [i for i, l in enumerate(lines) if f'「{anchor}」' in l]
    for n in idxs:
        h = max(i for i in range(n + 1) if lines[i].startswith('## '))
        s = max((i for i in range(n + 1) if '[실습 안내]' in lines[i]), default=n - 8)
        body_marker = s < n - 45 or s < h
        if body_marker:
            s = max(h, n - 8)
        e = n + 1
        if body_marker:
            e = next((i for i in range(n + 1, len(lines)) if lines[i].startswith('#')), len(lines))
        while e < len(lines) and lines[e].startswith('> →'):
            e += 1
        out.append(f'### 교재 위치: {src} {s + 1}~{e}행 (절: {lines[h][3:]})\n\n' + '\n'.join(lines[s:e]).strip())
    return '\n\n---\n\n'.join(out)


os.makedirs(f'{HUB}/guides', exist_ok=True)
os.makedirs(f'{HUB}/_context/textbook-excerpts', exist_ok=True)
for slug, title, src, anchor, loc, typ, pri, toc, fill in G:
    ex = excerpt(src, anchor)
    assert ex, slug
    with open(f'{HUB}/_context/textbook-excerpts/{slug}.md', 'w', encoding='utf-8') as f:
        f.write(f'# 교재 원문 발췌 — 「{title}」\n\n> 인쇄본 원고(`docs/4-1/manuscript/{src}`)에서 이 가이드를 가리키는 부분을 그대로 옮겼습니다. 생성: `_context/gen_placeholders.py` (2026-11-04 원고 기준). 원고가 바뀌면 다시 뽑습니다.\n\n{ex}\n')
    if slug in WRITTEN:
        continue
    tname, tlevel = TYPE_DESC[typ]
    body = [f'# {title}', '',
            f'> **준비 중인 가이드입니다.** 수업 전에 채워집니다. 그동안은 교재 {loc.split(" · ")[0]} {loc.split(" · ")[1] if " · " in loc else ""}와 부록 A를 보세요.'.replace('  ', ' '), '',
            '<!-- 아래는 작성자용 자리표시입니다. 가이드를 다 쓰면 이 줄부터 「작성 계획」 끝까지 지우고 본문으로 바꿉니다. -->', '',
            '## 목차 초안', '']
    body += [f'{i}. {t}' for i, t in enumerate(toc, 1)]
    body += ['', '## 작성 계획', '',
             '| 항목 | 내용 |', '|---|---|',
             f'| 교재 위치 | {loc} |',
             f'| 교재 원문 | `_context/textbook-excerpts/{slug}.md` |',
             f'| 유형 | {typ} {tname} |',
             f'| 우선순위 · 마감 | {pri} · {DUE[pri]} |',
             f'| 목표 수준 (표준) | {tlevel} |',
             '', '### 이 가이드가 채울 것 (교재에 없는 것)', '']
    body += [f'- {x}' for x in fill]
    body += ['', '### 지킬 규칙', '',
             '- `_context/RULES.md` 전부. 특히 학생에게 하는 말만 · 정답 비공개 · 실제 개인 데이터 금지 · 코드 이름 금지 · 인쇄본과 같은 이름 · 교재 내용 반복 금지.',
             '- 제목(맨 위 `#` 줄)은 인쇄본과 글자 하나까지 같아야 합니다. 바꾸지 않습니다.',
             '', '### 완료 기준', '',
             '- [ ] 최소 수준: 제목 · 교재 절 번호 · 쓰는 곳 · 핵심 3줄 · 막혔을 때 볼 곳',
             '- [ ] 표준 수준: 위 「목표 수준」의 내용',
             '- [ ] 「준비 중」 안내와 이 작성 계획을 지웠다',
             '- [ ] `_context/RULES.md`의 점검 명령을 돌려 걸린 곳이 없다',
             '- [ ] `_context/ONLINE_MATERIALS_PLAN.md` §3-2 표의 상태를 「작성」으로 바꿨다', '']
    if typ in ('T',) or slug == 'design-shopping-guide':
        body.insert(-1, '- [ ] 맨 아래에 "화면 확인 날짜: YYYY-MM-DD"를 적었다')
    with open(f'{HUB}/guides/{slug}.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(body))

# registry for README generation
import json
json.dump([{'slug': g[0], 'title': g[1], 'loc': g[4], 'type': g[5], 'pri': g[6]} for g in G],
          open(f'{HUB}/_context/guides.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('guides', len(G), 'placeholders', len(G) - len(WRITTEN & {g[0] for g in G}))
