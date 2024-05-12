import random
messages = ["It is certain","It is decidedly so","Yes, definitely","Reply hazy try again","Ask again later","Concentrate and ask again","My reply is no", "Outlook not so good", "Very doubtful"]
print(messages[random.randint(0,len(messages)-1)])
print(len(messages))
print(random.randint(0,7))
print(messages[8])

# con el comando sep=[inserte el caracter a ser usado] podemos separar mensajes
#por ejemplo print(hola como estas, sep=,)nos entrega hola,como,estas