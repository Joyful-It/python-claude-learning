class LLM:
    def __init__(self,name,number,frame):
        self.name=name
        self.number=number
        self.__frame=frame
    def set_frame(self):
        print(f"{self.__frame}")
open=LLM("open",10,123)
open.set_frame()