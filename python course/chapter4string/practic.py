latter= ''' Dear <|Name|>,
            You are selected
            <|Date|>.'''
print(latter.replace("<|Name|>","Raghav").replace("<|Date|>","20/10/2029"))
print(latter.find("  ",""))