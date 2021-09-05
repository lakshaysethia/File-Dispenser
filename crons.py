from crontab import CronTab

cron = CronTab(user='root')

job = cron.new(command='python file_dipenser.py')

job.minute.every(1)
cron.write()
