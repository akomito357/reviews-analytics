data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料。')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('每一筆留言的平均長度是', sum_len/len(data))

# 篩選長度小於100的留言
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
# 以上已經做好篩選
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

# 篩選有提到good的留言
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言包含good')


print(data[0])

# 文字記數
wc = {} # word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增新的key進入wc字典

for word in wc: #這邊的word表示字典內的key（左邊）
    if wc[word] > 1000000:
        print(word, wc[word])
print('留言裡共有', len(wc), '種單字')

while True:
    word = input('請問你想查什麼字：')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為：', wc[word])
    else:
        print('這個字沒有出現過喔！')

print('感謝使用本查詢功能')


