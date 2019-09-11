import datetime
import schedule
import time
import os

'''
nohup python auto_commit.py &
'''


def update_readme():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    message = "Update at {}".format(ts)
    os.system("sed -i '$d' README.md")
    os.system('echo "{}" >> README.md'.format(message))

    os.system('git add README.md')
    os.system('git commit -m "update"')
    os.system('git push')
    
    with open('log.txt', 'a+', encoding='utf-8') as f:
        f.write(message)
        f.write('\n')
        f.flush()

if __name__ == "__main__":
    schedule.every(6).hours.do(update_readme)
    if os.path.exists('log.txt'):
        os.remove('log.txt')

    while True:
        schedule.run_pending()
        time.sleep(1)
