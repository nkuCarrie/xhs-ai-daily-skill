#!/usr/bin/env python3
import re,sys
from pathlib import Path
p=Path(__file__).parents[1]/'SKILL.md'
s=p.read_text()
assert s.startswith('---\n')
fm=s.split('---\n',2)[1]
for key in ('name','description','version','license'):
    assert re.search(rf'^{key}:',fm,re.M), f'missing {key}'
name=re.search(r'^name:\s*(.+)$',fm,re.M).group(1).strip()
assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name), name
assert len(name)<=64
assert len(re.search(r'^description:\s*(.+)$',fm,re.M).group(1))<=1024
print('OK',name)
