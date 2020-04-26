
#records all items 

item_list = ['a', 'b', 'c']
audio_cables = {'ts':1, 'trs': 2, 'trs_snake': 1}

class Studio():
    def __init__(self, item_list, audio_cables):
        self.item_list = item_list
    def __repr__():
        return "Studio" 
    def inventory(self):
        print(item_list)

studio_1 = Studio(item_list, audio_cables)
print(studio_1.inventory()) 
