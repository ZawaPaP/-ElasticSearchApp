## 概要
"Pythonで作る初めてのElasticSearchアプリケーション" をもとに作成したアプリケーションです。
ElasticSearchとKibanaはDockerで起動しています。

ElasticSearchの基本的な使い方を学ぶために作成しました。


### つかいかた

Dockerをインストールしている前提です。
#### ElasticSearchとKiabanaを起動します。
```
docker compose up -d
```
ボリュームはローカルに保存されます。

#### pipenvをインストールします。
```
pip install pipenv
```


#### データ取得
データは楽天BooksのAPIを用いて取得しています。
.envにAPIキーを設定したのちに以下コマンドでデータを取得できます。
デフォルトでは "Python" というキーワードで検索していますが、変更したい場合はget_books_from_rakuten.pyを編集してください。

```
pipenv run python get_books_from_rakuten.py

```

#### データをElasticSearchに登録
```
pipenv run python register_books_to_elasticsearch.py
```

#### アプリケーションを起動
```
pipenv run python app.py
```
Flaskが起動します。 http://localhost:5000 にアクセスするとアプリケーションが表示されます。