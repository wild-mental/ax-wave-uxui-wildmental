#!/bin/sh
# 상위 프로젝트(교재 원고)에서 사본을 다시 가져온다. 저장소 맨 위에서 실행: sh _context/sync-from-textbook.sh
# 원본: ../docs/4-1/ (인쇄본 원고·지시문 킷·데이터셋·Figma 구성안·제작 계획)
set -e
HERE=$(cd "$(dirname "$0")/.." && pwd)
SRC="$HERE/../docs/4-1"
[ -d "$SRC/manuscript" ] || { echo "상위 프로젝트 docs/4-1 을 찾을 수 없습니다: $SRC"; exit 1; }
cp "$SRC/kits/claude-code-prompts.md" "$SRC/kits/DESIGN-axyourbody-sample.md" "$HERE/kits/"
for p in m-general f-general m-athlete f-athlete; do
  mkdir -p "$HERE/datasets/$p" && cp "$SRC/dataset/$p/"*.csv "$HERE/datasets/$p/"
done
cp "$SRC/ONLINE_MATERIALS_PLAN.md" "$HERE/_context/"
python3 - "$SRC/manuscript" "$HERE/textbook-materials" <<'PY'
import re, sys
m, out = sys.argv[1], sys.argv[2]
note = '> 교재 「웹서비스 UX/UI 기획」 앞부분과 같은 글입니다. Claude에 붙여 넣을 때 필요한 부분만 복사해 쓰세요.\n\n'
for src, dst in [('01-common-prd.md', 'common-prd.md'), ('02-profiles.md', 'profile-cards.md')]:
    s = re.sub(r'<!--.*?-->\n?', '', open(f'{m}/{src}', encoding='utf-8').read())
    head, body = s.split('\n', 1)
    open(f'{out}/{dst}', 'w', encoding='utf-8').write(head + '\n\n' + note + body.lstrip('\n'))
PY
python3 "$HERE/_context/gen_placeholders.py"
echo "사본과 교재 원문 발췌를 다시 만들었습니다. git diff 로 바뀐 곳을 확인하세요."
