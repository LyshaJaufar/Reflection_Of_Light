        if e.key == pygame.K_0 or e.key == pygame.K_1 or e.key == pygame.K_2 or e.key == pygame.K_3\
        or e.key == pygame.K_4 or e.key == pygame.K_5 or e.key == pygame.K_6 or e.key == pygame.K_7\
        or e.key == pygame.K_8 or e.key == pygame.K_9 or e.key:
            angle.text +=  str(e.key-48)
            print(angle.text)
            print('here')

        #angle.text += str(current)
        
        if e.key == pygame.K_RETURN:
            angle.returnPressed = True
            angle.active = False
            return angle.text
