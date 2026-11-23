# 막혔을 때 모음

수업 중에 막혔을 때 도구별로 빨리 찾아보는 페이지입니다. 단계별 방법은 항목 끝의 가이드에 다 있습니다.

## 먼저 해 볼 것

1. **새로 고침합니다.** 고쳤는데 화면이 그대로면 `Cmd+R`(Windows `F5`)을 누릅니다. 그래도 같으면 강력 새로 고침 `Cmd+Shift+R`(Windows `Ctrl+Shift+R`)을 합니다. 자세히: 「[GitHub Pages 정적 배포 가이드](../guides/github-pages-deploy-guide.md)」
2. **같은 계정, 같은 폴더인지 봅니다.** Claude는 교육기관에서 받은 계정, GitHub는 워크시트를 쓰던 계정으로 로그인합니다. Code 탭에서는 하위 폴더가 아니라 `axyourbody-prototype` 맨 위 폴더를 엽니다. 자세히: 「[Claude Code 데스크톱 앱 설치 (Mac판 · Windows판)](../guides/claude-code-install-guide.md)」
3. **복사본으로 되돌립니다.** 큰 변경 전에 만든 `<원래 파일 이름>-before-<작업>` 복사본이 있으면 "prototype-first-<테마이름>.html을 prototype-first-<테마이름>-before-states.html과 똑같은 내용으로 되돌려 주세요. 복사본 파일은 그대로 두세요."처럼 파일 이름만 바꿔 지시합니다. 직접 되돌릴 때는 망가진 파일을 지우고, 복사본을 한 번 더 복사해 원래 이름으로 바꿉니다. 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」
4. **사용 한도에 걸렸으면 기다리거나 다른 도구로 이어 갑니다.** 일정 시간이 지나면 다시 쓸 수 있습니다. 기다릴 수 없으면 [사전 안내](../pre-course-notice.md) 5번의 조건에 맞는 다른 회사의 AI 코딩 도구(OpenAI Codex, Cursor 등)로 같은 작업 폴더를 열고 이어 합니다. 만든 파일은 작업 폴더에 그대로 남습니다.

그래도 안 되면 손을 들어 현장에서 도움을 받습니다.

## Claude (웹·데스크톱 앱)

- **로그인 메일이 오지 않는다** → 스팸함을 보고, 1~2분 뒤 다시 요청합니다. 계정 정보는 교육기관 안내를 다시 봅니다. 자세히: 「[Claude 시작 가이드](../guides/claude-start-guide.md)」
- **"사용 한도에 가까워졌다"는 안내가 뜬다** → 일정 시간이 지나면 다시 쓸 수 있습니다. 긴 대화를 새 대화로 나누면 한도를 덜 씁니다. 자세히: 「[Claude 시작 가이드](../guides/claude-start-guide.md)」
- **`{ }`를 그대로 두고 보냈다** → 같은 대화에 "앞 지시문의 {책 제목}은 '데미안'이야. 다시 해 줘."처럼 빈자리에 들어갈 내용을 알려 줍니다(도서관 앱 예). 자세히: 「[Claude 시작 가이드](../guides/claude-start-guide.md)」
- **파일이 첨부되지 않는다** → 파일 이름에 특수문자가 많으면 영문으로 바꿉니다. 엑셀(`.xlsx`)로 저장한 사본이면 CSV로 다시 저장해 첨부합니다. 자세히: 「[Claude 시작 가이드](../guides/claude-start-guide.md)」
- **답이 지시와 다르다** → 원하는 결과를 한 문장으로 다시 쓰고, "먼저 무엇을 바꿀지 목록으로 보여 줘"라고 덧붙입니다. 자세히: 「[Claude 시작 가이드](../guides/claude-start-guide.md)」
- **표를 복사해 붙였더니 칸이 깨졌다** → 마우스로 끌어 고르지 말고 답 아래의 Copy 단추로 다시 복사합니다. 자세히: 「[Claude 시작 가이드](../guides/claude-start-guide.md)」
- **대화가 길어져 앞 내용을 놓친다** → "지금까지 정한 결론만 다섯 줄로 요약해 줘. 새 대화에 붙여 넣을 거야. 아직 정하지 못한 것은 따로 한 줄로 적어 줘."라고 보낸 뒤, New chat에 요약을 붙여 넣고 이어 갑니다. CSV는 다시 첨부합니다. 자세히: 「[Claude 시작 가이드](../guides/claude-start-guide.md)」
- **답에 나온 날짜·값을 믿어도 될지 모르겠다** → "그 판단의 근거가 된 줄을 파일 이름 · 날짜 · 값으로만 보여 줘"라고 묻고, CSV를 직접 열어 그 줄이 있는지 봅니다. 없으면 옮기지 않습니다. 자세히: 「[Claude 시작 가이드](../guides/claude-start-guide.md)」
- **과업 후보에 기능 이름이 섞여 나온다** → "기능 이름이 들어간 후보만 골라 상황과 하려는 일로 다시 써 줘." 자세히: 「[과업·불편 목록 가이드](../guides/task-pain-list-guide.md)」
- **페르소나 초안에 없는 수치가 섞였다** → "내가 준 자료에 없는 날짜와 숫자가 들어간 문장을 모두 찾아 목록으로 보여 줘. 고치지는 마." 자세히: 「[페르소나 카드 가이드](../guides/persona-card-guide.md)」
- **서비스 구조 설명서를 Claude가 고쳐 쓴다** → "설명서는 고치지 말고, 세 줄 설명과 질문 5개 이내만 답해 줘." 자세히: 「[서비스 구조 설명서 작성 가이드](../guides/service-structure-guide.md)」
- **영어 DESIGN.md가 잘 읽히지 않는다** → 문서를 붙여 넣고 "이 DESIGN.md의 색·글꼴·부품·하지 말 것을 한국어로 다섯 줄씩 요약해 줘. 문서는 고치지 마."라고 묻습니다. 자세히: 「[디자인 쇼핑처 둘러보기 가이드](../guides/design-shopping-guide.md)」

