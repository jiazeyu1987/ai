import  data_model_folder as dmf
import tkinter
import gc
class TKInterMain:
    def __init__(self):
        win = tkinter.Tk()
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        ww = 1400
        wh = 800
        w = tkinter.Canvas(win, width=ww, height=wh)
        w2= tkinter.Canvas(win, width=ww, height=wh)
        w.pack()
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
        self.old_entity = None


    def start(self):
        self.win.mainloop()

    def draw_entity(self,entity):
        #gc.collect()
        if(self.show_canvas==1):
            self.canvas2.pack()
            self.canvas.pack_forget()
            self.show_canvas = 2
        else:
            self.canvas.pack()
            self.canvas2.pack_forget()
            self.show_canvas = 1

        hn = int(self.wh * 0.8 / entity.shape[0])
        wn = int(self.ww * 0.8 / entity.shape[1])
        grid = int(min(hn, wn))
        tw = grid * entity.shape[1]
        th = grid * entity.shape[0]
        left_point = (int((self.ww - tw) / 2), int((self.wh - th) / 2))
        for i in range(entity.shape[0]):
            for j in range(entity.shape[1]):
                if(self.old_entity==None or self.old_entity[i][j]!=entity[i][j]):
                    p1 = j * grid + left_point[0]
                    p2 = i * grid + left_point[1]
                    p3 = j * grid + left_point[0] + grid - 2
                    p4 = i * grid + left_point[1] + grid - 2
                    color = self.get_color(entity[i][j])
                    if (self.show_canvas == 1):
                        self.canvas2.create_rectangle(p1, p2, p3, p4, fill=color)
                    else:
                        self.canvas.create_rectangle(p1, p2, p3, p4, fill=color)


    def get_color(self,v):
        if (v == 1):
            return "#000000"
        elif (v == 0):
            return "#FFFFFF"