class C:
    def __init__(self, this_dict):
        self.this_dict={}
        self.this_dict=this_dict
        self.sum=0

    def m1(self,this_key, this_value):
        self.this_dict[f'{this_key}']=this_value

    def m2(self, this_keys):
        for x in list(this_keys):
            self.sum+=self.this_dict[f'{x}']


    def __str__(self):
        return f'{self.this_dict} {self.sum}'


temp=C({"A":120,"D":150,"G":90,"K":110})
temp.m1('G',130)
temp.m2('GA')
print(temp.__str__())