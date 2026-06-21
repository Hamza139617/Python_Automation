import os

folder = "automationProject"

iterator = 1

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".pdf"):
        os.rename(filename, f"{iterator}.pdf")
        iterator += 1




