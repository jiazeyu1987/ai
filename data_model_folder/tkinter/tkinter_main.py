import  data_model_folder as dmf
import tkinter
import gc
import  time
import numpy as np
import  threading
class TKInterMain:
    def __init__(self):
        win = tkinter.Tk()
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        ww = 1400
        wh = 800
        w = tkinter.Canvas(win, width=ww, height=wh)
        w2= tkinter.Canvas(win, width=ww, height=wh)
        #w.pack()
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        #win.mainloop()
        self.win = win
        self.wh =int(wh)
        self.ww = int(ww)
        self.canvas = w
        self.canvas2 = w2
        self.show_canvas = 1
        self.current_canvas = 1
        self.old_entity = None
        self.stop_flag = False
        self.entity_grid = None
        self.img = None

    def start(self):
        self.win.mainloop()




    def set_entity(self,entity):
        self.canvas.pack_forget()
        self.entity_grid = []
        for j in range(entity.shape[0]):
            arr=[]
            for i in range(entity.shape[1]):
                arr.append(None)
            self.entity_grid.append(arr)
        hn = (self.wh * 0.8 / entity.shape[0])
        wn = (self.ww * 0.8 / entity.shape[1])
        grid = (min(hn, wn))
        tw = grid * entity.shape[1]
        th = grid * entity.shape[0]
        left_point = (((self.ww - tw) / 2), ((self.wh - th) / 2))
        for i in range(entity.shape[0]):
            for j in range(entity.shape[1]):
                if (self.old_entity == None ):
                    p1 = j * grid + left_point[0]
                    p2 = i * grid + left_point[1]
                    p3 = j * grid + left_point[0] + grid
                    p4 = i * grid + left_point[1] + grid
                    color = self.get_color(entity[i][j])
                    self.entity_grid[i][j]=self.canvas.create_rectangle(p1, p2, p3, p4, fill="#FFFFFF")
        self.old_entity = np.zeros(entity.shape,np.int16)
        self.canvas.pack()

    def draw_entity(self,entity):
        hn = (self.wh * 0.8 / entity.shape[0])
        wn = (self.ww * 0.8 / entity.shape[1])
        grid = (min(hn, wn))
        tw = grid * entity.shape[1]
        th = grid * entity.shape[0]
        left_point = (((self.ww - tw) / 2), ((self.wh - th) / 2))
        if(self.old_entity is None):
            pass
        else:
            for i in range(entity.shape[0]):
                for j in range(entity.shape[1]):
                    if(self.old_entity[i][j]!=entity[i][j]):
                        p1 = j * grid + left_point[0]
                        p2 = i * grid + left_point[1]
                        p3 = j * grid + left_point[0] + grid
                        p4 = i * grid + left_point[1] + grid
                        color = self.get_color(entity[i][j])
                        #self.canvas.create_rectangle(p1, p2, p3, p4, fill=color)
                        self.canvas.itemconfig(self.entity_grid[i][j],fill=color)
        self.old_entity = entity

    def draw_entity2(self,entity):
        self.get_image(entity)
        self.canvas.create_image((600, 800), image=self.img, state="normal")
        #th = threading.Thread(target=self.get_image, args=(entity,))

    def get_image(self,entity):
        img = tkinter.PhotoImage(width=600, height=800)
        for i in range(entity.shape[0]):
            for j in range(entity.shape[1]):
                if (self.old_entity[i][j] != entity[i][j]):
                    color = self.get_color(entity[i][j])
                    img.put(color, (j, i))
        self.img = img
                    # self.canvas.create_rectangle(p1, p2, p3, p4, fill=color)

                    #self.canvas.itemconfig(self.entity_grid[i][j], fill=color)




    def get_color(self,v):
        if (v == 1):
            return "#000000"
        elif (v == 0):
            return "#FFFFFF"