# 评分列表
score_li = []
# 总分
total_score = 0
for i in range(1, 11):
    score = float(input(f"请第{i}位评委输入评分：\n"))
    score_li.append(score)
score_li.sort()
print(f"去掉最低分：{score_li[0]}")
print(f"去掉最高分：{score_li[len(score_li)-1]}")
# 去掉最低分
score_li.remove(score_li[0])
# 去掉最高分
score_li.pop()
for j in score_li:
    total_score += j
print(f'选手最终得分为：{total_score/(len(score_li))}')
