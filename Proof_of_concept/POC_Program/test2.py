total = 0
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
                a = int(a) + int(dict1.get(i))
        return a

print(input("Comment vous sentez vous de manière générale ?"))
print("je suis déprimé tous les jours et je me sens triste quasiment toute la journée\n")
total = total + load_list("je suis déprimé tous les jours et je me sens extrèmement triste quasiment toute la journée")


print(input("Vous aviez presque tout le temps le sentiment de n'avoir goût à rien, d'avoir perdu l'intérêt ou le plaisir pour les choses qui vous plaisent habituellement ?"))
print("je me sens perdu dans ce que je ne fait rien pendant mes journée\n")
total = total + load_list("je me sens perdu dans ce que je ne fait rien pendant mes journée")

print(input("Avez vous encore de l'appetit?"))
print("je ne mange quasiment pas\n")
total = total + load_list("je ne mange quasiment pas")


print(input("Êtes vous tendu, angoissé ou irritable en ce moment ?"))
print("je suis assez facilement irritable, et de plus en plus tendu\n")
total = total + load_list("je suis assez facilement irritable et de plus en plus tendu")

print(input("Rensentez vous un ralentissement dans votre vie ou un manque d'envie?"))
print("je suis lent et je ne ressent rien me donne envie\n")
total = total + load_list("je suis lent et rien ne me donne envie")

if total >= -3 :
    print("Diagnostic: possible saineté")
elif total < -3 and total >=-9:
    print("Diagnostic: possible dépréssion légère")
elif total <= -10 and total >= -17:
    print("Diagnostic: possible depression moyen")
else:
    print("Diagnostic: possible dépression sévere")
