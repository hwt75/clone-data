# -*- coding: utf-8 -*-
"""Phân tích 'Kinh Dịch Trọn Bộ' (Ngô Tất Tố) -> hào từ đầy đủ cho 64 quẻ.

Chiến lược: neo theo dòng chữ Hán mở đầu mỗi hào (初九/六二/…) vì nhãn tiếng Việt
trong bản số hoá có nhiều lỗi ('Dịch âni', 'Lạc Tứ', 'Lục T'). Dùng tên Hán-Việt
làm phương án dự phòng.
"""
import re, json, unicodedata

LINES = open('ntt.txt', encoding='utf-8').read().split('\n')
BODY_START = 1793

qidx = [i for i, l in enumerate(LINES) if l.startswith('QUẺ ') and i >= BODY_START]
assert len(qidx) == 64
NTT_NAMES = [LINES[i][4:].strip() for i in qidx]
bounds = [(i, qidx[k + 1] if k + 1 < len(qidx) else len(LINES)) for k, i in enumerate(qidx)]

HAN = {'初九': ('Sơ Cửu', 1), '初六': ('Sơ Lục', 1), '九二': ('Cửu Nhị', 2),
       '六二': ('Lục Nhị', 2), '九三': ('Cửu Tam', 3), '六三': ('Lục Tam', 3),
       '九四': ('Cửu Tứ', 4), '六四': ('Lục Tứ', 4), '九五': ('Cửu Ngũ', 5),
       '六五': ('Lục Ngũ', 5), '上九': ('Thượng Cửu', 6), '上六': ('Thượng Lục', 6),
       '用九': ('Dụng Cửu', 7), '用六': ('Dụng Lục', 7)}