## Claude Code (Code 탭)

### 앱과 작업 폴더

- **Code 탭이 안 보이거나 화면이 가이드와 다르다** (환경 선택이 입력창 위에 있음) → 앱 버전을 올립니다. Mac은 메뉴 막대 **Claude → Check for Updates…**, Windows는 **Help → Check for Updates…**를 누르고 앱을 다시 엽니다. 자세히: 「[Claude Code 데스크톱 앱 설치 (Mac판 · Windows판)](../guides/claude-code-install-guide.md)」
- **`Error 403` 같은 로그인 오류가 난다** → 로그아웃한 뒤 다시 로그인합니다. 그래도 안 되면 앱을 완전히 끄고(Mac `Cmd+Q`, Windows 작업 관리자에서 Claude 끝내기) 다시 엽니다. 개인 무료 계정으로 들어가 있지 않은지도 봅니다. 자세히: 「[Claude Code 데스크톱 앱 설치 (Mac판 · Windows판)](../guides/claude-code-install-guide.md)」
- **Windows에서 "Git is required"가 뜬다** → 먼저 앱 버전을 올립니다. 그래도 뜨면 Git for Windows(git-scm.com)를 설치하고 앱을 다시 엽니다. 자세히: 「[Claude Code 데스크톱 앱 설치 (Mac판 · Windows판)](../guides/claude-code-install-guide.md)」
- **"Failed to load session"이 뜬다** → 고른 폴더를 옮기거나 이름을 바꾸지 않았는지 봅니다. 폴더 선택에서 `axyourbody-prototype`을 다시 고릅니다. 자세히: 「[Claude Code 데스크톱 앱 설치 (Mac판 · Windows판)](../guides/claude-code-install-guide.md)」
- **`@`로 가리킨 파일을 못 찾거나 목록에 바깥 파일이 보인다** → 작업 폴더를 잘못 연 것입니다. `axyourbody-prototype`을 다시 열고 "작업 폴더의 파일 목록을 폴더별로 보여 주세요. 파일은 만들거나 고치지 마세요."로 확인합니다. 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」
- **작업 폴더 밖의 파일을 고치거나 무엇을 설치하겠다고 한다** → 허락하지 않고 "왜 필요한지 먼저 설명해 주세요. 작업 폴더 안에서, 외부 라이브러리 없이 할 수 있는 방법으로 해 주세요."라고 답합니다. 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」
- **대화가 길어져 앞에서 정한 것을 잊는다** → 새 대화를 열고 "@context/service-structure.md @context/screen-flow.md 와 prototype-first-<테마이름>.html을 먼저 읽고, 지금 파일의 화면 목록을 알려 주세요."로 시작합니다. 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」
- **만들다 중간에 멈췄다** → "이어서 계속해 줘. 이미 만든 부분은 고치지 마." 문서라면 "이어서 써 줘. 이미 쓴 부분은 고치지 마." 자세히: 「[여러 버전 통합 가이드](../guides/version-merge-guide.md)」 · 「[나만의 DESIGN.md 만들기 가이드](../guides/my-own-design-md-guide.md)」

