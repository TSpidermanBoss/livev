  
from pyrogram import Client, Filters, Emoji
import random
import time
app = Client("session",bot_token="663574960:AAGWg1VGruCPuckHzjbpDLRIbPWkX6YcDlc",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b")  


@app.on_message(Filters.command('bowl'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
    if len(message.text.split(' ')) > 1:
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
      q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
      time.sleep(2)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      if a.text == "Ball 0.1🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.1🎾: 🙆‍♂ Wide Ball 🙆‍♂":
        a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
        q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
        z = random.choice(["🅾 Dot Ball 🅾"])
        r = random.choice([x,z,x,z,y,x])
        if a.text == "Ball 0.1🎾: no ball" or a.text == "Ball 0.1🎾: wide ball":
          a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
          q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
          time.sleep(2)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
          z = random.choice(["🅾 Dot Ball 🅾"])
          r = random.choice([x,z,x,z,y,x])
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
      q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
      time.sleep(2)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      if a.text == "Ball 0.1🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.1🎾: 🙆‍♂ Wide Ball 🙆‍♂":
        a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
        q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
        z = random.choice(["🅾 Dot Ball 🅾"])
        r = random.choice([x,z,x,z,y,x])
        if a.text == "Ball 0.1🎾: no ball" or a.text == "Ball 0.1🎾: wide ball":
          a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
          q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
          time.sleep(2)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
          z = random.choice(["🅾 Dot Ball 🅾"])
          r = random.choice([x,z,x,z,y,x])
       x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
      q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
      time.sleep(2)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      if a.text == "Ball 0.1🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.1🎾: 🙆‍♂ Wide Ball 🙆‍♂":
        a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
        q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
        z = random.choice(["🅾 Dot Ball 🅾"])
        r = random.choice([x,z,x,z,y,x])
        if a.text == "Ball 0.1🎾: no ball" or a.text == "Ball 0.1🎾: wide ball":
          a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
          q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
          time.sleep(2)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
          z = random.choice(["🅾 Dot Ball 🅾"])
          r = random.choice([x,z,x,z,y,x])
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
      q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
      time.sleep(2)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      if a.text == "Ball 0.1🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.1🎾: 🙆‍♂ Wide Ball 🙆‍♂":
        a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
        q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
        z = random.choice(["🅾 Dot Ball 🅾"])
        r = random.choice([x,z,x,z,y,x])
        if a.text == "Ball 0.1🎾: no ball" or a.text == "Ball 0.1🎾: wide ball":
          a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
          q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
          time.sleep(2)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
          z = random.choice(["🅾 Dot Ball 🅾"])
          r = random.choice([x,z,x,z,y,x])
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
      q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
      time.sleep(2)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      if a.text == "Ball 0.1🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.1🎾: 🙆‍♂ Wide Ball 🙆‍♂":
        a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
        q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
        z = random.choice(["🅾 Dot Ball 🅾"])
        r = random.choice([x,z,x,z,y,x])
        if a.text == "Ball 0.1🎾: no ball" or a.text == "Ball 0.1🎾: wide ball":
          a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
          q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
          time.sleep(2)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
          z = random.choice(["🅾 Dot Ball 🅾"])
          r = random.choice([x,z,x,z,y,x])
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
      q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
      time.sleep(2)
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      if a.text == "Ball 0.1🎾: 🙅‍♂ No Ball 🙅‍♂" or a.text == "Ball 0.1🎾: 🙆‍♂ Wide Ball 🙆‍♂":
        a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
        q = float(q) + float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
        x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
        y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
        z = random.choice(["🅾 Dot Ball 🅾"])
        r = random.choice([x,z,x,z,y,x])
        if a.text == "Ball 0.1🎾: no ball" or a.text == "Ball 0.1🎾: wide ball":
          a = message.reply("Ball 0.1🎾: " + "** " + r + " **")
          q = float(r.replace("🚾 Run out 🚾","0.1").replace("🚾 Catch out 🚾","0.1").replace("🚾 Wicket 🚾","0.1").replace("🅾 Dot Ball 🅾","0").replace("🙅‍♂ No Ball 🙅‍♂","1").replace("🙆‍♂ Wide Ball 🙆‍♂","1"))
          time.sleep(2)
          x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
          y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
          z = random.choice(["🅾 Dot Ball 🅾"])
          r = random.choice([x,z,x,z,y,x])
      message.reply("**" + message.text.split(' ')[1] + " OVER " + str(q).replace('.','/') + "**")
    else:
      message.reply('Please write ball number after command!')


@app.on_message(Filters. command('leavechat'))
def ran(client,message):
 if message.from_user.id == 312525402:
  if len(message.text.split( )) > 1:
    client.leave_chat(int(message.text.split(' ')[1]))
  else:
    client.leave_chat(message.chat.id)
@app.on_message(Filters. command('cnnn'))
def ran(client,message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
  with open("sure.txt","w") as file:
   file.write("no")
   file.close()
   message.reply("Success off")
app.run()