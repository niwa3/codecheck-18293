def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    if len(argv) != 3:
        print(-1)
        return 0
    for i, v in enumerate(argv):
        if v.isdigit() is False:
            print(-1)
            return 0
