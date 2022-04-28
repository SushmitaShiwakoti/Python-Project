class student:
    def execute(self):
        print("Compiling")
        print('Running')

class myeditor:
    def execute(self):
        print('Spell Check')
        print('Convertion check')
        print('Compiling')
        print('Running')

class laptop:
    def code(self,ide):
        ide.execute()
# ide=student()
ide=myeditor()
lap1=laptop()
lap1.code(ide)

