# 사전 안내 (Mac판 · Windows판)

수업 첫날 **11/24(화) 전까지** 아래 준비를 끝내 두세요. 계정 만들기와 앱 설치를 수업 시간에 하면 실습 시간이 그만큼 줄어듭니다. 모두 합쳐 1시간 정도 걸립니다.

**준비물**: 수업에 가져올 노트북(Mac 또는 Windows), 최신 브라우저(Chrome · Edge · Safari 중 하나), 교재

## 1. 한눈에 보는 체크리스트

다 끝낸 항목에 표시하면서 진행하세요.

- [ ] GitHub 계정을 만들었다 (실명이 드러나지 않는 아이디)
- [ ] 비공개 저장소 `axyourbody-worksheet`를 만들고 `worksheet.md`를 붙여 넣었다
- [ ] 그 저장소에 강사 GitHub 아이디 `wild-mental`을 초대했다
- [ ] 교육기관에서 받은 Claude 계정으로 claude.ai에 로그인했다
- [ ] Claude 데스크톱 앱을 설치하고 같은 계정으로 로그인했다
- [ ] 앱의 **Code** 탭에서 빈 작업 폴더 `axyourbody-prototype`을 열어 보았다
- [ ] Figma 무료 계정을 만들었다
- [ ] Google 계정으로 Google Stitch에 로그인해 보았다
- [ ] 온라인 자료실을 즐겨찾기에 넣었다

## 2. GitHub 계정과 워크시트 저장소

GitHub(깃허브: 파일을 저장소 단위로 보관하고 고친 이력을 남기는 웹 서비스)는 4일 동안 워크시트를 쓰는 곳이고, Day 4에는 완성한 프로토타입을 공개하는 곳입니다.

1. github.com에서 무료 계정을 만듭니다. **아이디는 Day 4 배포 주소에 그대로 들어갑니다**(예: `https://아이디.github.io/axyourbody/`). 실명을 드러내고 싶지 않다면 실명이 아닌 아이디로 만드세요.
2. 비공개(Private) 저장소 `axyourbody-worksheet`를 만들고, 자료실의 [worksheet.md](https://github.com/wild-mental/ax-wave-uxui-wildmental/blob/main/worksheet-template/worksheet.md)를 복사해 `worksheet.md`로 붙여 넣습니다.
3. 저장소의 **Settings → Collaborators → Add people**에서 강사 아이디 `wild-mental`을 초대합니다.

단계별 화면은 교재 부록 A-2와 「[GitHub 워크시트 저장소 가이드](guides/github-worksheet-repo-guide.md)」를 따르세요. 저장소는 끝까지 **Private**으로 둡니다.

## 3. Claude 계정

이 수업에서는 **교육기관에서 제공하는 Claude Pro 계정**을 씁니다. 계정 정보는 교육기관 안내로 따로 받습니다.

1. 브라우저에서 claude.ai에 접속해 받은 계정으로 로그인합니다.
2. 새 대화를 열어 "안녕"이라고 보내 보고 답이 오는지 확인합니다.

자세한 사용법은 교재 부록 A-1과 「[Claude 시작 가이드](guides/claude-start-guide.md)」에 있습니다. 계정 안내를 아직 받지 못했다면 4번의 앱 설치까지만 해 두고, 첫날 수업 시작 전에 알려 주세요.

## 4. Claude 데스크톱 앱 설치와 로그인

Day 3~4에는 Claude 데스크톱 앱의 **Code** 탭(Claude Code)으로 프로토타입을 만듭니다. 명령어를 치는 터미널은 쓰지 않습니다.

| 단계 | Mac | Windows |
|---|---|---|
| 내려받기 | Claude 공식 다운로드 페이지(claude.ai/download)에서 **macOS**용을 내려받습니다 | 같은 페이지에서 **Windows**용을 내려받습니다 (ARM 노트북이면 ARM64용) |
| 설치 | 내려받은 파일을 열고 Claude 아이콘을 **Applications**(응용 프로그램) 폴더로 끌어다 놓습니다 | 내려받은 설치 파일을 실행하고 안내대로 설치합니다 |
| 로그인 | 앱을 열고 3번의 Claude 계정으로 로그인합니다 | 앱을 열고 3번의 Claude 계정으로 로그인합니다 |
| 확인 | 앱 위쪽에 **Code** 탭이 보이는지 확인합니다 | 앱 위쪽에 **Code** 탭이 보이는지 확인합니다 |

단계별 화면과 막혔을 때 볼 내용은 「[Claude Code 데스크톱 앱 설치 (Mac판 · Windows판)](guides/claude-code-install-guide.md)」에 있습니다.

## 5. 사용 한도에 걸렸을 때 쓸 수 있는 다른 도구

Claude Pro 계정에는 일정 시간 동안 쓸 수 있는 양(사용 한도)이 있습니다. 실습 중에 한도를 다 써서 Claude Code를 한동안 쓸 수 없게 되면, **OpenAI Codex나 Cursor처럼 아래 조건에 맞는 다른 회사의 AI 코딩 도구**를 써도 됩니다.

- 내 컴퓨터의 폴더를 작업 폴더로 열 수 있다
- 그 폴더 안의 파일을 읽고, 새 파일을 만들고, 고칠 수 있다
- 대화로 지시하고 결과를 파일로 저장할 수 있다

교재의 지시문은 그대로 쓰고, 파일을 가리키는 `@` 표기 같은 사용법만 그 도구의 방식에 맞춥니다. 수업 중에 바로 바꾸고 싶다면 하나를 미리 설치해 두어도 좋습니다(선택).

## 6. Figma 무료 계정

figma.com에서 무료 계정을 만들고 로그인해 둡니다. 템플릿 복제는 Day 2에 「[Figma 템플릿 열기·복제 가이드](guides/figma-template-guide.md)」를 보며 함께 합니다.

## 7. Google 계정과 Google Stitch

Google 계정으로 stitch.withgoogle.com에 로그인해 첫 화면이 열리는지만 확인합니다. 사용법은 Day 3에 교재 부록 A-4와 「[Stitch 시작 가이드](guides/stitch-start-guide.md)」로 배웁니다.

## 8. 설치 확인: 작업 폴더 열어 보기

수업 당일 바로 실습할 수 있는지 미리 확인합니다.

1. 바탕화면이나 문서 폴더에 빈 폴더 `axyourbody-prototype`을 만듭니다.
2. Claude 데스크톱 앱에서 **Code** 탭을 엽니다.
3. 입력창 아래의 환경 선택에서 내 컴퓨터(로컬)를 고르고, 그 옆의 폴더 선택에서 1번 폴더를 고릅니다.
4. "이 폴더에 무엇이 있는지 알려 줘"라고 보내 봅니다. "비어 있다"는 답이 오면 준비가 끝난 것입니다.

화면 구성이 이 안내와 다르면 「[Claude Code 데스크톱 앱 설치 (Mac판 · Windows판)](guides/claude-code-install-guide.md)」의 막혔을 때 항목을 보세요.

## 9. 온라인 자료실과 막혔을 때

- 온라인 자료실 `https://wild-mental.github.io/ax-wave-uxui-wildmental/`을 즐겨찾기에 넣어 두세요. 온라인 가이드, Figma 템플릿 링크, 지시문 킷, 프로필 데이터셋이 모두 여기 있습니다.
- 준비 중에 막힌 단계가 있으면 체크리스트에 표시만 해 두고, **첫날 수업 시작 전에 현장에서** 함께 해결합니다. 막힌 화면을 캡처해 오면 더 빨리 해결할 수 있습니다.

화면 확인 날짜: 2026-11-17
