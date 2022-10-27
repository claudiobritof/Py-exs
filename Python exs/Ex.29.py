#Car limit

vel = int(input("Car speed: \n"))
if vel > 80:
    print("Higher than speed limit. \nSpeed: {}km/h!".format(vel))
    multa = 7 * (vel - 80)
    print("Traffic ticket: U$S{:.2f}.".format(multa))
else:
    print("Speed inside limits.")