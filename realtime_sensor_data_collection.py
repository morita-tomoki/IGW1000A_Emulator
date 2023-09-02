import os
import csv
import random
import time
from datetime import datetime

# ヘッダー行の列名
header = ["タイムスタンプ", "デバイスID", "デバイス名", "ラベル1", "ラベル2", "デバイスタイプ", "プロトコル", "デバイス固有ID",
          "センサータイプ", "センサーモデル", "温度", "湿度", "明るさ", "加速度情報", "加速度X", "加速度Y", "加速度Z", "開閉情報"]


# ダミーデータをリアルタイムに生成してCSVファイルに追記する関数
def append_realtime_data(base_folder, device_id, device_name):
    # 現在の日付を取得
    current_datetime = datetime.now()
    year = current_datetime.strftime('%Y')
    month = current_datetime.strftime('%m')
    day = current_datetime.strftime('%d')

    # フォルダのパスを生成
    folder_path = os.path.join(base_folder, year, month, day)

    # フォルダが存在しない場合は、作成する
    os.makedirs(folder_path, exist_ok=True)

    # CSVファイルのパスを生成
    csv_filename = f"TempHumXYZAccIllSensor_1_{current_datetime.strftime('%Y-%m-%d-%H')}.csv"
    csv_file_path = os.path.join(folder_path, csv_filename)

    with open(csv_file_path, mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        label1 = "YTC"
        label2 = ""
        device_type = "sensor"
        protocol = "enocean"
        device_specific_id = "d2"
        sensor_type = "14"
        sensor_model = "41"
        temperature = round(random.uniform(20, 25), 2)  # ランダムな温度を生成 (20から25の範囲)
        humidity = round(random.uniform(50, 60), 2)  # ランダムな湿度を生成 (50から60の範囲)
        brightness = round(random.uniform(0, 100), 2)  # ランダムな明るさを生成 (0から100の範囲)
        acceleration_status = "0"  # 加速度情報 (0:閾値超過なし, 1:閾値1を超過, 2:閾値2を超過)
        acceleration_x = round(random.uniform(-1.05, -1.025), 3)  # ランダムな加速度Xを生成 (-1.05から-1.025の範囲)
        acceleration_y = round(random.uniform(-0.075, -0.044), 3)  # ランダムな加速度Yを生成 (-0.075から-0.044の範囲)
        acceleration_z = round(random.uniform(0, 0.024), 3)  # ランダムな加速度Zを生成 (0から0.024の範囲)
        contact = "0"  # 開閉情報

        # 現在のエポックミリ秒を取得
        timestamp = int(time.time() * 1000)

        # ダブルクォーテーションで値を囲む
        row_data = [timestamp, device_id, device_name, label1, label2, device_type, protocol, device_specific_id,
                    sensor_type, sensor_model, temperature, humidity, brightness, acceleration_status,
                    acceleration_x, acceleration_y, acceleration_z, contact]

        csv_writer.writerow(row_data)


def main():
    base_folder = "Root"    # ベースフォルダを設定

    while True:
        for i in range(1, 13):  # 1から12までのセンサーを作成
            device_id = i
            device_name = f"Multi_Sensor_{i}"
            try:
                # リアルタイムデータ生成の間隔（秒）を指定してデータを追記
                append_realtime_data(base_folder, device_id, device_name)
                current_datetime = datetime.now()
                print(f"センサー {device_id} データを更新しました。{current_datetime.strftime('%Y-%m-%d-%H-%M')}")
            
            except Exception as e:
                print(f"センサー {device_id} でエラーが発生しました: {str(e)}")

        # 60秒ごとにデータを生成
        time.sleep(60)

if __name__ == "__main__":
    main()