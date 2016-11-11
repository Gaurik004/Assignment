import time
import progressbar

bar=progressbar.progressBar()

for i in bar(range(100)):
    time.sleep(0.02)