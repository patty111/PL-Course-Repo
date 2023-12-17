from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import random
from wordcloud import WordCloud, STOPWORDS

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

text = open(path.join(d, 'alice.txt'), encoding='utf-8').read()

alice_mask = np.array(Image.open(path.join(d, "girl.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords, contour_width=3,contour_color='steelblue').generate(text)


plt.imshow(wc, interpolation='bilinear')
# default_colors = wc.to_array()
# plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
        #    interpolation="bilinear")

plt.axis("off")
plt.savefig("result.png")
plt.show()