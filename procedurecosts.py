def newprocedure():
    procedure=None
    revenue=0
    print('The following are lists of clinical oral evaluation/ prediagnostic service procedures. Enter each procedure, one by one. Type done when finished.')
    print('D0120, D0140, D0145, D0150,D0160, D0170, D0180, D0190, D0191')
    while True:
        procedure= input('what type of procedure was performed? ')
        if procedure=='done':
            break
        procedure= procedure.rstrip()
        procedure=procedure.upper()
        procedures[procedure]=procedures.get(procedure, 0)+1
    print('The following are lists of Diagnostic Imaging procedures. Enter each procedure, one by one. Type done when finished.')
    print('D0210, D0220, D0230, D0240, D0250, D0270, D0272, D0273, D0274, D0277, D0310, D0320, D0321')
    DIprocedure=None
    while True:
        DIprocedure=input('what type of procedure was performed? ')
        DIprocedure= DIprocedure.rstrip()
        if DIprocedure=='done':
            break
        Diprocedure=DIprocedure.upper()
        procedures[DIprocedure]=procedures.get(DIprocedure, 0)+1
    userresponse= input('if you would like to add procedures for another patient, type \'yes\', if not, type \'done\'')
    if userresponse=='yes':
        newprocedure()
    procedureslist=['D0120','D0140','D0145','D0150','D0160','D0170', 'D0180', 'D0190', 'D0191', 'D0210', 'D0220', 'D0230', 'D0240', 'D0250', 'D0270', 'D0272', 'D0273', 'D0274', 'D0277', 'D0310', 'D0320', 'D0321'  ]
    if userresponse=='done':
        for element in procedureslist:
            procedures[element]=procedures.get(element,0)
        print("Procedure, Frequency")
        for k, v in procedures.items():
            print (k,v)
            if k=='D0120' or k=='D0140' or k=='D0145' or k=='D0160' or k=='D0170' or k=='D0180':
                revenue+=(v*150)
            elif k=='D0150':
                revenue+=(v*175)
            elif k=='D0210':
                revenue+=(v*200)
            elif k=='D0220' or 'D0240' or 'D0250':
                revenue+=(v*75)
            elif k=='D0230' or 'D0270':
                revenue+=(v*50)
            elif k=='D0272':
                revenue+=(v*70)
            elif k=='D0273':
                revenue+=(v*90)
            elif k=='D0274':
                revenue+=(v*110)
            elif k=='D0277':
                revenue+=(v*160)
        print("The revenue for all recorded UCR procedures is", revenue)
        return(revenue)




print('This Program will calculate revenue for dental clinics based off UCR procedure revenue')
firstinput= input('type \'new\' if you wish to add a new procedure: ')
procedures=dict()
if firstinput=='new':
    newprocedure()
