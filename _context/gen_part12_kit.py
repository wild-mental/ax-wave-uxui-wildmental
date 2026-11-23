"""교재 원고 Part 1·2의 [실습 안내] 지시문 블록을 kits/claude-prompts-part-1-2.md 로 옮긴다.
sync-from-textbook.sh 가 부른다. 원고의 지시문 블록 위치가 바뀌면 SPEC 의 행 번호 대신 첫 줄로 찾는다."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
M = os.path.join(HERE, '..', '..', 'docs', '4-1', 'manuscript')
OUT = os.path.join(HERE, '..', 'kits', 'claude-prompts-part-1-2.md')
# (파일, 지시문 첫 줄 앞부분, 절, 이름, 워크시트, 안내)
SPEC = [
 ('part-1.md', '나는 서비스기획을 공부하고 있어', '1.2', '사례 분석 메모 정리 지시문', '익숙한 서비스의 사용 경험을 과업 관점으로 뜯어본 사례 분석 시트', '써 보며 적은 메모를 `{메모 붙여 넣기}` 자리에 넣습니다.'),
 ('part-1.md', '너는 서비스기획 보조야', '1.5', '과업 후보 넓히기 지시문', '타깃 사용자의 해야 할 일과 불편을 정리한 과업·불편 목록', '프로필 카드는 [공통 PRD와 프로필 카드](../textbook-materials/profile-cards.md)에서 내 프로필 것을 복사합니다. `[내가 찾은 단서]`의 예는 교재의 예이므로 내가 찾은 단서로 바꿉니다.'),
 ('part-1.md', '아래는 내가 정리한 과업·불편 목록과', '1.6', '페르소나 카드 초안 지시문', '설계 판단의 기준이 되는 타깃 사용자 페르소나 카드', '과업·불편 목록은 워크시트 문서의 본표를 복사합니다.'),
 ('part-2.md', '아래는 가상 인물 박준혁(38세', '2.2', '흐름이 바뀌는 날 찾기 지시문', '고객 여정 위에 사건과 대상 객체를 붙인 이벤트 보드 · 여정 레인', '첫 줄의 인물 소개는 교재의 예(박준혁)입니다. 내 프로필의 이름과 한 줄 소개로 바꾸고, 내 프로필 폴더의 CSV 내용을 붙여 넣습니다. 일반인 프로필(김도현·이서연)은 식사 기록이 빈 날도 중요한 단서이므로 `meal.csv`도 함께 넣습니다. CSV 파일은 붙여 넣는 대신 대화에 첨부해도 됩니다.'),
 ('part-2.md', '아래는 내가 만든 서비스 AX YOUR BODY의 이벤트 보드야', '2.4', '빠진 사건 찾기 지시문', '고객 여정 위에 사건과 대상 객체를 붙인 이벤트 보드 · 사건 레인', '사건 카드를 다 붙인 뒤에 씁니다. 사건 목록은 「[이벤트 보드 사용 가이드](../guides/event-board-guide.md)」 3부처럼 보드를 PDF로 내보내 Claude에게 글로 옮기게 한 뒤 붙여 넣습니다.'),
 ('part-2.md', '아래는 AX YOUR BODY의 대상 객체 카드야', '2.5', '대상 객체 카드 점검 지시문', '서비스가 다루는 대상 객체·속성·관계를 정리한 대상 객체 카드', '첫 줄의 인물 소개는 교재의 예(박준혁)입니다. 내 프로필로 바꿉니다.'),
 ('part-2.md', '아래는 내가 설계한 서비스의 구조 설명서야', '2.8', '서비스 구조 설명서 점검 지시문', 'Claude에 넘길 서비스 구조 설명서', '설명서 1~8번을 다 채운 뒤에 씁니다.'),
]
def block(f, first):
    L = open(os.path.join(M, f), encoding='utf-8').read().split('\n')
    for i, l in enumerate(L):
        if l.startswith('> ```') and i + 1 < len(L) and L[i + 1].lstrip('> ').startswith(first):
            j = i + 1
            while not L[j].startswith('> ```'): j += 1
            return [x[2:] if x.startswith('> ') else x[1:] for x in L[i:j + 1]]
    sys.exit(f'지시문을 찾지 못했습니다: {f} · {first}')
def anchor(sec, name): return sec.replace('.', '') + '-' + name.replace(' ', '-').replace('·', '')
out = ['# Part 1·2 지시문 킷', '',
 '교재 Part 1·2의 [실습 안내]에 인쇄된 Claude 지시문을 복사해 쓸 수 있게 옮겼습니다. 내용은 교재와 같습니다. 지시문 이름은 찾기 쉽게 이 자료실에서 붙인 것입니다.', '',
 '- **쓰는 법:** 회색 상자 안의 글을 모두 복사해 Claude 새 대화에 붙여 넣고, `{ }` 부분을 내 내용으로 바꿉니다(교재 부록 A-1).',
 '- **받은 결과:** 그대로 쓰지 말고 근거를 확인한 뒤 워크시트 문서의 해당 표로 옮깁니다.',
 '- **Part 3·4 지시문:** [Part 3·4 지시문 킷](claude-code-prompts.md)에 있습니다.', '',
 '| 교재 | 지시문 | 쓰는 워크시트 |', '|---|---|---|']
out += [f'| {s} | [{n}](#{anchor(s, n)}) | {w} |' for _, _, s, n, w, _ in SPEC] + ['']
for f, first, s, n, w, note in SPEC:
    out += [f'## {s} {n}', '', f'교재 {s}절 · 워크시트: {w}', '', note, ''] + block(f, first) + ['']
open(OUT, 'w', encoding='utf-8').write('\n'.join(out).rstrip() + '\n')
print('kits/claude-prompts-part-1-2.md:', len(SPEC), '개')
