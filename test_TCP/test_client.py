import socket

# サーバーとの通信に使うポート番号（サーバーと共有）
PORT = 8080

# クライアント用のソケットを作成
# サーバーの説明を参照
cliesock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ソケットをアドレスに接続する
# サーバーのbind()の説明を参照
cliesock.connect(('192.168.1.136', 8080))

# サーバーにデータを送信する
cliesock.send(b'hello, world!')

# サーバーからデータを受信する
data = cliesock.recv(1024)
print(data)

# ソケットを閉じる
cliesock.close()