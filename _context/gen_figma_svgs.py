#!/usr/bin/env python3
"""Figma 템플릿 SVG 4장을 만든다 (figma-template/*.svg).

사용: python3 _context/gen_figma_svgs.py
- 칸 이름·체크리스트는 figma-template/README.md 와 같게 유지한다. README를 고치면 이 파일의 문구도 함께 고친다.
- Figma에 끌어다 놓으면 <g id="…">가 레이어 이름, <text>가 편집 가능한 글자 레이어가 된다.
- 교재 톤 절제형: 흰 바탕 · 회색 선 · 제목과 레인 이름 띠만 다크그린. 색이 아니라 모양과 라벨로 구분한다.
"""
import os
from xml.sax.saxutils import escape

HUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HUB, 'figma-template')

DEEP, ACCENT, LIGHT = '#0f3b2e', '#1d6b50', '#eaf3ee'
LINE, HINT, INK, PAPER = '#c4ccc8', '#7a8580', '#1c1c1e', '#ffffff'
FONT = "'Noto Sans KR', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif"


def tw(s, size):
    """대략적인 글자 폭(px)."""
    return sum(size * (1.0 if ord(c) > 0x2E80 else 0.56) for c in s)


def wrap(s, size, width):
    lines, cur = [], ''
    for word in s.split(' '):
        cand = (cur + ' ' + word).strip()
        if tw(cand, size) <= width or not cur:
            cur = cand
        else:
            lines.append(cur); cur = word
    if cur:
        lines.append(cur)
    return lines


class SVG:
    def __init__(self, w, h, title):
        self.w, self.h, self.parts = w, h, []
        self.parts.append(f'<rect id="바탕" x="0" y="0" width="{w}" height="{h}" fill="{PAPER}"/>')

    def g(self, name, inner):
        self.parts.append(f'<g id="{escape(name)}">' + ''.join(inner) + '</g>')

    @staticmethod
    def rect(x, y, w, h, fill='none', stroke=LINE, sw=2, rx=8, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

    @staticmethod
    def text(x, y, s, size=18, fill=INK, weight=400, anchor='start'):
        # Figma 가져오기용: 크기는 px 단위 style, 글꼴은 Figma 기본 제공 Noto Sans KR 하나, 가운데·끝 정렬은 x를 직접 계산
        if anchor == 'middle':
            x = x - tw(s, size) / 2
        elif anchor == 'end':
            x = x - tw(s, size)
        style = f"font-family:'Noto Sans KR';font-size:{size}px;font-weight:{weight};fill:{fill}"
        return f'<text x="{x:.1f}" y="{y:.1f}" style="{style}">{escape(s)}</text>'

    def texts(self, x, y, s, size, width, fill=INK, weight=400, lh=1.45):
        out = []
        for i, line in enumerate(wrap(s, size, width)):
            out.append(self.text(x, y + i * size * lh, line, size, fill, weight))
        return out, len(wrap(s, size, width))

    def save(self, name):
        body = '\n'.join(self.parts)
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}px" height="{self.h}px" '
               f'viewBox="0 0 {self.w} {self.h}">\n{body}\n</svg>\n')
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
            f.write(svg)


def header(s, title, where, w_left):
    s.g('워크시트 이름', [
        s.text(60, 78, title, 34, DEEP, 700),
        s.text(60, 116, where, 17, HINT),
        s.rect(60, 136, w_left, 4, fill=DEEP, stroke='none', sw=0, rx=2),
    ])


def checklist(s, x, y, w, items, size=17):
    inner = [s.rect(x, y, w, 10, fill=DEEP, stroke='none', sw=0, rx=0)]
    inner.append(s.text(x + 24, y + 48, '완료 기준 체크리스트', 20, DEEP, 700))
    cy = y + 88
    for it in items:
        t, n = s.texts(x + 56, cy, it, size, w - 84)
        inner.append(s.rect(x + 24, cy - size + 1, size, size, fill=PAPER, stroke=INK, sw=1.5, rx=3))
        inner += t
        cy += n * size * 1.45 + 12
    h = cy - y + 8
    inner.insert(0, s.rect(x, y, w, h, fill=PAPER, stroke=LINE, sw=2, rx=0))
    s.g('완료 기준 체크리스트', inner)
    return y + h


