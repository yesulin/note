def word(words):
    if '山寨' in words:
        new_words=words.replace('山寨','**')
        return new_words # 返回语句

result=word('我这个手机是山寨版的吧！')
print(result)