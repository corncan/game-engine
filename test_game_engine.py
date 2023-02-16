#Copyright 2023 Hudson Rocke

import Game_engine as en

coords = [100, 100]

p = False
backdrop = False

while 1:
    en.display("guava.png", coords, False, (10, 10))
    if en.sense_key("w"):
        coords[1] -= 10
        
    #en.play_sound("pickupCoin.wav")
    
    p = en.sense_press("p", p)
    if p:
        if not backdrop:
            backdrop = True
        elif backdrop:
            backdrop = False
            
    en.text((20, 9), "Text", 20, "white")
    
    if backdrop:
        en.backdrop()
        clicked = en.button((0, 0), (100, 100), "Button")
        
    en.run((100, 0, 50))