def fold(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace('đ', 'd').lower()


CANON = {'so cuu': 1, 'so luc': 1, 'cuu nhi': 2, 'luc nhi': 2, 'cuu tam': 3,
         'luc tam': 3, 'cuu tu': 4, 'luc tu': 4, 'cuu ngu': 5, 'luc ngu': 5,
         'thuong cuu': 6, 'thuong luc': 6, 'dung cuu': 7, 'dung luc': 7}
NAMES6 = {1: ('Sơ Cửu', 'Sơ Lục'), 2: ('Cửu Nhị', 'Lục Nhị'), 3: ('Cửu Tam', 'Lục Tam'),
          4: ('Cửu Tứ', 'Lục Tứ'), 5: ('Cửu Ngũ', 'Lục Ngũ'), 6: ('Thượng Cửu', 'Thượng Lục')}

STOP = re.compile(r'^(GIẢI NGHĨA|LỜI KINH|Truyện của|Bản nghĩa|Bản dịch|Lời bàn|Chú thích|QUẺ )')
# nhãn trong bản số hoá bị hỏng nhiều kiểu: 'Dịch âni', 'Dịchnghĩa', 'Dịch nghũu'
# -> so khớp sau khi bỏ dấu VÀ bỏ khoảng trắng
_flat = lambda s: fold(s).replace(' ', '')
IS_AM = lambda s: _flat(s).startswith('dicha')
IS_NGHIA = lambda s: _flat(s).startswith('dichngh')
STRIP_LABEL = re.compile(r'^\S+\s*\S*\s*[.,]?\s*[-–—]\s*')


def clean(s):
    s = re.sub(r'\[\d+\]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s.rstrip(' .,;')


def strip_hao_name(s):
    """bỏ tiền tố 'Sơ Cửu:' / 'Hào Sáu Tư:' nếu có"""
    m = re.match(r'^(?:Hào\s+)?(\S+\s+\S+?)\s*[::.,;]\s*(.+)$', s)
    if m and re.sub(r'\s+', ' ', fold(m.group(1))) in CANON:
        return m.group(2)
    m = re.match(r'^Hào\s+\S+\s+\S+?\s*[::.,;]\s*(.+)$', s)
    if m:
        return m.group(1)
    # tiền tố tên hào sai chính tả ('Lạc Tứ:' thay cho 'Lục Tứ:'): cắt cụm ngắn
    # đứng trước dấu hai chấm, miễn là không chứa dấu phẩy và ≤ 3 từ
    m = re.match(r'^([^,:：]{1,16})[:：]\s*(.+)$', s)
    if m and len(m.group(1).split()) <= 3:
        return m.group(2)
    return s


def block(seg, k):
    """gom một đoạn nhãn (Dịch âm / Dịch nghĩa) có thể xuống dòng"""
    out = [STRIP_LABEL.sub('', seg[k], count=1)]
    j = k + 1
    while j < len(seg) and seg[j].strip() and not STOP.match(seg[j]) \
            and not IS_AM(seg[j]) and not IS_NGHIA(seg[j]):
        out.append(seg[j])
        j += 1
    return clean(' '.join(x.strip() for x in out)), j


result = {}
for n, (a, b) in enumerate(bounds, 1):
    seg = LINES[a:b]
    haos = {}
    for i, line in enumerate(seg):
        # NFKC: chuẩn hoá bộ thủ Khang Hy (⼆ U+2F06) về chữ Hán thường (二)
        flat = unicodedata.normalize('NFKC', re.sub(r'\s+', '', line))
        key = flat[:2]
        if key not in HAN:
            continue
        ten, ngoi = HAN[key]
        if ngoi in haos:
            continue
        # gom các nhãn ngay sau dòng chữ Hán
        labs, j = [], i + 1
        while j < len(seg) and len(labs) < 2:
            if STOP.match(seg[j]) or (j > i + 4 and not labs):
                break
            if IS_AM(seg[j]) or IS_NGHIA(seg[j]):
                txt, j = block(seg, j)
                labs.append(txt)
            else:
                j += 1
        if not labs:
            continue
        am = strip_hao_name(labs[0])
        nghia = strip_hao_name(labs[1]) if len(labs) > 1 else ''
        haos[ngoi] = {'ten': ten, 'am': am, 'nghia': nghia}

    # dự phòng: neo theo tên Hán-Việt cho ngôi còn thiếu
    if len(set(haos) & set(range(1, 7))) < 6:
        for i, line in enumerate(seg):
            if not IS_AM(line):
                continue
            content = STRIP_LABEL.sub('', line, count=1)
            m = re.match(r'^(\S+\s+\S+?)\s*[::.,;]\s*(.+)$', content)
            if not m:
                continue
            k = re.sub(r'\s+', ' ', fold(m.group(1)))
            if k not in CANON or CANON[k] in haos:
                continue
            ngoi = CANON[k]
            am, j = block(seg, i)
            am = strip_hao_name(am)
            nghia = ''
            while j < len(seg) and not seg[j].strip():   # bỏ qua dòng trống chen giữa
                j += 1
            # nhãn kế tiếp là phần dịch nghĩa, kể cả khi bị ghi nhầm thành 'Dịch âm'
            # (vd quẻ 18 hào 2, dòng 8373 của bản ebook)
            if j < len(seg) and (IS_NGHIA(seg[j]) or IS_AM(seg[j])):
                nghia, _ = block(seg, j)
                nghia = strip_hao_name(nghia)
            haos[ngoi] = {'ten': NAMES6.get(ngoi, ('', ''))[0], 'am': am, 'nghia': nghia}
    result[n] = {'ntt_name': NTT_NAMES[n - 1], 'haos': haos}

# Vá thủ công: quẻ 53 Tiệm hào 2 — bản ebook thiếu cả mốc chữ Hán lẫn tên hào
# (dòng 18977-18979: '鴻漸于磐, 飲食衎衎' không có tiền tố 六二). Nằm giữa Sơ Lục
# và Cửu Tam nên chắc chắn là Lục Nhị; nội dung lấy nguyên văn từ chính bản này.
if 2 not in result[53]['haos']:
    result[53]['haos'][2] = {'ten': 'Lục Nhị',
                             'am': 'Hồng tiệm vu bàn, ẩm thực hãn hãn',
                             'nghia': 'Con sếu tiến chưng tảng đá, ăn uống hơn hớn',
                             'va': True}

tot = sum(len([k for k in v['haos'] if k <= 6]) for v in result.values())
print('Hào từ trích được: %d / 384' % tot)
thieu = [(n, sorted(set(range(1, 7)) - set(k for k in v['haos'] if k <= 6)))
         for n, v in result.items() if len([k for k in v['haos'] if k <= 6]) < 6]
print('Quẻ còn thiếu:', len(thieu))
for n, miss in thieu:
    print('   quẻ %-2d %-12s thiếu ngôi %s' % (n, result[n]['ntt_name'], miss))
trong = [(n, k) for n, v in result.items() for k in v['haos'] if not v['haos'][k]['nghia']]
print('Hào thiếu phần dịch nghĩa:', len(trong), trong[:10])
json.dump(result, open('hao_tu.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
