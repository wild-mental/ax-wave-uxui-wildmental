# GitHub Pages 정적 배포 가이드

교재: 부록 A-6 · GitHub Pages 정적 배포 · 쓰는 때: Day 4, 4.7절 배포 전 점검을 마친 뒤 · 쓰는 곳: 배포 전용 공개 저장소(예: `axyourbody`)

## 이 가이드에서 볼 것

클릭 순서는 교재 부록 A-6에 다 있습니다. 이 가이드는 그 순서를 화면으로 보여 주고, 단계마다 "이렇게 보이면 정상"과 자주 막히는 곳을 더합니다. 개인정보 점검과 `deploy` 폴더 만들기는 「[배포 전 점검과 정적 배포 가이드](pre-deploy-check-guide.md)」에서 먼저 끝냅니다.

## 0. 시작 전 확인

- [ ] 배포 전 점검표의 일곱 항목 중 "배포 후 재확인"을 뺀 여섯 항목이 정상이거나 조치가 끝났다
- [ ] `deploy` 폴더 안에 `index.html`, `favicon.svg` **두 파일만** 있다
- [ ] 파일 이름이 영문 소문자다. 확장자가 보이게 설정했다(Mac: **Finder → 설정 → 고급 → 모든 파일 확장자 보기**, Windows: 파일 탐색기 **보기 → 표시 → 파일 이름 확장명**)
- [ ] 워크시트를 쓰던 GitHub 계정으로 github.com에 로그인했다

## 1. 배포 전용 공개 저장소 만들기

1. github.com 오른쪽 위 **+ → New repository**를 누릅니다.
2. **Repository name**에 `axyourbody`처럼 영문 소문자 이름을 씁니다. 이 이름이 주소 끝에 붙습니다. `아이디.github.io`라는 이름은 쓰지 않습니다(다른 용도의 저장소가 됩니다).
3. **Public**을 고릅니다. **Add a README file** 같은 선택 칸은 켜지 않고 그대로 둡니다.
4. **Create repository**를 누릅니다.

(선택) 이 저장소는 누구나 볼 수 있고, 올린 기록에 GitHub 계정 이메일이 남을 수 있습니다. 이메일을 드러내고 싶지 않다면 올리기 전에 github.com 오른쪽 위 프로필 사진 → **Settings → Emails**에서 **Keep my email addresses private**를 켭니다. 그다음부터 웹에서 올린 기록에는 GitHub가 만든 대신 주소가 남습니다.

이렇게 보이면 정상: 빈 저장소 화면 가운데에 **uploading an existing file** 링크가 있는 안내 상자가 나옵니다.

## 2. 두 파일 올리기

1. **uploading an existing file**(또는 **Add file → Upload files**)을 누릅니다.
2. `deploy` 폴더를 열고 **안의 두 파일**을 함께 골라 브라우저의 끌어다 놓는 칸에 놓습니다.

| Mac | Windows |
|---|---|
| Finder에서 `deploy` 폴더를 열고 `Cmd`를 누른 채 두 파일을 눌러 고른 뒤 끌어다 놓습니다 | 파일 탐색기에서 `deploy` 폴더를 열고 `Ctrl`을 누른 채 두 파일을 눌러 고른 뒤 끌어다 놓습니다 |

3. 아래로 내려 **Commit changes**를 누릅니다.

이렇게 보이면 정상: 저장소 첫 화면의 파일 목록이 `favicon.svg`, `index.html` 두 줄입니다. `deploy`라는 폴더가 보이면 폴더째 올린 것입니다. 「막혔을 때」의 404 항목대로 고칩니다.

## 3. Pages 켜기

1. 저장소 위쪽의 **Settings**를 누릅니다(안 보이면 `···` 메뉴 안에 있습니다).
2. 왼쪽 메뉴의 **Pages**를 누릅니다.
3. **Build and deployment**의 **Source**가 **Deploy from a branch**인지 봅니다.
4. **Branch**에서 `main`, 옆 폴더 칸에서 `/ (root)`를 고르고 **Save**를 누릅니다.

> [캡처 예정] 공통: Settings → Pages의 Build and deployment(Deploy from a branch · main · / (root) · Save)

## 4. 공개 주소 확인

