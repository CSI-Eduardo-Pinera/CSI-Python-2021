import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67636/pg67636.txt")
res.raise_for_status()
playFile = open("The Useful Arts Employed in the Construction of Dwelling Houses.text", "wb")
for chunk in res.iter_content(10000):
    playFile.write(chunk)
playFile.close()