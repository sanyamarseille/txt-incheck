#!/usr/bin/env python3
#coding:UTF-8

import os

# FILE1にFILE2の文字列が含まれているかどうか
# チェックするスクリプト

FILE1 = ''
FILE2 = ''

# withを使うとそのブロック終了時にファイルが閉じられる
# 明示的に.close()を宣言するより楽（書き忘れたときの保険になる）

# チェック対象となるリストを読み込む
with open(FILE2) as f2:
    line2 = f2.readline()

    while line2:
        # 比較するリストを読み込む
        with open(FILE1) as f1:
            line1 = f1.readline()

            while line1:
                # 読み込んだ行が同一か
                if line1 == line2:
                    # 改行コードを削除して標準出力
                    print(line2.rstrip(os.linesep) + ' in FILE1 List')
                line1 = f1.readline()
    
        line2 = f2.readline()
