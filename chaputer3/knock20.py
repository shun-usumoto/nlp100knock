import json
import gzip


def britain():
    # gzipモジュールを用いてファイルを開く
    with gzip.open("jawiki-country.json.gz", "rt", "utf-8") as data_file:
        # ファイルを1行ずつ読み込む
        for line in data_file:
            # json.loads()を用いてstr型をdict型に変換
            data = json.loads(line)
            if data["title"] == "イギリス":
                return data["text"]


if __name__ == "__main__":
    print(britain())
