# Twelve 
前回うpしたリポジトリの大幅改良版です。

# 注意
文字の出力しか出来ないのは前回と同じです。

# 改良点
①ライブラリをLarkからANTLRに変更
②ANTLRで再実装したため大幅なバグ修正

以上の２つが主な改良点です。

# スクリプトファイル
srcフォルダの中に入ってます
「.12」拡張子以外で実行すると弾き飛ばされます。

# EXEファイル
distフォルダの中に入ってます。
また、srcフォルダ内の「main.py」からも実行可能です。

# 実行方法
# Pythonファイルから実行する場合
------------------------
python main.py <ファイル名>.12
------------------------
# main.pyから実行する場合
------------------------
./twelve <ファイル名>.12

# サンプルコード
------------------------
printl "Hello, World!";
------------------------
