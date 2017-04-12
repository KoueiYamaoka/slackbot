# Slack Bot

とある研究室の Slack で運用されている Bot "shumaikun" です．
Bot の機能は Python で実装されています．  
Python のお勉強をしつつ Slack に有意義な機能を追加していこうというコンセプトです．

## Bot の機能

まだ何も実装されていません．  
また，現在では "shumaikun" が反応するようになっていないワードを DM で受けとると
"Command Not Found." と返してきます．

(機能を実装したら，内容や使い方等をここへ簡単に記載してくれると助かります．)

## Bot の機能開発について

Bot の開発に参加するには，このリポジトリを
[Fork](https://github.com/KoueiYamaoka/slackbot) して下さい．  
以下は基本的な流れになります．
詳しくは「プルリクエスト 作成」とかで検索してみて下さい．

1. ローカルのリポジトリ (`master`) を最新の状態にする．
1. 開発用に branch を作成する．
1. 開発用のブランチでファイルを編集する．
1. コミットを作成し，プルリクエストを送る．

:warning: Bot の機能を書いた Python コードは `plugins/` 中に配置して下さい．

### 【重要】機能をテストする場合

ローカルにあるコードを動作させるには Python3 の slackbot ライブラリが必要です．  
``$ pip install slackbot``

起動は次のコマンドで行います．  
``$ python3 run.py``

Python の slackbot はローカルでテストしようとするとコードの大幅な
書き換えが必要になって大変なので，開発中のテストを行うための Bot である
"*shumaikun_dev*" が Slack のチャンネル "*dev_shumaikun*" にいます．  

また，"*shumaikun_dev*" を起動させるためには，API TOKEN 等を含んだ
`setting_slackbot.py` をリポジトリに配置する必要がありますが，これは
API TOKEN を含むためこのリポジトリにはありません．開発に参加される方に
は Slack 等でコンタクトを頂ければファイルを配布します．

動作確認を行い，正常に動くことを確認してからプルリクエストを送って下さい．

## LICENSE

MIT License

Copyright (c) 2017 Kouei Yamaoka

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
