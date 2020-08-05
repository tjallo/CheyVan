from datetime import datetime

def lg(message):
    time = datetime.now()
    servername = message.guild
    author = message.author
    channel = message.channel
    content = message.content
    f = open(f"messages/{servername}.txt","a+")
    f.write(f'{time}, {author}, {channel}: {message.content}                            | {message}\n')