### 첫 프로토타입과 상태 화면

- **요약 없이 바로 만들기 시작했다** → 멈추고 "만들기 전에 이해한 내용을 다섯 줄로 요약해 주세요. 제가 확인한 뒤에 시작합니다." 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」
- **지시와 다른 결과가 나온다** → 원하는 결과를 한 문장으로 다시 쓰고 "무엇을 바꿀지 목록으로 먼저 보여 주고, 제가 승인하면 고쳐 주세요."를 붙입니다. 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」
- **브라우저 화면이 하얗거나 모든 버튼이 안 된다** → "브라우저로 열면 화면이 비어 있습니다. 원인을 찾아 쉬운 말로 설명하고, 그 부분만 고쳐 주세요." 두 번 해도 안 되면 복사본에서 되돌립니다. 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」
- **버튼을 눌러도 아무 일이 없다** → "{화면 이름}의 "{버튼 이름}" 버튼을 누르면 {다음 화면}으로 가야 하는데 아무 일도 없습니다. 이 버튼만 이어 주세요." 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」
- **지어낸 수치가 있다** → "{화면 이름}의 {숫자}는 data 폴더에 없는 값입니다. CSV에 있는 값으로 바꾸거나, 없으면 그 칸을 지워 주세요." 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」
- **고쳤더니 다른 곳도 바뀌었다** → "방금 수정에서 {바뀐 곳}도 바뀌었습니다. 그 부분만 수정 전으로 되돌려 주세요." 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」
- **상태 미리 보기 버튼이 없다** → "화면에 상태 미리 보기 전환 버튼을 달아, 정상·빈 상태·오류·로딩·이상치를 바꿔 가며 볼 수 있게 해 주세요. 다른 부분은 바꾸지 마세요." 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」

### 통합·디자인 스킬·리소스

- **줄 번호가 어긋난다** → 파일이 고쳐진 뒤일 가능성이 큽니다. "prototype-merged.html 의 영역 지도를 같은 형식으로 만들어 줘. 아무 파일도 고치지 마."로 다시 받습니다. 자세히: 「[여러 버전 통합 가이드](../guides/version-merge-guide.md)」
- **통합 파일에 영역이 빠졌다** → "번호 목록의 {번호}번 {영역 이름}이 prototype-merged.html 에 없어. {파일} {시작}~{끝}줄에서 가져와 넣어 줘. 다른 영역은 고치지 마." 자세히: 「[여러 버전 통합 가이드](../guides/version-merge-guide.md)」
- **통합하면서 색을 멋대로 통일했다** → "이번 단계에서는 각 영역의 색과 글꼴을 원래 파일 그대로 둬야 해. 원래 스타일로 되돌려 줘." 자세히: 「[여러 버전 통합 가이드](../guides/version-merge-guide.md)」
- **첫 프로토타입 파일이 바뀌었다** → "방금 prototype-first-<테마이름>.html 에 한 변경을 모두 되돌려 줘." 되돌아오지 않으면 시작 전에 만든 폴더 복사본에서 그 파일만 다시 복사해 옵니다. 자세히: 「[여러 버전 통합 가이드](../guides/version-merge-guide.md)」
- **`/` 목록에 스킬이 없다** → 새 대화를 열어 다시 봅니다. 작업 폴더, 대문자 `SKILL.md`, 영문 소문자·하이픈 폴더 이름을 확인합니다. 그래도 없으면 지시문을 `design/skill-{스킬이름}.md`로 저장해 가리킵니다. 자세히: 「[디자인 스킬 가져오기 가이드](../guides/design-skill-guide.md)」
- **설치 명령을 실행하겠다고 한다** → 거절하고 "설치는 하지 마. 이 파일 안에서 HTML·CSS·JavaScript만으로 같은 모양과 움직임을 만들어 줘." 자세히: 「[디자인 스킬 가져오기 가이드](../guides/design-skill-guide.md)」
- **스킬을 적용했더니 다른 영역도 바뀌었다** → "{영역 이름} 밖에서 바뀐 곳이 있어. prototype-merged-before-skill.html 과 비교해서 {영역 이름} 밖의 변경은 모두 원래대로 되돌려 줘." 자세히: 「[디자인 스킬 가져오기 가이드](../guides/design-skill-guide.md)」
- **흑백 보기가 일부 영역에만 적용된다** → "흑백 보기가 {영역 이름}에는 적용되지 않아. 페이지 전체가 회색조로 바뀌게 고쳐 줘. 모양은 바꾸지 마." 자세히: 「[파비콘·컬러 샘플 가이드](../guides/favicon-color-sample-guide.md)」

