import redis

client = redis.StrictRedis(host="127.0.0.1", port=6379)

# client.set("username", "时可爱")
print(client.get("username").decode("utf-8"))

'''
pipe = client.pipeline()
# print(dir(pipe))
pipe.set("s1", "女班长笑的好开心")
pipe.set("s2", "男班长笑的好猥琐")
pipe.set("s3", "当兵的不敢惹")
pipe.set("s4", "少林的也惹不起，会空手入白刃")

pipe.execute()
'''

print("##"*10)
print("内置方法：")
print(dir(client))
print("##"*10)

