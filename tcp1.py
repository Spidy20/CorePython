class TSP():

    def __init__(self):

        self.cost_matrix=list()
        self.init_cost_list=list()
        self.visited=list()
        self.cost=0
        self.a=list()
        self.n=0
        self.temp_list=list()
        self.temp=0


    def get(self):

        # Getting number of node
        self.n=int(input("Enter number of cities"))

        #Creating cost matrix
        print("Enter cost matrix:\n")
        for i in range(self.n):
            init_cost_str=input(f"Enter element of row #{i}:")
            self.init_cost_list=list(init_cost_str.split(" "))
            self.cost_matrix.append(self.init_cost_list)
            self.visited.append(0)

        #Show cost matrix
        print("The cost matrix is:")
        for i in self.cost_matrix:
            print(i)



        #Creating empty cost matrix
        for i in range(self.n):
            self.temp_list.append(0)
        for i in range(self.n):
            self.a.append(self.temp_list)


        #Show empty cost matrix
        for i in self.a:
            print(i)

        print("Visited",self.visited)


    def mincost(self,city):
        self.city=city

        self.visited[self.city] = 1
        print("Chack visited", self.visited)
        k=self.city + 1
        print(f"City count:",k)

        if self.city==4:
            self.put()
        else:
            self.ncity= self.least(self.city)
            if self.ncity==999:
                self.ncity=0
                print(f"n city {self.ncity+1}")
                self.cost+=int(self.cost_matrix[self.city][self.ncity])
                print("Cost:",self.cost)
                return
        self.mincost(self.ncity)


    def least(self,c):
        self.temp+=1
        return self.temp


    def put(self):
        print("\nMinimum cost")
        print(self.cost)


#Initiatlizing object of Class TSP
t=TSP()
t.get()
print("The path is:")
t.mincost(0)
t.put()