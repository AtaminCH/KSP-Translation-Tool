import csv
import sys

print('Start')
# SimpleTranslator.csvを辞書に格納する
if sys.argv[1] == 'excel':
    with open('SimpleTranslator.csv') as csv_file:
        reader = csv.reader(csv_file)
        # キーに原文、値に翻訳文を入れる
        dictionary = {row[1]: row[0] for row in reader}
else:
    with open('SimpleTranslator.csv', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        # キーに原文、値に翻訳文を入れる
        dictionary = {row[1]: row[0] for row in reader}

# file.txtを読み込んで、英語のテキストを日本語のテキストに置き換える
with open('file.txt', encoding="utf-8") as file, open('deepl_jp.txt', 'w', encoding="utf-8") as output_file:
    for source_line in file:
        for source_text, jp_text in dictionary.items():
            # file.txtとSimpleTranslator.csvの原文が一致
            if source_text in source_line:
                # R\n\nは無視する
                if jp_text != 'R\n\n':
                    # 英語を日本語に置き換える
                    jp_data = source_line.replace(' = ' + source_text + '\n', ' = ' + jp_text + '\n')
                    break
        # 出力ファイルにキーと翻訳済みの値を出力する
        if sys.argv[1] == 'excel':
            output_file.write(jp_data[:-2])  # Excel
        else:
            output_file.write(jp_data)  # Googleスプレッドシート
print('Completed')
