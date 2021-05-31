from jinja2 import Template

import glob

files = sorted(glob.glob("*.mp3"))
for i in range(len(files)):
    files[i] = f'<tr><th>{files[i][:-4]}</th>' \
               f'<th>' \
               f'<audio controls>' \
               f'<source src="{files[i]}" type="audio/mpeg">' \
               f'</audio>' \
               f'</th>' \
               f'</tr>' \

html = open('hryak_fm_shabl.html').read()
t = Template(html)
m3 = t.render(list_of_files=files)
print(m3)
f = open('jinja_play_rez.html', 'w')
f.write(m3)
f.close()