### 나만의 DESIGN.md와 배포 준비

- **테마 통일 뒤 배치가 바뀌었다** → "배치와 영역 순서가 prototype-improved.html 과 달라졌어. 배치는 원래대로 두고 색·글꼴·모서리·그림자·간격만 바꿔 줘." 자세히: 「[나만의 DESIGN.md 만들기 가이드](../guides/my-own-design-md-guide.md)」
- **재현 결과가 전혀 다르다** → 시험 폴더에 다른 파일이 없었는지, 새 대화였는지, 설정값이 숫자로 적혀 있는지부터 확인합니다. 자세히: 「[나만의 DESIGN.md 만들기 가이드](../guides/my-own-design-md-guide.md)」
- **점검 단계에서 Claude Code가 파일을 고쳤다** → 복사본 `prototype-final-before-deploy.html`에서 되살리고, "점검만 해 줘. 고치지 마."를 첫 줄에 두어 다시 보냅니다. 자세히: 「[배포 전 점검과 정적 배포 가이드](../guides/pre-deploy-check-guide.md)」
- **`deploy` 폴더에 다른 파일도 들어갔다** → "deploy 폴더에는 index.html 과 favicon.svg 만 남기고 나머지는 지워 줘. 작업 폴더의 원본은 건드리지 마." 자세히: 「[배포 전 점검과 정적 배포 가이드](../guides/pre-deploy-check-guide.md)」

## GitHub (워크시트 저장소·배포)

### 워크시트 저장소

- **Copy raw file 아이콘이 안 보인다** → 창을 넓힙니다. 또는 **Raw**를 눌러 열린 화면에서 `Cmd+A` → `Cmd+C`(Windows `Ctrl+A` → `Ctrl+C`)로 복사합니다. 자세히: 「[GitHub 워크시트 저장소 가이드](../guides/github-worksheet-repo-guide.md)」
- **`wild-mental`이 검색되지 않거나 초대가 사라졌다** → 철자(가운데 하이픈)를 확인합니다. 초대는 7일 안에 수락되지 않으면 사라지므로 다시 초대합니다. 자세히: 「[GitHub 워크시트 저장소 가이드](../guides/github-worksheet-repo-guide.md)」
- **Settings 탭이 없다** → 창이 좁으면 위쪽 탭 끝의 **⋯** 안에 있습니다. 그래도 없으면 자료실 저장소를 보고 있는 것입니다. 주소에 내 아이디가 있는지 봅니다. 자세히: 「[GitHub 워크시트 저장소 가이드](../guides/github-worksheet-repo-guide.md)」
- **워크시트 저장소를 Public으로 만들었다** → Settings 맨 아래 **Danger Zone**의 **Change visibility** → private → **I have read and understand these effects** → **Make this repository private**까지 누릅니다. 자세히: 「[GitHub 워크시트 저장소 가이드](../guides/github-worksheet-repo-guide.md)」
- **Preview에서 표가 깨졌다** → 칸 안에 `|`를 썼거나 줄을 바꾼 곳을 찾아 쉼표로 고칩니다. 자세히: 「[GitHub 워크시트 저장소 가이드](../guides/github-worksheet-repo-guide.md)」
- **이미지가 안 보이고 글자만 나온다** → 올린 파일 이름과 `( )` 안의 이름이 대소문자, 확장자(`.jpg` · `.jpeg` · `.png`)까지 똑같은지 봅니다. 자세히: 「[GitHub 워크시트 저장소 가이드](../guides/github-worksheet-repo-guide.md)」
- **쓴 내용이 사라졌다** → **Commit changes**를 누르지 않고 나오면 저장되지 않습니다. 지운 내용은 **History**(시계 아이콘)에서 그때 기록을 열어 복사해 다시 붙여 넣고 저장합니다. 자세히: 「[GitHub 워크시트 저장소 가이드](../guides/github-worksheet-repo-guide.md)」
- **시크릿 창에서 워크시트 저장소 링크가 404로 나온다** → 정상입니다. 비공개라는 뜻입니다. 자세히: 「[GitHub 워크시트 저장소 가이드](../guides/github-worksheet-repo-guide.md)」

