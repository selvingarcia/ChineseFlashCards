import pandas as pd
from chinese import ChineseAnalyzer
import pinyin.cedict

df = pd.read_csv("most_common_5k_chinese_words_v5.csv")
# dfs = df[["word", "pinyin"]]

meanings = [pinyin.cedict.translate_word(word) for word in df["word"].values]

my_series = pd.Series(meanings, name="meaning")
df= pd.concat([df, my_series], axis=1)
dfs = df[["word","pinyin", "meaning"]]
dfs.to_csv("data.csv", index=False)