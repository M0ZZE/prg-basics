import tv

def main():
   # object creation
   tv_1=tv.TV()

   # object usage
   tv_1.turn_on()
   tv_1.set_channel(5)
   #['TVP1','TVP2','Polsat','TVN','Filmbox','Discover']
   tv_1.volume_down()
   tv_1.volume_up()
   tv_1.set_channels(['TVP1','TVP2','Polsat','TVN','Filmbox','Discover'])
   tv_1.show_channels()
   #tv_1.turn_off()
   tv_1.show_status()



if __name__ == "__main__":
   main() 