def band_label(s, x, y, w, h, label):
    return [s.rect(x, y, w, h, fill=DEEP, stroke='none', sw=0, rx=0),
            s.text(x + w / 2, y + h / 2 + 9, label, 24, PAPER, 700, 'middle')]


# ---------------- 00 표지 ----------------
def cover():
    s = SVG(1400, 900, '표지')
    s.g('표지 제목', [
        s.rect(0, 0, 1400, 14, fill=DEEP, stroke='none', sw=0, rx=0),
        s.text(80, 130, 'AX YOUR BODY · Figma 워크시트', 44, DEEP, 700),
        s.text(80, 180, '웹서비스 UX/UI 기획 교재의 Figma 실습 파일입니다. 페이지 01~03에서 워크시트를 씁니다.', 20, HINT),
        s.rect(80, 210, 1240, 4, fill=DEEP, stroke='none', sw=0, rx=2),
    ])
    y = 290
    for label, hint in [('이름', ''), ('담당 프로필', '예) 정하은 (여성 · 운동인) f-athlete'),
                        ('워크시트 저장소 링크', 'https://github.com/내 아이디/axyourbody-worksheet')]:
        s.g(f'{label} 칸', [s.text(80, y, label, 22, DEEP, 700),
                            s.rect(80, y + 18, 1240, 84, fill=PAPER, stroke=LINE, sw=2),
                            s.text(104, y + 70, hint, 20, HINT)])
        y += 150
    s.g('안내', [s.text(80, 800, '이 파일은 강사만 볼 수 있게 공유하고, 공유 링크를 worksheet.md 맨 위 Figma 링크 칸에 적습니다(교재 부록 A-3).', 18, HINT)])
    s.save('00-cover.svg')


