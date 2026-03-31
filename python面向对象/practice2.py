class teacher:
    def __init__(self,name,teaching_year,major):
        self.name=name
        self.teaching_year=teaching_year
        self.major=major
    def teach(self):
        print(f"{self.name} teachs {self.major}.she/he has {self.teaching_year} ")

xing=teacher("xingpenghui","10","AI")
xing.teach()