### 배포 저장소 (GitHub Pages)

- **배포 주소가 404를 보여 준다** → ① 몇 분이 지났는지 ② Actions 탭에 빨간 X가 있는지 ③ `index.html`이 저장소 맨 위에 있는지 ④ 이름에 대문자가 없는지 ⑤ Settings → Pages가 `main` · `/ (root)`인지 봅니다. 폴더째 올렸다면 저장소를 지우고 새로 만들어 두 파일만 올립니다. 자세히: 「[GitHub Pages 정적 배포 가이드](../guides/github-pages-deploy-guide.md)」
- **Settings → Pages에 Branch 칸이 없거나 업그레이드 안내가 나온다** → 저장소가 Private입니다. 배포 저장소를 Public으로 새로 만듭니다. 워크시트 저장소는 Public으로 바꾸지 않습니다. 자세히: 「[GitHub Pages 정적 배포 가이드](../guides/github-pages-deploy-guide.md)」
- **화면은 나오는데 파비콘이 안 보인다** → 저장소에 `favicon.svg`가 있는지, 이름이 정확한지 봅니다. 맞다면 강력 새로 고침을 하거나 시크릿 창으로 다시 엽니다. 자세히: 「[GitHub Pages 정적 배포 가이드](../guides/github-pages-deploy-guide.md)」
- **고쳐 올렸는데 예전 화면이 나온다** → Actions 탭의 맨 위 줄이 초록 체크가 될 때까지 기다린 뒤 강력 새로 고침을 합니다. 자세히: 「[GitHub Pages 정적 배포 가이드](../guides/github-pages-deploy-guide.md)」
- **개인정보가 담긴 파일을 올렸다** → 지워도 고친 이력에 남습니다. Settings 맨 아래 **Danger Zone**의 **Delete this repository**로 저장소를 지우고, 점검을 다시 한 뒤 새 저장소를 만듭니다. 자세히: 「[GitHub Pages 정적 배포 가이드](../guides/github-pages-deploy-guide.md)」
- **발표 직전에 배포 링크가 404로 나온다** → 방금 올렸다면 몇 분 뒤 새로 고침합니다. 그래도 안 되면 발표는 로컬의 `prototype-final.html`로 하고, 제출 전까지 고칩니다. 자세히: 「[발표·동료 리뷰 진행 가이드](../guides/presentation-review-guide.md)」

## Figma

- **Duplicate 메뉴가 보이지 않는다** → 로그인했는지 봅니다. 캔버스 빈 곳을 한 번 누른 뒤 다시 파일 이름을 누릅니다. 자세히: 「[Figma 템플릿 열기·복제 가이드](../guides/figma-template-guide.md)」
- **글자가 안 고쳐지고 "View only"가 보인다** → 원본을 보고 있는 것입니다. 복제한 내 파일을 엽니다. 브라우저 탭 이름에 `axyourbody_`가 보여야 내 파일입니다. 자세히: 「[Figma 템플릿 열기·복제 가이드](../guides/figma-template-guide.md)」
- **템플릿 링크가 열리지 않는다** → 자료실 저장소의 `figma-template` 폴더에서 SVG 네 장을 내려받아, 새 **Design** 파일의 페이지 네 개에 한 장씩 끌어다 놓습니다. 자세히: 「[Figma 템플릿 열기·복제 가이드](../guides/figma-template-guide.md)」
- **내 파일을 못 찾겠다** → figma.com 첫 화면 왼쪽의 **Drafts**에서 `axyourbody_이름_프로필ID`를 찾습니다. 자세히: 「[Figma 템플릿 열기·복제 가이드](../guides/figma-template-guide.md)」
- **칸 이름 상자를 지웠다** → 바로 `Cmd+Z`(Windows `Ctrl+Z`)로 되돌리고 잠가 둡니다(`Shift+Cmd+L`, Windows `Ctrl+Shift+L`). 자세히: 「[Figma 템플릿 열기·복제 가이드](../guides/figma-template-guide.md)」
- **고쳐야 할 상자가 눌러도 골라지지 않는다** → 잠근 상자입니다. 왼쪽 레이어 목록에서 자물쇠를 눌러 풉니다. 자세히: 「[Figma 템플릿 열기·복제 가이드](../guides/figma-template-guide.md)」
- **화면이 너무 커서 페이지 전체가 안 보인다** → `Shift+1`로 화면에 맞춰 봅니다. 확대·축소는 `Cmd`(Windows `Ctrl`)를 누른 채 마우스 휠을 굴립니다. 자세히: 「[Figma 템플릿 열기·복제 가이드](../guides/figma-template-guide.md)」
- **Share 창에서 초대가 안 된다** → 이메일 주소에 띄어쓰기가 섞이지 않았는지 봅니다. 자세히: 「[Figma 템플릿 열기·복제 가이드](../guides/figma-template-guide.md)」
- **공유 링크를 "Anyone"으로 열어 두었다** → Share 창에서 **Only invited people**로 바꿉니다. 링크 주소는 그대로 써도 됩니다. 자세히: 「[Figma 템플릿 열기·복제 가이드](../guides/figma-template-guide.md)」

