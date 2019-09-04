testcases=int(input("Enter no of test cases: "))
seat=[]
for i in range(0,testcases):
    seat.append(int(input("Enter seat no: ")))

print(seat)
seat_type=''

left,right=False,False
L1,L2,R1,R2=False,False,False,False
opp_seat_no=0


#SEAT TYPE
for seat_no in seat :
    if seat_no%3==2:
        seat_type='MS'
        if seat_no%12 in range(1,7):
            left=True
            if seat_no%12 in range(1,4):
                L1=True
                opp_seat_no=seat_no+9
            else:
                L2=True
                opp_seat_no=seat_no+3
        else:
            right=True
            if seat_no%12>6 and seat_no%12<=9:
                R1=True
                opp_seat_no=seat_no-3
            else:
                R2=True
                opp_seat_no=seat_no-9


    else:
      if seat_no%6==1 or seat_no%6==0:
          seat_type='WS'
          if seat_no%12 in range(1,7):
              left=True
              if seat_no%12 in range(1,4):
                  L1=True
                  opp_seat_no=seat_no+11
              else:
                  L2=True
                  opp_seat_no=seat_no+1
          else:
                right=True
                if seat_no%12>6 and seat_no%12<=9:
                    R1=True
                    opp_seat_no=seat_no-1
                else:
                    R2=True
                    opp_seat_no=seat_no-11
      else:
            seat_type='AS'
            if seat_no%12 in range(1,7):
                left=True
                if seat_no%12 in range(1,4):
                    L1=True
                    opp_seat_no=seat_no+7
                else:
                    L2=True
                    opp_seat_no=seat_no+5
            else:
                right=True
                if seat_no%12>6 and seat_no%12<=9:
                    R1=True
                    opp_seat_no=seat_no-5
                else:
                    R2=True
                    opp_seat_no=seat_no-7

    print(opp_seat_no,end=' ')
    print(seat_type)
