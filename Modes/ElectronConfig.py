def electronConfig():
  electronNum = int(input("Whats the atomic number"))
  version = input("Do you want the condensed version? (y/n)")
  if version == 'y':
      condensed = True
  else:
      condensed = False
        
  electronConfig = ''

  configNums = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p"]
  condensedElements = ["[He] ", "[Ne] ", "[Ar] ", "[Kr] ", "[Xe] ", "[Rn] "]


  for nums in configNums:
    if electronNum > 0:
      if nums.find('s') == 1:
        if condensed and electronNum > 2 and nums == "1s":
          electronConfig = "[He]"
          electronNum -= 2
        else:
          if electronNum > 2:
            electronNum -= 2
            electronConfig += nums + "2 "
          elif electronNum < 2:
            electronConfig += nums + str(electronNum) + " "
            electronNum = 0
          else:
            electronNum -= 2
            electronConfig += nums + "2 "

      elif nums.find('p') == 1:
        if condensed and electronNum > 6:
          electronConfig = condensedElements[int(nums[0]) - 1] 
          electronNum -= 6
        else:
          if electronNum > 6:
            electronNum -= 6
            electronConfig += nums + "6 "
          elif electronNum < 6:
            electronConfig += nums + str(electronNum) + " "
            electronNum = 0
          else:
            electronNum -= 6
            electronConfig += nums + "6 "

      elif nums.find('d') == 1:
        if electronNum > 10:
          electronNum -= 10
          electronConfig += nums + "10 "
        elif electronNum < 10:
          electronConfig += nums + str(electronNum) + " "
          electronNum = 0
        else:
          electronNum -= 10
          electronConfig += nums + "10 "

      elif nums.find('f') == 1:
        if electronNum > 14:
          electronNum -= 14
          electronConfig += nums + "14 "
        elif electronNum < 14:
          electronConfig += nums + str(electronNum) + " "
          electronNum = 0
        else:
          electronNum -= 14
          electronConfig += nums + "14 "

      else:
          break

  print(electronConfig)