## Google Stitch

- **로그인이 안 되거나 "사용할 수 없다"고 나온다** → 회사·학교 Google 계정은 관리자가 막아 두었을 수 있습니다. 개인 Gmail 계정으로 다시 로그인합니다. 자세히: 「[Stitch 시작 가이드](../guides/stitch-start-guide.md)」
- **생성이 오래 걸리거나 멈췄다** → 2~3분 기다린 뒤 페이지를 새로 고칩니다. 만든 시안은 프로젝트에 남아 있습니다. 같은 지시를 여러 번 보내면 한도만 줄어듭니다. 자세히: 「[Stitch 시작 가이드](../guides/stitch-start-guide.md)」
- **한도를 다 썼다는 안내가 나온다** → 이미 만든 시안으로 비교를 마칩니다. 시간이 모자라면 테마 2개 × 화면 2장으로 줄입니다. 시안이 모자라면 짝의 Stitch 화면을 함께 봅니다. 자세히: 「[Stitch 시안 만들기 가이드](../guides/stitch-draft-guide.md)」 · 「[Stitch 시작 가이드](../guides/stitch-start-guide.md)」
- **DESIGN.md 파일 첨부가 안 되거나 입력창이 너무 길다** → 메모장으로 열어 내용 전체를 `[디자인 규칙]` 아래에 붙여 넣습니다. 길어도 그대로 보내도 됩니다. 잘리면 색 · 글꼴 · 부품 · 하지 말 것 항목만 붙입니다. 자세히: 「[Stitch 시안 만들기 가이드](../guides/stitch-draft-guide.md)」 · 「[Stitch 시작 가이드](../guides/stitch-start-guide.md)」
- **휴대폰 화면(App)으로 만들었다** → 같은 프로젝트에서 "같은 화면을 웹 데스크톱 너비로 다시 만들어 줘"라고 하거나, 새 프로젝트를 **Web**으로 엽니다. 자세히: 「[Stitch 시작 가이드](../guides/stitch-start-guide.md)」
- **고치라고 한 화면 말고 다른 화면이 바뀌거나 새 화면이 생겼다** → 캔버스에서 고칠 화면을 한 번 눌러 고른 상태로 두고 다시 지시합니다. 자세히: 「[Stitch 시작 가이드](../guides/stitch-start-guide.md)」
- **DESIGN.md를 무시하는 것 같다** → "첨부한 DESIGN.md의 색·글꼴·모서리 규칙을 세 줄로 요약한 뒤 그 규칙대로 다시 그려 주세요." 자세히: 「[Stitch 시안 만들기 가이드](../guides/stitch-draft-guide.md)」
- **고칠수록 나빠진다** → 고치기를 멈추고 직전에 내보낸 이미지를 비교표에 씁니다. 남은 문제는 이유 칸에 적습니다. 자세히: 「[Stitch 시안 만들기 가이드](../guides/stitch-draft-guide.md)」
- **이미지 저장 항목이 없다** → 시안을 크게 띄우고 화면 캡처로 시안 부분만 잡습니다. Mac `Ctrl+Shift+Cmd+4`, Windows `Win+Shift+S`. 자세히: 「[Stitch 시작 가이드](../guides/stitch-start-guide.md)」

## 브라우저·파일·폴더