# ---------------- 01 이벤트 보드 ----------------
def event_board():
    W, H = 3400, 1560
    s = SVG(W, H, '이벤트 보드')
    header(s, '고객 여정 위에 사건과 대상 객체를 붙인 이벤트 보드',
           '교재 2.2절(여정 레인) · 2.4절(사건·대상 객체·질문 레인) · 칸 이름 상자는 지우지 말고 잠가 두세요(Lock)', 2360)
    LX, LW, AX, AR = 60, 190, 250, 2420  # lane label x/width, area x/right
    y0 = 190
    # 여정 레인: 단계 상자 6개
    jh = 520
    inner = band_label(s, LX, y0, LW, jh, '여정')
    sw_ = (AR - AX - 20 * 5) / 6
    fields = ['단계 이름', '근거 날짜', '행동', '생각', '감정 (-2~+2 숫자와 낱말)', '접점', '불편 (과업 번호)', '기회']
    for i in range(6):
        x = AX + 10 + i * (sw_ + 20)
        box = [s.rect(x, y0 + 14, sw_, jh - 28, fill=PAPER, stroke=LINE, sw=2)]
        box.append(s.text(x + 18, y0 + 52, f'단계 {i + 1}', 22, DEEP, 700))
        fy = y0 + 92
        for f in fields:
            box.append(s.text(x + 18, fy, f, 15, HINT))
            box.append(f'<line x1="{x + 18}" y1="{fy + 30}" x2="{x + sw_ - 18}" y2="{fy + 30}" stroke="{LINE}" stroke-width="1" stroke-dasharray="4 4"/>')
            fy += 50
        s.g(f'단계 {i + 1}', box)
    inner.append(s.text(AX + 10, y0 + jh + 30, '단계는 4~6개를 시간순으로 씁니다. 남는 상자는 지웁니다. 감정 숫자는 단계 사이를 실선으로 잇습니다.', 16, HINT))
    s.g('여정 레인', inner)
    # 사건·대상 객체·질문 레인
    y = y0 + jh + 56
    for name, h, hint in [('사건', 250, '사건 카드를 여정 단계 아래에 시간순으로 붙입니다. 과거형으로 씁니다. 예) "세트가 기록됨"'),
                          ('대상 객체', 230, '사건 속 명사를 대상 객체 카드로 붙입니다. 같은 대상 객체는 한 장만 둡니다.'),
                          ('질문', 190, '지금 답할 수 없는 것을 질문 카드로 남깁니다.')]:
        s.g(f'{name} 레인', band_label(s, LX, y, LW, h, name) + [
            s.rect(AX + 10, y + 10, AR - AX - 10, h - 20, fill=PAPER, stroke=LINE, sw=2, dash='10 8', rx=6),
            s.text(AX + 34, y + 46, hint, 17, HINT)])
        y += h + 16
    # 오른쪽: 체크리스트 + 카드 견본
    RX, RW = 2480, 860
    cy = checklist(s, RX, 190, RW, [
        '여정 단계를 4~6개 적고 단계마다 근거 날짜를 붙였다',
        '사건을 과거형으로 10개 이상 시간순으로 붙였다',
        '사건마다 등장하는 대상 객체를 대상 객체 레인에 붙였다',
        '대상 객체 레인의 대상 객체를 문서 템플릿의 대상 객체 카드로 옮겼다 (대상 객체 행으로, 또는 다른 대상 객체의 속성으로)'])
    py = cy + 30
    pal = [s.rect(RX, py, RW, H - py - 40, fill=LIGHT, stroke=LINE, sw=2, rx=0),
           s.text(RX + 24, py + 46, '복사해서 쓰는 카드', 22, DEEP, 700),
           s.text(RX + 24, py + 78, 'Mac Option, Windows Alt를 누른 채 끌면 복사됩니다. 종류 라벨은 지우지 않습니다.', 15, HINT)]
    s.g('복사용 카드 영역', pal)

    def tag(x, y, label):
        w = tw(label, 15) + 24
        return [s.rect(x, y, w, 30, fill=DEEP, stroke='none', sw=0, rx=4), s.text(x + w / 2, y + 21, label, 15, PAPER, 700, 'middle')]
    cx, cyy = RX + 40, py + 120
    s.g('사건 카드 견본', [s.rect(cx, cyy, 360, 110, fill=PAPER, stroke=INK, sw=2, rx=6)] + tag(cx + 14, cyy + 14, '사건') +
        [s.text(cx + 18, cyy + 84, '○○가 기록됨', 22, INK)])
    s.g('대상 객체 카드 견본', [s.rect(cx + 410, cyy, 200, 200, fill=PAPER, stroke=INK, sw=4, rx=6)] + tag(cx + 424, cyy + 14, '대상 객체') +
        [s.text(cx + 428, cyy + 120, '대상 객체 이름', 22, INK)])
    qx, qy = cx, cyy + 220
    s.g('질문 카드 견본', [s.rect(qx, qy, 300, 150, fill=PAPER, stroke=INK, sw=2, rx=6, dash='8 6'),
                           f'<path d="M {qx + 236} {qy} L {qx + 294} {qy} Q {qx + 300} {qy} {qx + 300} {qy + 6} L {qx + 300} {qy + 64} Z" fill="{DEEP}"/>',
                           s.text(qx + 284, qy + 30, '?', 24, PAPER, 700, 'middle')] + tag(qx + 14, qy + 14, '질문') +
        [s.text(qx + 18, qy + 100, '아직 모르는 것', 22, INK)])
    s.g('카드 구분 안내', [s.text(cx, qy + 210, '사건 = 가로로 긴 직사각형 · 대상 객체 = 정사각형(굵은 테두리)', 16, HINT),
                          s.text(cx, qy + 240, '질문 = 점선 테두리 + 모서리 "?" · 색 없이도 모양과 라벨로 구분됩니다', 16, HINT)])
    s.save('01-event-board.svg')


# ---------------- 02 화면 흐름 순서표와 화면 목록 ----------------
def table(s, name, x, y, w, cols, widths, rows, first_col=None, row_h=64):
    inner = []
    cx = x
    for c, cw in zip(cols, widths):
        inner += [s.rect(cx, y, cw, 56, fill=DEEP, stroke=PAPER, sw=1, rx=0), s.text(cx + 16, y + 36, c, 18, PAPER, 700)]
        cx += cw
    for r in range(rows):
        cx = x
        for ci, cw in enumerate(widths):
            inner.append(s.rect(cx, y + 56 + r * row_h, cw, row_h, fill=PAPER, stroke=LINE, sw=1.5, rx=0))
            if ci == 0 and first_col and r < len(first_col):
                inner.append(s.text(cx + 16, y + 56 + r * row_h + 40, first_col[r], 18, INK, 700))
            cx += cw
    s.g(name, inner)
    return y + 56 + rows * row_h