1. 몇 분 기다린 뒤 Settings → Pages 화면을 새로 고칩니다. 길게는 10분쯤 걸리기도 합니다.
2. 맨 위에 "Your site is live at"과 함께 `https://아이디.github.io/axyourbody/` 형식의 주소, **Visit site** 버튼이 나오면 배포가 끝난 것입니다.
3. 주소가 아직 안 나오면 저장소 위쪽의 **Actions** 탭을 엽니다. "pages build and deployment" 줄 앞이 노란 원이면 진행 중, 초록 체크면 끝, 빨간 X면 실패입니다.

## 5. 직접 열어 확인하고 기록하기

- **시크릿 창**(Chrome · Edge · Safari 모두 Mac `Cmd+Shift+N`, Windows `Ctrl+Shift+N`)으로 공개 주소를 엽니다. 로그인하지 않은 다른 사람이 보는 화면과 같습니다.

- 핵심 과업을 처음부터 끝까지 눌러 보고, 탭에 파비콘이 보이는지 봅니다.
- 휴대폰으로도 엽니다. 주소를 직접 치기 번거로우면 나에게 메시지로 보내 엽니다.
- 주소를 배포 전 점검표의 "배포 후 재확인" 행과 버전 기록 아래 "배포 링크"에 적습니다.

## 6. 고쳐서 다시 올리기

1. 작업 폴더에서 고친 뒤, 배포 전 점검을 바뀐 부분만 다시 합니다.
2. 배포 저장소에서 **Add file → Upload files**로 **같은 이름**의 파일을 올리고 **Commit changes**를 누릅니다. 같은 이름이면 덮어써집니다.
3. 몇 분 뒤 주소를 새로 고칩니다. 그대로면 강력 새로 고침(Mac `Cmd+Shift+R`, Windows `Ctrl+Shift+R`)을 합니다.

## 7. 잘못 올렸을 때

- **개인정보가 없는 파일을 하나 더 올렸다** → 그 파일을 눌러 열고, 오른쪽 위 `···` 메뉴의 **Delete file** → **Commit changes**로 지웁니다.
- **개인정보가 담긴 파일을 올렸다** → 지워도 고친 이력에 남습니다. **Settings** 맨 아래 **Danger Zone**의 **Delete this repository**로 저장소를 통째로 지우고, 점검을 다시 한 뒤 새 저장소를 만듭니다.

## 워크시트 저장소와 헷갈리지 않기

| | 워크시트 저장소 | 배포 저장소 |
|---|---|---|
| 이름 | `axyourbody-worksheet` | `axyourbody` (예) |
| 공개 범위 | **Private** (끝까지) | **Public** |
| 들어가는 것 | `worksheet.md`, 이미지, `my-own-DESIGN.md` | `index.html`, `favicon.svg` 두 파일만 |
| Pages | 켜지 않음 | 켬 |
| 초대 | 강사 `wild-mental` | 없음 |

지금 보고 있는 저장소가 어느 쪽인지는 저장소 이름 옆의 **Private** / **Public** 표시로 확인합니다.

## 막혔을 때

- **주소가 404를 보여 준다** → ① 아직 몇 분이 안 지났는지 ② Actions 탭에 빨간 X가 있는지 ③ `index.html`이 `deploy` 폴더 안이 아니라 저장소 맨 위에 있는지 ④ 이름이 `Index.html`, `index.HTML`처럼 대문자가 아닌지 ⑤ Settings → Pages가 `main` · `/ (root)`인지 봅니다. 폴더째 올렸다면 저장소를 지우고 새로 만들어 두 파일만 올리는 것이 가장 빠릅니다.
- **Settings → Pages에 Branch 고르는 칸이 없거나 업그레이드 안내가 나온다** → 저장소가 Private입니다. 배포 저장소를 Public으로 새로 만듭니다. 워크시트 저장소는 Public으로 바꾸지 않습니다.
- **Branch 목록에 main이 없다** → 아직 파일을 올리지 않은 것입니다. 2번을 먼저 합니다.
- **화면은 나오는데 파비콘이 안 보인다** → 저장소에 `favicon.svg`가 있는지, 이름이 정확한지 봅니다. 맞다면 강력 새로 고침을 하거나 시크릿 창으로 다시 엽니다. 브라우저가 예전 아이콘을 기억하고 있을 때가 많습니다.
- **고쳐 올렸는데 예전 화면이 나온다** → Actions 탭의 맨 위 줄이 초록 체크가 될 때까지 기다린 뒤 강력 새로 고침을 합니다.

화면 확인 날짜: 2026-11-17
