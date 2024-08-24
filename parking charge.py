veh=input('enter the type of vehicle: ')
time=int(input('enter number of hours the vehicle is parked: '))
if (veh=='cycle' or veh == 'bike'):
    charge=time*5
    print('parking charge is: ',charge)
elif (veh=='truck' or veh == 'bus'):
    charge=time*20
    print('parking charge is: ',charge)
elif (veh=='car'):
    charge=time*10
    print('parking charge is: ',charge)
else:
    print('enter a valid vehicle')
