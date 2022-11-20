def load_list(x, path_list='list.txt'):
    '''Open the lexic and put it in a list '''
    content_list_split = []
    dict1 = {}
    a = 0
    x = x.split(" ")
    with open(path_list, encoding='utf8') as f:
        content_list = f.read().splitlines()
        for i in range(len(content_list)):
            content_list_split.append(content_list[i].split(','))
        for j in range(len(content_list_split)):
            dict1[content_list_split[j][0]] = content_list_split[j][1]
        for i in x:
            if i in dict1:
                print(dict1.get(i))
                a = a + int(dict1.get(i))
        return a
print(load_list("je suis Capacités abandon"))