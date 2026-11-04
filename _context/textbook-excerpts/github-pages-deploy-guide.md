# 교재 원문 발췌 — 「GitHub Pages 정적 배포 가이드」

> 인쇄본 원고(`docs/4-1/manuscript/appendix-a-tools.md`)에서 이 가이드를 가리키는 부분을 그대로 옮겼습니다. 생성: `_context/gen_placeholders.py` (2026-11-04 원고 기준). 원고가 바뀌면 다시 뽑습니다.

## A-6 · GitHub Pages 정적 배포

→ 온라인 가이드: 「GitHub Pages 정적 배포 가이드」

GitHub Pages(깃허브 페이지: GitHub 저장소에 올린 HTML 파일을 그대로 웹 주소로 공개해 주는 기능)로 배포합니다. A-2에서 만든 GitHub 계정을 그대로 씁니다. 무료 계정에서는 **공개(Public) 저장소**에서만 Pages를 켤 수 있으므로, 워크시트 저장소와 별도로 **배포 전용 공개 저장소**를 하나 더 만들고 거기에는 배포할 두 파일만 올립니다.

준비
1. **배포 전 점검표를 먼저 끝냅니다**(워크시트 「공개 전 개인정보·품질을 확인한 배포 전 점검표와 배포 링크」). 실제 이름·연락처·실제 신체 수치·사진이 남아 있지 않은지 확인합니다.
2. 작업 폴더의 `deploy` 폴더에 `index.html`(`prototype-final.html`을 바꿔 넣은 것)과 `favicon.svg` 두 파일만 있는지 확인합니다. CSV·워크시트·DESIGN 파일은 넣지 않습니다(지시문 킷의 「배포 전 개인정보 점검·정적 배포 준비 지시문」).
3. 브라우저에서 `deploy/index.html`을 직접 열어 모든 화면과 파비콘이 보이는지 확인합니다. 파일 이름은 모두 영문 소문자로 씁니다.

배포 저장소 만들기
1. github.com 오른쪽 위 **+ → New repository**를 누릅니다.
2. 저장소 이름을 정합니다(예: `axyourbody`). 이 이름이 주소 끝에 붙습니다.
3. 공개 범위는 **Public**을 고르고 **Create repository**를 누릅니다.

파일 올리기
1. 새 저장소 첫 화면의 **uploading an existing file** 링크(또는 **Add file → Upload files**)를 누릅니다.
2. `deploy` 폴더 **안의** 두 파일(`index.html`, `favicon.svg`)을 끌어다 놓습니다. 폴더째 올리지 않습니다. `index.html`이 저장소 맨 위에 있어야 첫 화면으로 열립니다.
3. 아래의 **Commit changes**를 눌러 올리기를 마칩니다.

Pages 켜기
1. 저장소의 **Settings → Pages**로 갑니다.
2. **Build and deployment**의 Source를 **Deploy from a branch**로 두고, Branch를 **main**, 폴더를 `/ (root)`로 골라 **Save**를 누릅니다.
3. 1~2분 기다린 뒤 Settings → Pages 화면을 새로 고치면 맨 위에 공개 주소가 나타납니다. 주소는 `https://아이디.github.io/저장소이름/` 형식입니다. 진행 상황은 저장소의 **Actions** 탭에서 볼 수 있고, 초록색 체크 표시가 뜨면 배포가 끝난 것입니다.

확인과 기록
1. 공개 주소를 열어 모든 화면, 버튼, 파비콘이 제대로 나오는지 확인합니다. 휴대폰으로도 한 번 엽니다.
2. 주소를 버전 기록의 "배포 링크" 칸과 배포 전 점검표의 "배포 후 재확인" 행에 적습니다.

고쳐서 다시 올릴 때
- **Add file → Upload files**로 같은 이름의 파일을 다시 올리고 Commit changes를 누르면 덮어씁니다. 1~2분 뒤 주소를 새로 고칩니다. 바뀌지 않아 보이면 강력 새로 고침(Mac `Cmd+Shift+R`, Windows `Ctrl+Shift+R`)을 합니다.

주소가 열리지 않을 때(404)
- 아직 1~2분이 지나지 않았는지, Actions 탭에 실패 표시가 있는지 봅니다.
- `index.html`이 폴더 안이 아니라 저장소 맨 위에 있는지, 이름이 `Index.html`처럼 대문자로 바뀌지 않았는지 확인합니다.
- Settings → Pages의 Branch가 main, 폴더가 / (root)인지 확인합니다.

공개 저장소에서 꼭 기억할 것
- 공개 저장소는 주소를 아는 누구나 **파일과 고친 이력까지** 볼 수 있습니다. 실수로 올린 파일은 지워도 이력에 남습니다. 그런 파일을 올렸다면 Settings 맨 아래의 **Delete this repository**로 저장소를 지우고, 새 저장소를 만들어 다시 올립니다.
- 공개하고 싶지 않은 내용은 배포 저장소에 올리지 않는 것이 유일하게 확실한 방법입니다. 워크시트는 A-2의 비공개 저장소에만 둡니다.
