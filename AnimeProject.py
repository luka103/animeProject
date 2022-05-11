# import sqlite3
#
# import json
#
# import requests
#
# anime_name = input("please enter anime name: ")
# fact_id = int(input("please enter fact id: "))
# url = f'https://anime-facts-rest-api.herokuapp.com/api/v1/{anime_name}/{fact_id}'
# r = requests.get(url)
# res_json = r.text
# res = json.loads(res_json)
# with open('anime.json', 'w') as file:
#     json.dump(res, file, indent=4)
#
# m = res['data']
# fact = m['fact']
# factId = m['fact_id']
#
# conn = sqlite3.connect("anime_fact.sqlite")
# cursor = conn.cursor()
# # cursor.execute('''CREATE TABLE facts
# #                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                 anime VARCHAR(50),
# #                 anime_fact VARCHAR(100),
# #                 fact_id FLOAT);''')
# # მოცემული ბრძანება მომხარებელს აძლევს საშუალებას ბაზაში გადაიტანოს ანიმეს დასახელება,ფაქტის ნომერი და თვითონ ფაქტი
# # cursor.execute("INSERT INTO facts (anime, fact_id, fact) VALUES ('{}', '{}', '{}')".format(anime_name, factId, fact))
# # conn.commit()
#
# # print(r)
# # print(r.status_code)
# # print(r.headers)
