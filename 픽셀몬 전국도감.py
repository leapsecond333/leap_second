import requests

headers = \
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


url = 'https://hungry0123.tistory.com/74'
site = requests.get(url, headers=headers)

data_count = site.text


pos9 = data_count.find('<table style="margin:auto;">')+len('<table style="margin:auto;">')
data_count = data_count[pos9:]

pos10 = data_count.find('</table>')
extract_data_count = data_count[: pos10]

data_count = data_count[pos10+1:]




for i in range(1, 899, 1):

    pos9 = data_count.find('<table style="margin:auto;">')+len('<table style="margin:auto;">')
    data_count = data_count[pos9:]

    pos10 = data_count.find('</table>')
    extract_data_count = data_count[: pos10]

    data_count = data_count[pos10+1:]


poke_name = site.text
scissors_data = site.text
spawn_time = site.text
spawn_biome = site.text
    biome_count = extract_data_count.count('#FFFFFF;">')
poke_rarity = site.text

# 이름
    pos1 = poke_name.find('margin-bottom:10px;">')+len('margin-bottom:10px;">')
    poke_name = poke_name[pos1:]

    pos2 = poke_name.find('</td>')
    extract_poke_name = poke_name[: pos2]

    print(i, extract_poke_name)
# 시간 텍스트
    for j in range(1):
        pos3 = scissors_data.find('<div  style="min-width: 100px;"></div>')+len('<div  style="min-width: 100px;"></div>')
        scissors_data = scissors_data[pos3:]

        pos4 = scissors_data.find('</td>')
        extract_scissors_data = scissors_data[: pos4]


        scissors_data = scissors_data[pos4+1:]

# 시간
    pos5 = scissors_data.find('<td>')+len('<td>')
    scissors_data = scissors_data[pos5:]

    pos6 = scissors_data.find('</td>')
    extract_spawn_time = scissors_data[: pos6]

    print(extract_spawn_time, '\n')
    
# 위치
    for k in range(biome_count):
        pos7 = spawn_biome.find('#FFFFFF;">')+len('#FFFFFF;">')
        spawn_biome = spawn_biome[pos7:]

        pos8 = spawn_biome.find('</td></tr>')
        extract_spawn_biome = spawn_biome[: pos8]
        spawn_biome = spawn_biome[pos8+1:]

        print(extract_spawn_biome, '\n')

# 희귀도
    pos11 = poke_rarity.find('sans-serif; font-weight:')+len('sans-serif; font-weight: 900; margin:auto">')
    poke_rarity = poke_rarity[pos11:]

    pos12 = poke_rarity.find('</td>')
    extract_poke_rarity = poke_rarity[: pos12]

    print(extract_poke_rarity, '\n')


    poke_name = poke_name[pos2+1:]
    spawn_time = spawn_time[pos6+1:]
    poke_rarity = poke_rarity[pos12+1:]
