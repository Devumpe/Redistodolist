
import redis

redis_host = "127.0.0.1"
redis_port = 6379

class hello_redis:
    try:
        def  __init__(self,client):
            self.client = client
        def input_redis(self,arg):  
            
            self.client.rpush('task',*(arg))
        def showout_redis(self):
            msg=self.client.lrange('task', 0 ,-1)
            print(msg)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    client = redis.Redis(host = redis_host, port = redis_port)
    hello_redis = hello_redis(client)
    print('please enter a chore or task.')
    text = input('')
    if text:
        hello_redis.input_redis(text) 
    else:
        print('Not new task or the blank task. you want to insert task? Y/N')
        answer = input('')
        if(answer == 'Y'):
            text = True
        elif(answer == 'N'):
            print('stop your task.')
            hello_redis.showout_redis()
    while True:
        text = input('')
        if not text:
            print('stop your task.')    
            break
        else:
            hello_redis.input_redis(text)
            
    hello_redis.showout_redis()








