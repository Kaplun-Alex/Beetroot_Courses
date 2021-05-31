import glob
import os


def get_m3u(name_of_file='temp.m3u'):
    files = glob.glob('./*.mp3')
    print(files)
    f = open(name_of_file, 'w')
    f.write(f'#EXTM3U\n')
    for j in range(len(files)):
        f.write(f'#EXTINF:{j},{files[j][2:-4]}\n{os.path.abspath(files[j][2:])}\n\n')
    f.close()
    return name_of_file


def mp3_to_html(name):
    head = '<!DOCTYPE html>\n' \
           '<html>\n' \
           '<head>\n' \
           '<meta charset="UTF-8">\n' \
           '<style>\n' \
           'table {\n' \
           'font-family: arial, sans-serif;\n' \
           'border-collapse: collapse;\n' \
           'width: 100%;\n' \
           '}\n' \
           'td, th {\n' \
           'border: 1px solid #dddddd;\n' \
           'text-align: left;\n' \
           'padding: 8px;}\n' \
           'tr:nth-child(even) {\n' \
           'background-color: #dddddd;\n' \
           '}\n' \
           '</style>\n' \
           '</head>\n' \
           '<body>\n' \
           '<h2>HRYAK FM</h2>\n' \
           '<table>\n' \
           '<tr>\n' \
           '<th>SONG</th>\n' \
           '<th>PLAY</th>\n' \
           '</tr>\n'
    legs = '</table>\n' \
           '</body>\n' \
           '</html>\n'

    list_of_links = glob.glob('./*.mp3')
    dirs_of_files = [os.path.abspath(list_of_links[i][2:]) for i in range(len(list_of_links))]
    print(dirs_of_files)
    f = open(name, 'w')
    f.write(head)
    for i in range(len(dirs_of_files)):
        f.write(f"<tr>\n <th>{list_of_links[i][2:-4]}</th>\n <th>\n<audio controls>\n<source src='{list_of_links[i][2:]}' type='audio/mpeg'>\n</audio>\n</th>\n </tr>\n")
    f.write(legs)
    f.close()


get_m3u('alex.m3u') # в файл
mp3_to_html('hryak.html') # локалхост проигрыватель

