import datetime
import schedule
import time
import os


def update_readme(message):
    os.system("sed -i '$d' README.md")
    os.system('echo "{}" >> README.md'.format(message))
    os.system('git add README.md')
    os.system('git commit -m "update"')
    os.system('git push')
    print('update github readme.md: ', message)

if __name__ == "__main__":
    now=datetime.datetime.now()
    ts=now.strftime('%Y-%m-%d %H:%M:%S')
    message="update at {}".format(ts)
    schedule.every(10).seconds.do(update_readme, message=ts)

    while True:
        schedule.run_pending()
        time.sleep(1)
