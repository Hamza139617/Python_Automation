from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from google import genai
import asyncio
import edge_tts
import random
from moviepy import ImageClip, AudioClip, concatenate_videoclips, AudioFileClip
import os
import re


def getImages():

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(
            viewport={"width":1280, "height":720},
            locale="en-US"
        )

        page = context.new_page()

        url1 = "https://artvee.com/s_collection/1246631/" #plage
        url2 = "https://artvee.com/s_collection/369851/" #landscape
        url3 = "https://artvee.com/main/?s=battle" #battle
        

        

        page.goto(url1, wait_until="load")

        
        for i in range(0, 4):
            num = random.randint(0,19)
            item = page.locator("header.entry-header").nth(num)
            item.locator("img").click()

            with page.expect_download() as download_info:
                page.wait_for_timeout(2000)
                page.get_by_text("Download", exact=True).nth(0).click()

            download = download_info.value

            download.save_as(f"image{i}.jpg")

            page.get_by_title("close").click()

        page.close()

        page = context.new_page()

        page.goto(url2, wait_until="load")

        for i in range(4, 10):
            num = random.randint(0,19)
            item = page.locator("header.entry-header").nth(num)
            item.locator("img").click()

            with page.expect_download() as download_info:
                if(i == 4):
                    page.wait_for_timeout(4000)
                else:
                    page.wait_for_timeout(2000)
    
                page.get_by_text("Download", exact=True).nth(0).click()

            download = download_info.value

            download.save_as(f"image{i}.jpg")

            page.get_by_title("close").click()

        page.close()

        page = context.new_page()

        page.goto(url3, wait_until="load")

        for i in range(10, 18):

            num = random.randint(0, 19)

            page.locator("img.lazy").nth(num).click()

            with page.expect_download() as download_info:
                if(i == 10 ):
                    page.wait_for_timeout(4000)
                else:
                    page.wait_for_timeout(2000)
    
                page.get_by_text("Download", exact=True).nth(0).click()
                
            download = download_info.value

            download.save_as(f"image{i}.jpg")

            page.get_by_title("close").click()




        
        




def prepareScript():
    client = genai.Client(api_key="Paste_Your_Gemini_Api_Over_Here")


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=(
            "Act as a charasmatic philospher who is an expert in explaining philosophy and is famous for his one lines and dialogues",
            "Objective: I want you to write a script for my youtube video which and the script must contain more than 3500 characters and less than 4000 characters."
            "Audience: You are preparing this script for an audience who are interested in philosophy and expose` content"
            "Output Format (Strict): The output should be directly the script without any instructions "
            "NOTE: Write the script as spoken narration only. Do not include any stage directions, scene descriptions, camera instructions, facial expressions, gestures, pauses, sound effects, or formatting inside parentheses or brackets. Output only the exact words that the speaker says, as if they were reading from a teleprompter."
        )
    )

    result = (response.text).split()
    print(response.text)
    return response.text
    





async def generate_audio(script, filename="tt.mp3"):
    voice = "en-US-GuyNeural"  
    communicate = edge_tts.Communicate(script, voice)
    await communicate.save(filename)





def prepareVoice(script = "someting"):
    asyncio.run(generate_audio(script))
    print("Audio saved as tt.mp3")






def createVideo(audio_file="tt.mp3", output="final_video.mp4"):
    audio = AudioFileClip(audio_file)
    total_duration = audio.duration

    image_files = [f for f in os.listdir(".") if re.match(r"image\d+\.jpg", f)]
    image_files.sort(key=lambda f: int(re.search(r"\d+", f).group()))

    num_images = len(image_files)
    duration_per_image = total_duration / num_images

    clips = []
    for img in image_files:
        clip = ImageClip(img).with_duration(duration_per_image)
        clip = clip.resized(height=720)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    video = video.with_audio(audio)
    video.write_videofile(output, fps=24)

    print(f"Video saved as {output}")















text = prepareScript()
prepareVoice(text)

getImages()

createVideo()
