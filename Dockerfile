# python:3.8の公式 image をベースの image として設定
FROM python:3.10

# pipのアップデート
RUN pip install --upgrade pip

# 作業ディレクトリの設定
WORKDIR /code

# カレントディレクトリにある資産をコンテナ上の指定のディレクトリにコピーする
COPY . .

# pipでrequirements.txtに指定されているパッケージを追加する
RUN pip install -r requirements.txt

# 起動（コンテナのポート8002番で受け付けるように起動する）
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000