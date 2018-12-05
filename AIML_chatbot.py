import aiml

kernel=aiml.Kernel()
kernel.learn("Hello.aiml")
a="hello spider"
print(kernel.respond(a))



