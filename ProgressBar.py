#progress bar v1

class ProgressBar():
    def __init__(self, total, width=10, symbol='=', brackets='[]', header='Progress:', footer='', title='Loading...'):
        self.total = total
        self.width = width
        self.symbol = symbol
        self.brackets = brackets
        self.header = header
        self.footer = footer
        self.progress = 0
        self.title = title
        print(title)

    def setProgress(self, progress):
        self.progress = progress

    def getProgress(self):
        return self.progress

    def update(self):
        print('\r'+self.header+' '+self.brackets[0]+self.symbol*(int(self.progress/self.total*self.width))+' '*(self.width-int(self.progress/self.total*self.width))+self.brackets[1]+' '+str(int(self.progress/self.total*100))+'%'+' '+self.footer,end='')
        return self.progress

    def done(self):
        print('\r'+self.header+' '+self.brackets[0]+self.symbol*self.width+self.brackets[1]+' 100%'+' '+self.footer)
    
if __name__ == '__main__':
    from time import sleep as s
    
    Bar = ProgressBar(100)

    for x in range(0,100):
        Bar.setProgress(x)
        Bar.update()
        s(0.025)
    Bar.done()

    input('Press enter to quit')
        
    
