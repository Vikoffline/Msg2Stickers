import json
import random
from vkbottle.bot import Bot, Message
import vk_api as VK
import asyncio

with open('config.json', 'r') as confile:
    config = confile
    config = json.load(confile)
    token = config['token']
    ids = config['ids']
    code = config['code']
    shortcuts = config['shortcuts']
    alph = config['alph']
    sep = config['sep']
    
print(token)

bot = Bot(token=token)

@bot.on.message()
async def Msg2Sticks(message: Message):
    myid = str(message.from_id)
    if myid in ids:

        session = VK.VkApi(token=ids[myid], scope=4096)
        vk = session.get_api()
        print('1')
        if message.text[0:len(code)] == code:
            try:
                msgtext = message.text.split(sep)
                id = msgtext[1].strip()
                text = msgtext[2].strip()
                
                id = id.replace('@', '')
                if id in shortcuts:
                    id = shortcuts[id]
                try:
                    int(id)
                except:
                    id = str(vk.users.get(user_id=id)[0]['id'])
                
                try:
                    for chr in text.lower():
                            if chr in alph:
                                vk.messages.send(peer_id=id, random_id='0', sticker_id=alph[chr])
                                await asyncio.sleep(random.randint(1, 2))
                    await message.reply('Готово')
                except VK.Captcha: 
                    await message.answer('О нет, капча. Попробуй попозже')
                except:
                    await message.answer('Стикеры не отправлены, попробуй ещё раз')
                
            except:
                await message.answer(f'Какой-то трабл. Всё правильно написал? {code+sep}ID{sep}Сообщение. Для бесед используй 2000000000 + последние цифры ссылки на беседу')

bot.run_forever()
