# Minecraft-controller-for-discord
マイクラのサーバー起動・停止を操作するbot
# Requirement
* python 3.8.5
* discord.py 1.6.0
* mcrcon 0.6.0

# Installation
package install
```bash
pip install -r requirements.txt
```

# Usage
Minecraft Serverの `server.properties` で以下を修正。  
```
enable-rcon=true
rcon.port=25575
rcon.password=password
```

`main.py` を環境に合わせて修正。
|constant|type|overview|
|:--|:--|:--|
|TOKEN|str|botのトークン|
|mine_workdir|str|マイクラのサーバー起動jarがあるディレクトリパス(full path)|
|server_start_bat|str|サーバー起動batのファイル名|
|rcon_hostname|str|RCON接続ホスト名|
|rcon_password|str|RCON接続パスワード|
|rcon_port|int|RCON接続ポート番号|

# Note
雑に実装してるので、拡張性はあまりない。許して  
サーバー起動batの参考
```bash
java -Xmx1024M -Xms1024M -jar minecraft_server.1.17.jar nogui
exit
```
`exit` を入れておくことで、サーバー停止後にウィンドウが勝手に落ちてくれる。
