import json
with open("large-file.json", "r", encoding = "UTF=8") as file:
    content = json.load(file)


def change_content(data):
    for i in data:
        if isinstance(i,dict):
            if 'payload' in i:
                if 'size' in i['payload']:
                    i['payload']['size'] = 42
                elif 'release' in i['payload']:
                    if 'assets' in i['payload']['release']:
                        for j in i['payload']['release']['assets']:
                            j['size'] = 42
                    elif 'repo' in i['payload']['release']:
                        for j in i['payload']['release']['repo']:
                            j['size'] = 42 
                elif 'pull_request' in i['payload']:
                    if 'head' in  i['payload']['pull_request']:
                          if 'repo' in i['payload']['pull_request']['head']:
                                repo = i['payload']['pull_request']['head']['repo']
                                if isinstance(repo, dict):
                                    repo['size'] = 42
                                else:
                                    i['payload']['pull_request']['head']['size'] = 42
                    if 'base' in  i['payload']['pull_request']:
                        if 'repo' in i['payload']['pull_request']['base']:
                            i['payload']['pull_request']['base']['repo']['size'] = 42
                elif 'forkee' in i['payload']:
                    i['payload']['forkee']['size'] = 42
                            
                    
                                    

    return data
              

changed_content = change_content(content)
changed_content = changed_content[::-1]
with open("output.2.3.json", "w") as file:
    json.dump(changed_content, file, indent=4, separators=(',', ':'))