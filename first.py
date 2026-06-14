#!/usr/bin/env python3
import yagmail 

bot = yagmail.SMTP("hamza139617@gmail.com", "ckon kvaj zunc yghc")

bot.send(
    to="orwellian1396@gmail.com",
    subject="nothing",
    contents="this is the content"
)

bot.close()