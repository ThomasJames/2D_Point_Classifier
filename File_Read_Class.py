class ReadFile:

    def __init__(self, p_x: float, p_y: float, id_n: int, cat: str):
        self.p_x = p_x
        self.p_y = p_y
        self.pt_x_list = []
        self.pt_y_list = []
        self.id_n = id_n
        self.cat = cat

    def access_csv_file(self):
        try:
            with open('r') as f:
                lines = f.readlines()[1:]
                for l in lines:
                    l = l.strip().split(',')
                    self.pt_x_list.append(float(l[1]))
                    self.pt_y_list.append(float(l[2]))
        except IOError:
            print("Unable to read this file")

    def read_output(self):
        try:
            with open('r') as o:
                lines = o.readlines()[1:]
                for l in lines:
                    l = l.strip().split(',')
                    self.id_n.append(str(l[0]))
                    self.cat.append(str(l[1]))
        except IOError:
            print("Unable to read this file")

    try:
        def generate_coordinates(self):
            return list(map(lambda x, y: (x, y), self.p_x, self.p_y))
    except IOError:
        print("Unable to create coordinates")
