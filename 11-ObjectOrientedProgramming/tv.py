class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no=1
      self.channels_list=[]
      self.volume=0

   #On/Off functions   
   def turn_off(self):
      self.is_on=False
   def turn_on(self):
      self.is_on=True

    #prints informations about channel, volume, status
   def show_status(self):
      print(f'Is On?: {self.is_on}.')
      if(self.is_on):
            try:
                print(f'Channel: {self.channel_no} ({self.channels_list[self.channel_no-1]}) Volume: {self.volume}')
            except IndexError:
                print(f'Channel: {self.channel_no} (No Singnal) Volume: {self.volume}')

    #setts channel number
   def set_channel(self,new_channel):
      self.channel_no=new_channel

    #setts channels list
   def set_channels(self, channels_list):
      self.channels_list=channels_list

    #prints whole channel list with indexes
   def show_channels(self):
      for i in range(len(self.channels_list)):
         print(f'{i+1}. {self.channels_list[i]}')

    #volume controll
   def volume_up(self):
        if(self.volume<10):
            self.volume+=1
   def volume_down(self):
        if(self.volume>0):
            self.volume-=1