print('Start')
# dictionary.cfgのキーをjp_keyに格納する
jp_key = set()
with open("dictionary.cfg", "r", encoding="utf-8") as jp_file:
    # 1行づつデータを読み込む
    for jp_line in jp_file:
        if "=" in jp_line:
            # キーと値がある場合実行
            key, _ = jp_line.split("=", 1)
            jp_key.add(key.strip())

# 未翻訳の内容を出力する
with open("epic.cfg", "r", encoding="utf-8") as epic_file:
    # 1行づつデータを読み込む
    for epic_line in epic_file:
        if "=" in epic_line:
            # キーと値がある場合実行
            key, value = epic_line.split("=", 1)
            key = key.strip()
            value = value.strip()
            if key not in jp_key:
                # jp_keyにキーがなかった場合実行
                with open('deepl.txt', 'a', encoding='utf-8') as file:
                    file.write(value + "\n")
                with open('file.txt', 'a', encoding='utf-8') as file:
                    file.write(epic_line)
print('Completed')
