#! python
# -*- coding: utf-8 -*-

import discord
import subprocess
from datetime import datetime
from mcrcon import MCRcon


client = discord.Client()

'''
TOKEN(str) : botのトークン
mine_workdir(str) : マイクラのサーバー起動jarがあるディレクトリパス(full path)
server_start_bat(str) : サーバー起動batのファイル名
rcon_hostname(str) : RCONのホスト名
rcon_password(str) : RCONの接続パスワード
rcon_port(int) : RCONのポート番号

'''

TOKEN = 'token'
mine_workdir = r'path'
server_start_bat = 'server_start.bat'
rcon_hostname = 'localhost'
rcon_password = 'test'
rcon_port = 25575


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(activity=discord.Game(name='Say !help'))
    print('Bot started.')
    print('----------------')

@client.event
async def on_message(message):
    if message.author.bot:
        '''
        メッセージを送った人がbotかどうかの判定。
        ここに指定のチャンネルID判定を追加すれば、コマンド実行するテキストチャンネルを限定できる。
        '''
        return

    if message.content.startswith('!test'): # message.content == '!test' とかでもOK
        #通常のテキスト形式で送る場合
        await message.channel.send('テスト')
        '''
        embed形式で送る場合
        ここ使うと便利かも↓
        https://cog-creators.github.io/discord-embed-sandbox/
        '''
        embed = embed=discord.Embed(title='タイトル', description='本文', color=0x22d11f, timestamp=datetime.utcnow())
        embed.set_footer(text="!test command")
        await message.channel.send(embed=embed)
        return

    elif message.content.startswith('!run'):
        '''
        Popenでbatを起動、別コンソールで起動するためstart、cwdで作業ディレクトリを指定
        '''
        subprocess.Popen(['start', server_start_bat], shell=True, cwd=mine_workdir)
        await message.channel.send('サーバーを起動しました。')
        return

    elif message.content.startswith("!stop"):
        '''
        RCONを使用してサーバーを操作、save-all -> stop
        '''
        with MCRcon(rcon_hostname, rcon_password, port=rcon_port) as mcr:
            res = mcr.command('save-all')
            print(res)
            res = mcr.command('stop')
            print(res)
        await message.channel.send('サーバーを停止しました。')
        return

    elif message.content.startswith('!help'):
        await message.channel.send('ヘルプ\n \
                            !run --- サーバー起動\n \
                            !stop --- サーバー停止')
        return


client.run(TOKEN)