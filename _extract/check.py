# -*- coding: utf-8 -*-
import os, re, collections

W = r'D:\claude\claude-source\wiki'

targets = set()
files = []
for root, dirs, fs in os.walk(W):
    for f in fs:
        if f.endswith('.md'):
            p = os.path.join(root, f)
            files.append(p)
            stem = f[:-3]
            targets.add(stem.lower())
            txt = open(p, encoding='utf-8').read()
            m = re.match(r'^---\n(.*?)\n---\n', txt, re.S)
            if m:
                for al in re.findall(r'^\s*-\s*"?(.+?)"?\s*$', m.group(1), re.M):
                    if al and not al.startswith('kinh-dịch') and ':' not in al:
                        targets.add(al.lower())

bad = collections.Counter()
where = {}
for p in files:
    txt = open(p, encoding='utf-8').read()
    for link in re.findall(r'\[\[([^\]\|#]+)(?:\|[^\]]*)?\]\]', txt):
        t = link.strip().replace('\\', '')
        if t.lower() not in targets:
            bad[t] += 1
            where.setdefault(t, os.path.basename(p))

print('Tổng số file :', len(files))
print('Tổng target  :', len(targets))
print('Link hỏng    :', len(bad))
for t, c in bad.most_common():
    print('  x%-3d %-45s  (vd: %s)' % (c, t, where[t]))