- **파일 이름이 `.md.txt`로 끝나거나 `index.html`이 `index`로만 보인다** → 확장자가 숨겨져 있습니다. Mac은 **Finder → 설정 → 고급 → 모든 파일 확장자 보기**, Windows는 파일 탐색기 **보기 → 표시 → 파일 이름 확장명**을 켜고 `.txt`를 지웁니다. 자세히: 「[Claude Code 데스크톱 앱 설치 (Mac판 · Windows판)](../guides/claude-code-install-guide.md)」 · 「[디자인 쇼핑처 둘러보기 가이드](../guides/design-shopping-guide.md)」
- **메모장이나 텍스트 편집기로 `.md` 파일을 저장하기 어렵다** → 메모장은 파일 형식 "모든 파일", 인코딩 UTF-8을 고릅니다. Mac 텍스트 편집기는 포맷 메뉴의 "일반 텍스트로 만들기"를 먼저 누릅니다. 어려우면 Code 탭에 "context 폴더에 screen-flow.md 파일을 만들고, 아래 글을 한 글자도 바꾸지 말고 그대로 저장해 줘."라고 맡깁니다. 자세히: 「[화면 흐름 순서표 작성 가이드](../guides/screen-flow-guide.md)」
- **`.claude` 폴더가 보이지 않는다** → Mac Finder에서는 점으로 시작하는 숨은 폴더라 `Cmd+Shift+.`을 누릅니다. Windows 파일 탐색기에서는 보통 그대로 보이고, 안 보이면 **보기 → 표시 → 숨겨진 항목**을 켭니다. 자세히: 「[디자인 스킬 가져오기 가이드](../guides/design-skill-guide.md)」
- **복사본을 만드는 법을 모르겠다** → Mac은 Finder에서 파일을 고르고 `Cmd+D`, Windows는 `Ctrl+C` → `Ctrl+V` 뒤 "- 복사본"이 붙은 파일 이름을 `F2`로 고칩니다. 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」
- **HTML 파일이 브라우저 대신 편집기로 열린다** → 오른쪽 버튼 → 다음으로 열기(Mac) 또는 연결 프로그램(Windows)에서 Chrome, Safari, Edge 같은 브라우저를 고릅니다. 자세히: 「[Claude Code 프로토타이핑 따라 하기](../guides/claude-code-prototyping-guide.md)」
- **데이터셋 링크를 눌렀더니 CSV가 다운로드 폴더로 바로 받아졌다** → 정상입니다. 다운로드 폴더에서 담당 프로필 폴더로 옮깁니다. 파일 이름은 바꾸지 않습니다. 자세히: 「[과업·불편 목록 가이드](../guides/task-pain-list-guide.md)」
- **Excel에서 CSV의 한글이 깨져 보인다** → Google 스프레드시트에서 파일 → 가져오기 → 업로드로 엽니다. Excel을 쓰려면 Windows는 데이터 → 텍스트/CSV에서, Mac은 파일 → 가져오기 → CSV 파일로 열고 파일 원본(인코딩)을 UTF-8로 고릅니다. 자세히: 「[과업·불편 목록 가이드](../guides/task-pain-list-guide.md)」
- **CSV가 한 칸에 몰려 보인다** (쉼표가 그대로 보임) → 프로그램의 가져오기 기능으로 다시 열고 구분 기호를 "쉼표"로 고릅니다. 자세히: 「[과업·불편 목록 가이드](../guides/task-pain-list-guide.md)」
- **CSV를 닫을 때 "CSV 형식으로 저장할까요?"가 나온다** → 저장하지 않습니다. 원본 CSV는 고쳐서 저장하지 않습니다. 자세히: 「[과업·불편 목록 가이드](../guides/task-pain-list-guide.md)」
- **정렬한 CSV를 원본 위에 저장했다** → 원본 파일을 다시 받아 `data` 폴더에 넣고, 정렬은 사본에서 합니다. 자세히: 「[화면 흐름 순서표 작성 가이드](../guides/screen-flow-guide.md)」
- **화면 전체를 흑백으로 보고 싶다** → Mac은 시스템 설정 → 손쉬운 사용 → 디스플레이 → 색상 필터, Windows는 설정 → 접근성 → 색 필터에서 회색조를 켭니다. 확인이 끝나면 꼭 끕니다. 자세히: 「[Stitch 시안 만들기 가이드](../guides/stitch-draft-guide.md)」
