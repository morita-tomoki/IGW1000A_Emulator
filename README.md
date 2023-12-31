# IGW1000A_Emulator

## YUEI IoTゲートウェイ IGW1000A リアルタイムセンサーデータ収集
このプロジェクトは、YUEIのIoTゲートウェイ IGW1000A から出力されるCSVファイルの形式を再現し、ダミーデータをリアルタイムに生成してCSVファイルに追記するPythonスクリプトです。

## コードファイル: realtime_sensor_data_collection.py
このPythonスクリプトは、以下の主要な機能を持っています。

1. ヘッダー行の列名を指定します。
2. ダミーデータを生成し、指定されたフォルダにCSVファイルとして保存します。
3. リアルタイムデータ生成の間隔を設定し、データを定期的に更新します。
## 使用方法
1. このスクリプトを実行するには、Python 3.x環境が必要です。Pythonがインストールされていない場合は、[Python公式ウェブサイト](https://www.python.org/downloads/)からダウンロードしてインストールしてください。

2. 必要なライブラリをインストールします。スクリプト内で使用されているライブラリは、通常のPythonインストールに含まれていますが、CSVファイルの出力フォルダの作成のためにosライブラリを確認してください。

3. スクリプト内の`base_folder`変数を、CSVファイルを保存したいベースフォルダのパスに設定します。デフォルトでは`"Root"`となっています。

4. リアルタイムデータ生成の間隔を調整したい場合は、`time.sleep(60)`の引数を変更してください。デフォルトでは60秒ごとにデータを生成します。

5. スクリプトを実行します。

`python realtime_sensor_data_collection.py`
1. スクリプトは無限ループ内で動作し、リアルタイムにダミーデータを生成しCSVファイルに追記します。エラーが発生した場合、エラーメッセージが表示されます。
## ダミーデータの生成
このスクリプトは、ランダムなセンサーデータを生成し、CSVファイルに書き込みます。以下のデータが生成されます:

- タイムスタンプ
- デバイスID
- デバイス名
- ラベル1
- ラベル2
- デバイスタイプ
- プロトコル
- デバイス固有ID
- センサータイプ
- センサーモデル
- 温度
- 湿度
- 明るさ
- 加速度情報
- 加速度X
- 加速度Y
- 加速度Z
- 開閉情報(磁気センサ)

これにより、YUEIのIoTゲートウェイ IGW1000A が出力するCSVデータと同様のフォーマットでダミーデータが生成されます。


## 出力されるデータの階層
生成したデータは `base_folder` で指定した出力先（ルートフォルダ）に保存されます。以下は、データの保存階層を表します：
```markdown
Root
└── 2020
    └── 07
        └── 21
            └── TempHumAccill_1_2020-07-21-10.csv
```
この階層に従って、生成されたCSVデータが年、月、日ごとにフォルダに保存されます。各ファイル名にはタイムスタンプとIoTゲートウェイのデバイスIDが含まれ、データの一意性を保証します。

## 意事項
- このスクリプトはダミーデータを生成し、実際のデバイスからのデータを収集しません。実際のデータを収集するためには、IGW1000Aデバイスを使用し、適切なインターフェースを設定する必要があります。

- ダミーデータはランダムに生成されるため、実際のセンサーデータとは無関係です。実際のプロジェクトでは、センサーデータを正確に収集および処理するための適切なセンサーおよびインターフェースを使用する必要があります。

- スクリプトの実行中にエラーが発生した場合、エラーメッセージが表示されます。エラーが解決しない場合、適切な対処が必要です。

このREADME.MDファイルに記載されている情報に従って、YUEIのIoTゲートウェイ IGW1000A からのCSVデータを再現するPythonスクリプトを使用して、ダミーデータを生成および収集する準備ができます。