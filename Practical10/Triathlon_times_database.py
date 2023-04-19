#create a class called 'triathlon'
class triathlon:
    #define the attribute of each variable
    name = ''
    place = ''
    time_swim = 0
    time_cycle = 0
    time_run = 0
    total_time = 0
    #define the function
    def __init__(self, n, p, s, c, r):
        self.name = n
        self.place = p
        self.time_swim = s
        self.time_cycle = c
        self.time_run = r
    def op(self):
        t = self.time_swim+self.time_cycle+self.time_run
        print('Name:',self.name, ' Location:', self.place,' Time for swimming:', self.time_swim,' Time for cycling:',self.time_cycle,' Time for running:',self.time_run,' Total time:', t)
#input an example
a = triathlon('Karina Yoon', 'Seoul', 120, 130, 50)
a.op()