import wordcloud
import jieba
txt = "射了好多精液"
w = wordcloud.WordCloud( width=1000, font_path="msyh.ttc",height=800)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("jy.png")