def section(s, title, x, y, w):
    return [s.rect(x, y, 8, 34, fill=DEEP, stroke='none', sw=0, rx=0), s.text(x + 22, y + 27, title, 24, DEEP, 700)]


def screen_flow():
    W, H = 1700, 2200
    s = SVG(W, H, '화면 흐름')
    header(s, '과업별 화면 흐름 순서표와 화면 목록', '교재 3.2절 · 다 쓴 글은 3.6절에서 작업 폴더의 context/screen-flow.md로 옮깁니다', 1580)
    cy = checklist(s, 60, 170, 1580, [
        '핵심 과업 1개의 기본 흐름을 처음부터 끝까지 화면 이름으로 이었다',
        '갈림길이 있으면 조건과 함께 적었다',
        '화면마다 목적과 측정 지표 1개를 적었다',
        '상태 화면 4종(빈·오류·로딩·이상치)을 적고, 빈 상태와 이상치에는 근거 데이터를 붙였다',
        '내용을 작업 폴더 context/screen-flow.md로 옮겼다'])
    y = cy + 40
    for title, hint, h in [('핵심 과업', '과업·불편 목록에서 고른 과업 한 문장', 90),
                           ('기본 흐름', '화면 이름 → 화면 이름 → 화면 이름 (글자로 한 줄, 화면 일곱 개 이하)', 90),
                           ('갈림길', '[조건] → 다른 경로 한 줄 (없으면 비움)', 90)]:
        s.g(title, section(s, title, 60, y, 1580) + [s.rect(60, y + 50, 1580, h, fill=PAPER, stroke=LINE, sw=2),
                                                     s.text(84, y + 50 + h / 2 + 7, hint, 18, HINT)])
        y += h + 80
    s.g('화면 목록 제목', section(s, '화면 목록', 60, y, 1580))
    y = table(s, '화면 목록 표', 60, y + 50, 1580, ['화면 이름', '이 화면의 목적', '측정 지표 1개'], [360, 760, 460], 7) + 60
    s.g('상태 화면 목록 제목', section(s, '상태 화면 목록', 60, y, 1580))
    table(s, '상태 화면 목록 표', 60, y + 50, 1580, ['상태', '어느 화면', '근거 데이터', '보여 줄 것'], [220, 360, 460, 540], 4,
          first_col=['빈 상태', '오류', '로딩', '이상치'])
    s.save('02-screen-flow.svg')


# ---------------- 03 시안 비교표 ----------------
def comparison():
    W, H = 2300, 1500
    s = SVG(W, H, '시안 비교표')
    header(s, 'Google Stitch로 만든 테마별 화면 시안 비교표', '교재 3.5절 · 시안 이미지는 시안 화면 칸에 붙여 넣습니다 · 세 기준은 ○ / △ / × + 이유 한 줄', 2180)
    cy = checklist(s, 60, 170, 2180, [
        '테마 2개 이상 × 핵심 화면 2개 이상의 시안을 붙였다',
        '세 기준을 모두 ○/△/×와 이유로 평가했다',
        '테마마다 한 줄 결론을 적었다'])
    y = cy + 40
    cols = ['테마', '시안 화면', '과업 수행 쉬움', '정보 위계', '프로필 적합성', '한 줄 결론']
    widths = [250, 760, 280, 280, 280, 330]
    end = table(s, '비교표', 60, y, 2180, cols, widths, 3, first_col=['테마 1', '테마 2', '테마 3 (선택)'], row_h=300)
    hints = []
    for r in range(3):
        ry = y + 56 + r * 300
        hints.append(s.text(60 + 250 + 20, ry + 160, '화면 이름 2~3개와 시안 이미지', 17, HINT))
        x = 60 + 250 + 760
        for _ in range(3):
            hints.append(s.text(x + 16, ry + 160, '○ / △ / × + 이유', 17, HINT)); x += 280
        hints.append(s.text(x + 16, ry + 160, '첫 프로토타입에 가져갈 점', 17, HINT))
    s.g('칸 안내', hints)
    s.save('03-draft-comparison.svg')


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    cover(); event_board(); screen_flow(); comparison()
    print('saved:', sorted(f for f in os.listdir(OUT) if f.endswith('.svg')))
