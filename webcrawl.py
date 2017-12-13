import json
import webhoseio

webhoseio.config(token="160a0e9e-b47e-4229-bf40-d7f1e2d5bf35")

query_params = {
    "q": "site:nytimes.com language:english site_type:news spam_score:0",
    "ts": "1504680060834",
    "sort": "crawled"
}

output = webhoseio.query("filterWebContent", query_params)
e=[]
count=0
for i in range(50):
    print(count)
    print(len(output['posts']))
    for x in output['posts']:
	if x['title']:
            count+=1
	    e.append({'title': x['title'], 'text': x['text'], 'label': 'real'})
        
    #time.sleep(300)
    output = webhoseio.get_next()


with open('web75.json', 'w') as outfile: json.dump(e, outfile)
print("success")
