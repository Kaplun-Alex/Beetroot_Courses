import glob
import os

print("Content-type: text/html")
print()
print()

print('''
<!DOCTYPE html>'
<html>
<head>
<meta charset="UTF-8">
<style>
table {
font-family: arial, sans-serif;
border-collapse: collapse;
width: 100%;
}
td, th {
border: 1px solid #dddddd;
text-align: left;
padding: 8px;}
tr:nth-child(even) {
background-color: #dddddd;
}
</style>
</head>
<body>
<h2>HRYAK FM</h2>
<table>
<tr>
<th>SONG</th>
<th>PLAY</th>
</tr>
''')

list_of_links = glob.glob('E://Python_Projects//Beetroot_Courses_Homework//2021_05_26_SQL_to_HTML/*.mp3')
dirs_of_files = [os.path.abspath(list_of_links[i][2:]) for i in range(len(list_of_links))]
#print(f'<h2>{dirs_of_files}</h2>')
for i in range(len(dirs_of_files)):
    print(f"<tr>\n <th>{list_of_links[i][:-4]}</th>\n <th>\n<audio controls>\n<source src='{list_of_links[i]}' type='audio/mpeg'>\n</audio>\n</th>\n </tr>\n")

print('''
</table>
</body>
</html>
''')





