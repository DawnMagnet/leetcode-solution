#!/usr/bin/env python3
import glob, os
from collections import defaultdict
md_list = []
for file_name in glob.glob("src/*/*/*.md"):
    if not "SUMMARY" in file_name:
        md_list.append(file_name)

md_dict = defaultdict(lambda: defaultdict(list))
for item in md_list:
    per = item.split('/')[1:]
    assert len(per) == 3
    md_dict[int(per[0])][int(per[1])].append(per[2])
md_dict = {t:dict(md_dict[t]) for t in md_dict}
res = ""
create_or_clean = lambda path : open("./src/" + path, 'w').close()
for year in sorted(md_dict.keys(), reverse=True):
    res += f'- [{year}年](./{year}/SUMMARY.md)\n'
    create_or_clean(f'./{year}/SUMMARY.md')
    for month in sorted(md_dict[year].keys(), reverse=True):
        res += f'    - [{month}月](./{year}/{month}/SUMMARY.md)\n'
        create_or_clean(f'./{year}/{month}/SUMMARY.md')
        for md_file_name in sorted(md_dict[year][month], key=lambda x: -int(x.split('-')[0])):
            day = int(md_file_name.split('-')[0])
            fully_name = f'./{year}/{month}/{md_file_name}'
            with open("./src/" + fully_name, 'r') as f:
                t = f.readlines()[0][2:]
                pos = t.find(' ')
                t = t[pos:-1]
            res += f'        - [{day}日 - {t}]({fully_name})\n'
# print(res)
with open('./src/SUMMARY.md') as f:
    fs = f.read()
pos = fs.find('年')
fs = fs[:pos]
while fs[-1] != '\n':
    fs = fs[:-1]

fs += res
# print(fs)
with open('./src/SUMMARY.md', 'w') as f:
    f.write(fs)
print("DONE!")