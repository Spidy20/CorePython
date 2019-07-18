#Create a private function
class SeeMee:
    def youcanseeme(self):
        print('you can see me')

    def __youcannotseeme(self):
        print( 'you cannot see me')

# Outside class
Check = SeeMee()
print(Check.youcanseeme())
print(Check._SeeMee__youcannotseeme())