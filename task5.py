import json
import csv

PURCHASE_LOG_FILE = './task5/purchase_log.txt'
VISIT_LOG_FILE = './task5/visit_log__1_.csv'
FUNNEL_FILE = './task5/funnel.csv'

purchase_dict = {}
with open(PURCHASE_LOG_FILE, 'r', encoding='utf-8') as f:
    for line in f:
        record = json.loads(line.strip())
        user_id = record.get('user_id')
        category = record.get('category')
        if user_id != "user_id":
            purchase_dict[user_id] = category

with open(VISIT_LOG_FILE, 'r', encoding='utf-8') as visit_log, \
        open(FUNNEL_FILE, 'w', encoding='utf-8', newline='') as funnel:
    reader = csv.reader(visit_log)
    writer = csv.writer(funnel)

    writer.writerow(['user_id', 'source', 'category'])

    next(reader)

    for row in reader:
        user_id, source = row
        category = purchase_dict.get(user_id)
        if category:
            writer.writerow([user_id, source, category])
