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
python3 "$HERE/_context/gen_placeholders.py"
echo "사본과 교재 원문 발췌를 다시 만들었습니다. git diff 로 바뀐 곳을 확인하세요."
