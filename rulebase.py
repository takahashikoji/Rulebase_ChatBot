import json
import collections

def rulebase(db,rt):
    count= 0
    while True:
        print(' ')
        if count== 0:
            print('「人工知能　','機械学習　','深層学習　」')
        else:
            print('上記から調べたい言葉を入力してね。')
        word= input('Keyward ')
        if word == 'exit':
            print('終了!!')
            break
        if word in db:
            count+= 1
            print(' ')
            print(db[word]['description'])
            print(db[word]['URL1'])
            print(db[word]['URL2'])
            database= db[word]['key']
            relation= rt[word]['key']
            print(' ')
            print('{} 関連の語句'.format(word))
            if database == relation:
                print(rt[word]["relation"])
        else:
            print('それはわからんばい。')

decoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)

with open('database.txt') as db_file:
    db = decoder.decode(db_file.read())
with open('relation.txt') as rt_file:
    rt = decoder.decode(rt_file.read())

rulebase(db,rt)
