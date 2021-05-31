from mako.template import Template

import glob

filez = sorted(glob.glob("*.mp3"))
for i in range(len(filez)):
    filez[i] = f'<li> <a href="{str(filez[i])}">{str(filez[i])}</a> </li>'
t = Template(filename='temp.html')
m3 = t.render(list_of_files=filez)
print(m3)
f = open('play.html', 'w')
f.write(m3)
f.close()
