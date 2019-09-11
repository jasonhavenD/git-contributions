import datetime
import schedule
import time
import os

'''
nohup python auto_commit.py &
'''

def update_readme():
    now=datetime.datetime.now()
    ts=now.strftime('%Y-%m-%d %H:%M:%S')
    message="update at {}".format(ts)
    os.system('git add ./*')
    os.system('git commit -m "update"')
    os.system('git push')
    with open('log.txt','a+',encoding='utf-8') as f:    
        f.write(message)
        f.write('\n')
        print(message)

if __name__ == "__main__":
    schedule.every(6).hours.do(update_readme)

    while True:
        schedule.run_pending()
        time.sleep(1)
