
from telethon import TelegramClient as tc, events
from Examples import *


test = 858692387
manager_id = 1570183346
api_hash = 'd7d8741f123a7c0ab2394870464c1794'
api_id = 3878059

client = tc('Easy', api_id, api_hash)

client.start(phone='79035886781',password='newnew')
@client.on(event=events.NewMessage())
async def answer(e):
    try:
        id = e.message.id
        command = e.message.message
        to_id = e.message.peer_id.user_id
        from_id = e.message.from_id.user_id

        pos = await client.get_messages(from_id, limit=1)
        pos = pos.total-1

        if pos == 1 and from_id != test:
                await client.send_message(from_id, message=hello())

        if from_id == test:

            command1 = ['гарант']
            command2 = ['даты', 'дата']
            command3 = ['незадним']
            command4 = ['доставка', 'дост', 'доставить']
            command5 = ['волнение']
            command6 = ['предоплата']
            command7 = ['сроки']
            command8 = ['опт', 'скидки']

            if command in command1:
                await client.delete_messages(entity=to_id, message_ids=id)
                await client.send_message(entity=to_id, message=comment(), parse_mode='Markdown')

            if command in command2:
                await client.delete_messages(entity=to_id, message_ids=id)
                await client.send_message(entity=to_id, message=dates())

            if command in command3:
                await client.delete_messages(entity=to_id, message_ids=id)
                await client.send_message(entity=to_id, message=actual())

            if command in command4:
                await client.delete_messages(entity=to_id, message_ids=id)
                await client.send_message(entity=to_id, message=delivery())

            if command in command5:
                await client.delete_messages(entity=to_id, message_ids=id)
                await client.send_message(entity=to_id, message=calm_down(), parse_mode='Markdown')

            if command in command6:
                await client.delete_messages(entity=to_id, message_ids=id)
                await client.send_message(entity=to_id, message=payments())

            if command in command7:
                await client.delete_messages(entity=to_id, message_ids=id)
                await client.send_message(entity=to_id, message=time())

            if command in command8:
                await client.delete_messages(entity=to_id, message_ids=id)
                await client.send_message(entity=to_id, message=sales())

    except Exception as e:
        print(e)

client.run_until_disconnected()