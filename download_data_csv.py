from urllib.request import urlopen

url = 'https://stooq.com/q/d/l/?s=^spx&i=d'

local_path = 'data/SPX.csv'
with urlopen(url) as webcontent, open(local_path, 'wb') as local_file:
    spx_content = webcontent.read()
    lines = spx_content.splitlines()
    lines_str = []
    for line in lines:
        lines_str.append(line.decode('utf8'))
    print(lines_str[:2])
    local_file.write(spx_content)
