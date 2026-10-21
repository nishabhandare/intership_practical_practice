while True:
    print("Main menu")
    print("1.Book Ride")
    print("2.Exit")
    print()

    user_response=int(input("Enter Choice (Book Ride or  Exit): "))
    match user_response:
        case 1:
            while True:
                print("\nCab Types")
                print("1. Auto\n2. Sedan\n3. SUV\n")
                cab_type=int(input("Choose Cab Type:"))
           
                match cab_type:
                    case 1:
                        print("1. Auto \tRate Per KM 12")
                        rate=12
                        break
                    case 2: 
                        print("2.Sedan \tRate Per KM 18")
                        rate=18
                        break
                    case 3:
                        print("3.SUV \tRate Per KM 25")
                        rate=25
                        break
                    case _:
                        print("Invalid Cab Type")
                        
            while True:
                print("\nPredefine Routes")
                print("Route No.  Source  Destination  Fixed_Distance")
                print("1.  Pune Station  Shivajinagar  5km")  
                print("2.  Pune Station  Kothrud  5km") 
                print("3.  Pune Station  Wakad  5km") 
                print("4.  Swargate  Kothrud  8km")
                print("5.  Swargate  Shivajinagar  8km")
                print("6.  Swargate  Wakad  8km")
                print("7.  Hinjawadi  Wakad  10km")
                print("8.  Hinjawadi  Shivajinagar  10km")
                print("9.  Hinjawadi  Kothrud  10km")
                print()
                route=int(input("Choice Route: "))
                match route:
                    case 1:
                        source="Pune Station"
                        destination="Shivajinagar"
                        distance=5
                        print("Pune Station To Shivajinagar 5km")
                        break 
                    case 2:
                        source="Pune Station"
                        destination="Kothrud"
                        distance=5
                        print("Pune Station To Kothrud 5km")
                        break 
                    case 3:
                        source="Pune Station"
                        destination="Wakad"
                        distance=5
                        print("Pune Station To Wakad 5km")
                        break 
                    case 4:
                        source="Swargate"
                        destination="Kothrud"
                        distance=8
                        print("Swargate To Kothrud 8km")
                        break 
                    case 5:
                        source="Swargate"
                        destination="Shivajinagar"
                        distance=8
                        print("Swargate To Shivajinagar 8km")
                        break 
                    case 6:
                        source="Swargate"
                        destination="Wakad"
                        distance=8
                        print("Swargate To Wakad 8km")
                        break
                    case 7:
                        source="Hinjawadi"
                        destination="Wakad"
                        distance=10
                        print("Hinjawadi To Wakad 10km")
                        break
                    case 8:
                        source="Hinjawadi"
                        destination="Shivajinagar"
                        distance=10
                        print("Hinjawadi To Shivajinagar 10km")
                        break
                    case 9:
                        source="Hinjawadi"
                        destination="Kothrud"
                        distance=10
                        print("Hinjawadi To Kothrud 10km") 
                        break
                    case _:
                        print("Invalid Route.Try Again.")
                        continue
                        
            
            print("\nCalculate Fare")
            total_fare= rate * distance
            print("Cab Type:",cab_type)
            print("Source:",source)
            print("Destination:",destination)
            print("Distance:",distance,)
            print("Rate:",rate)
            print("Total Fare:",total_fare)
        
            print("\nCancellation Before OTP")
            print("1. Confirm & Share OTP\n2. Cancel Ride")
            print("Once the OTP has been shared, the ride cannot be cancelled")
            print()
            final_conformation=int(input("Choose Conform or Cancel Ride: "))
            match final_conformation:
                case 1:
                    otp=1234
                    print("Confirm & Share OTP")
                    while True:
                        print("OTP: ",otp)
                        Enter_otp=input("Enter Given OTP:")
                        if Enter_otp == str(otp):
                            print("OTP is Correct. Ride is Confirmed.")
                            break
                        else:
                            print("OTP is Incorrect.Try Again.")
                                    
                case 2:
                    print("Ride is Canceled")
                case _:
                    print("Invalid choice.")    
            print()
        case 2:
            print("GoodBye.")
            break
        
        case _:
            print("Invalid Choice.")       
                