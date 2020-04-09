class PIP:
    def __init__(self, p_x, p_y, a_x, a_y, b_x, b_y, pt_list, pg):
        self.p_x = p_x
        self.p_y = p_y
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.pt_list = pt_list
        self.pg = pg

    def minimum_bound(self):
        if min(self.a_x) < self.p_x < max(self.a_x) and min(self.a_y) < self.p_y < max(self.a_y): 
            return True
        else:
            return False 

    # Source: [Franklin, 2000] http://geomalgorithms.com/a03-_inclusion.html
    def ray_casting(self):
        n = len(self.pg) - 1  
        counter = 0  
        for j in range(n):  
            if (self.pg[j][1] <= self.pt[1] < self.pg[j + 1][1]) or (self.pg[j][1] > self.pt[1] >= self.pg[j + 1][1]): 
                vt = (self.pt[1] - self.pg[j][1]) / (self.pg[j + 1][1] - self.pg[j][1]) 
                if self.pt[0] < (self.pg[j][0] + vt * (self.pg[j + 1][0] - self.pg[j][0])):
                    counter += 1
            j += 1
        return counter 

    def is_on_line(self):
        if not ((self.a_y <= self.p_y <= self.b_y or self.b_y <= self.p_y <= self.a_y) and
                (self.a_x <= self.p_x <= self.b_x or self.b_x <= self.p_x <= self.a_x)):
            return False                
        elif self.a_x == self.b_x and self.p_x == self.a_x:  
            return True             
        elif self.a_x != self.b_x and self.compute_y(self.p_x, self.a_x, self.a_y, self.b_x, self.b_y) == self.p_y:  
            return True 
        else:
            return False 
        
    def compute_y(self, x, x1, y1, x2, y2):
        return (x - x1) / (x2 - x1) * (y2 - y1) + y1

    def locate_points(self):
        loc = [None] * len(self.pt_list)
        for k in range(len(loc)):
            if not self.minimum_bound(self.p_x[k],
                                      self.p_y[k],
                                      self.s_x,
                                      self.s_y): 
                loc[k] = "outside"
            elif (self.ray_casting(self.pt_list[k], 
                                   self.pg)) % 2 != 0:  
                loc[k] = "inside"  
            else:
                loc[k] = "outside"  
            for j in range(len(self.s_x) - 1):
                if self.is_on_line(self.p_x[k],
                                   self.p_y[k], 
                                   self.s_x[j], 
                                   self.s_y[j], 
                                   self.s_x[j + 1], 
                                   self.s_y[j + 1]):  
                    loc[k] = "boundary"

    def locate_point(self):
        loc = [None]* len(self.pt_list)
        if (self.ray_casting(self.pt_list, self.pg)) % 2 != 0:  # Points tested by ray casting
            loc[0] = "inside"
        else:
            loc[0] = "outside"
        for j in range(len(self.s_x) - 1):
            if self.is_on_line(self.p_x, self.p_y, self.s_x[j], self.s_y[j], self.s_x[j + 1], self.s_y[j + 1]): 
                loc[0] = "boundary"
