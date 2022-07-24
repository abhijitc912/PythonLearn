content = True
i=1
with open('14_search_log.txt') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f'python is present in line number {i}')
        i+=1
        