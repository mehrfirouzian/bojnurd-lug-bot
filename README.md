# bojnurd-lug-bot
از اون جایی که لاگ متعلق به یک فرد خاص نیست پس باید همه برای امکانات ربات تصمیم بگیرند. پس هر قابلیت بات پس از مورد قبول واقع شدن توسط اعضا به ربات اضافه خواهد شد.

# what I need?
python3-pip - it may installed already, if so you don't have it: <code> #sudo apt install python3-pip </code>
python-telegram package - install it by <code> #pip3 install python-telegram-bot </code>

# How to run it?
then, simply make a .py file in project directory, then put these in the file

<pre>
from bot import Bot
bot = Bot(token='**bot token(gather it from t.me/botfather)**', chat_id=**group chat_id(ask a specialist for this)**)
bot.run()</pre>

and then run it by: 
<code>python3 file_name.py</code>
