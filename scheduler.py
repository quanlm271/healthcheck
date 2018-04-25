
import json
import sched, datetime, time
import requests

skeduler = sched.scheduler(time.time, time.sleep)
jobs = []

def load_job():
    print "load job"
    return [
            {
                'url': 'http://google.com.vn',
                'interval': 2,
                'priority': 1
            },
        ]
def do_action(code):
    print code
    if code.status_code == 200:
        print "OK"

def execute_job(job):#address
    print "--execute job"
    print ("LOG-"+str(datetime.datetime.today())+"-"+job['url'])
    try:
        r = requests.get(job['url'])
        do_action(r)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print e
    # repeat
    register_job(job)

def register_job(job):
    print "--register job"
    skeduler.enter(job['interval'], 100, execute_job, (job,))

def init():
    print "init"
    jobs = load_job()
    for j in jobs: register_job(j)

def run():
    init()
    skeduler.run()

run()