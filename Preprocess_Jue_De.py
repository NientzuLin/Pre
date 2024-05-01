import re

# 打開檔案讀取内容
with open("jue_de_raw.txt", "r", encoding="utf-8") as file:
    # 讀取文件中每一行資料，將它們存放在lines的列表中
    lines = file.readlines()

# 創建input_list，去掉每行末尾的換行符
input_list = [line.strip() for line in lines]
print(input_list)


# 刪除英文字符
def remove_english(text):
    return re.sub(r'[a-zA-Z]', '', text)


# 刪除特殊字符（保留中文字符、数字和字母）
def remove_special(text):
    return re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', '', text)


# 儲存最終結果的列表
result_sentences = []

# 删除所有輸入行中的英文字符
input_list = [remove_english(line) for line in input_list]

# 刪除所有輸入行中的中文標點符號
input_list = [remove_special(line) for line in input_list]

# 篩選每一個句子
for i in range(len(input_list)):
    line = input_list[i]
    # 如果不是第一行，則取上一行最後五個字符
    before = input_list[i - 1][-5:] if i > 0 else ""
    # 尋找目前行的 "覺得" 的位置
    index = line.find("覺得")
    if index != -1:
        # 提取 "覺得" 前五個字符，并刪去特殊字符
        before += line[max(index - 5, 0):index]
        # 提取 "覺得" 後面的字符（包括中文字符），并删除特殊字符
        after = line[index + len("覺得"):index + len("覺得") + 5]
        # 構建新的句子
        new_sentence = before + "[" + "覺得]" + after
        # 将新句子添加到結果列表中
        result_sentences.append(new_sentence)

# 輸出結果
for sentence in result_sentences:
    print(sentence)
