import requests


response = requests.get("https://raw.githubusercontent.com/Hamza139617/resume_screener_data/main/1.pdf")

file =  open("1.pdf", "wb")

print(response.text)
print(response.content)

file.write(response.content)

file.close()