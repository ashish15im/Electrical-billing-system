__author__ = 'Ashish'
import wx

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Real World Test")
        panel = wx.Panel(self)

        # First create the controls
        topLbl = wx.StaticText(panel, -1, "NEB SARAI EXTN. AREA WELFARE SOCIETY",pos=(0,0),size=wx.DefaultSize,style=wx.ALIGN_CENTER_HORIZONTAL)
        topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))

         #The middle names

        middleLbl = wx.StaticText(panel, -1, "Registered under Societies "
                                             "Regestration Act "
                                             "1860 Regestration"
                                             " No.:S-33898(1998)",pos=(0,100),size=wx.DefaultSize,style=wx.ALIGN_CENTER_HORIZONTAL)
        middleLbl.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD))
        #last label

        lastLbl = wx.StaticText(panel, -1, "Office:285-A,Forest lane,"
                                           "Nebsarai Extn,"
                                           "New Delhi-110068",size=wx.DefaultSize,style=wx.ALIGN_CENTER_HORIZONTAL)
        lastLbl.SetFont(wx.Font(6, wx.SWISS, wx.NORMAL,wx.NORMAL))



        nameLbl = wx.StaticText(panel, -1, "Name:",pos=wx.DefaultPosition,size=wx.DefaultSize,style=wx.ALIGN_LEFT)
        name = wx.TextCtrl(panel, -1, "",pos=wx.DefaultPosition,size=(175, -1),style=wx.ALIGN_LEFT);

        addrLbl = wx.StaticText(panel, -1, "Address:",style=wx.ALIGN_LEFT)
        addr1 = wx.TextCtrl(panel, -1, "",style=wx.ALIGN_LEFT);
        addr2 = wx.TextCtrl(panel, -1, "",style=wx.ALIGN_LEFT);


        BillDate = wx.StaticText(panel, -1, "Day, Month, Year:",style=wx.ALIGN_LEFT)
        Day= wx.TextCtrl(panel, -1, "",size=(150,-1),style=wx.ALIGN_LEFT);
        Month = wx.TextCtrl(panel, -1, "",size=(100,-1),style=wx.ALIGN_LEFT);
        Year= wx.TextCtrl(panel, -1, "",size=(70,-1),style=wx.ALIGN_LEFT);

        MeterNo = wx.StaticText(panel, -1, "Meter Number:",style=wx.ALIGN_LEFT)
        MeterNo1 = wx.TextCtrl(panel, -1, "",style=wx.ALIGN_LEFT);

        BillNo = wx.StaticText(panel, -1, "Bill No:",style=wx.ALIGN_LEFT)
        BillNo1= wx.TextCtrl(panel, -1, "",style=wx.ALIGN_LEFT);

        BillingCycle=wx.StaticText(panel,-1,"Billing Cycle",style=wx.ALIGN_LEFT)
        BillingCycle1=wx.TextCtrl(panel,-1," ",style=wx.ALIGN_LEFT);

        MeterReading = wx.StaticText(panel, -1, "Previous Readings,Current Readings:",style=wx.ALIGN_LEFT)
        Previous= wx.TextCtrl(panel, -1, "",size=(150,-1));
        Current= wx.TextCtrl(panel, -1, "",size=(100,-1));
        #Year= wx.TextCtrl(panel, -1, "", size=(70,-1));

        TotalUnits=wx.StaticText(panel,-1,"Total Units")
        TotalUnits1=wx.TextCtrl(panel,-1," ");

        Rate_Units=wx.StaticText(panel,-1,"Rate/unit")
        Rate_Units1=wx.TextCtrl(panel,-1," ");

        Amount=wx.StaticText(panel,-1,"Amount(*)")
        Amount1=wx.TextCtrl(panel,-1," ");

        FixedCharges = wx.StaticText(panel, -1, "Load, Rate Rs, Amount Rs.:")
        Load= wx.TextCtrl(panel, -1, "", size=(150,-1));
        Rate_Rs = wx.TextCtrl(panel, -1, "", size=(50,-1));
        Amount_Rs= wx.TextCtrl(panel, -1, "", size=(70,-1));

        TotalRs=wx.StaticText(panel,-1,"Total Rs")
        TotalRs1=wx.TextCtrl(panel,-1," ");

        MaintainceRs=wx.StaticText(panel,-1,"Maintenance Rs")
        MaintainceRs1=wx.TextCtrl(panel,-1," ");

        OtherRs=wx.StaticText(panel,-1,"Other Rs")
        OtherRs1=wx.TextCtrl(panel,-1," ");

        TotalRs=wx.StaticText(panel,-1," ")
        TotalRs1=wx.TextCtrl(panel,-1," ");

        GrandTotalRs=wx.StaticText(panel,-1,"Grand Total Rs")
        GrandTotalRs1=wx.TextCtrl(panel,-1," ");

        PreviousDueRs=wx.StaticText(panel,-1,"Previous Due Rs")
        PreviousDueRs1=wx.TextCtrl(panel,-1," ");

        PaymentRecRs=wx.StaticText(panel,-1,"Payment Received Rs")
        PaymentRecRs1=wx.TextCtrl(panel,-1," ");

        CurrentChrRs=wx.StaticText(panel,-1,"Current Charges Rs")
        CurrentChrRs1=wx.TextCtrl(panel,-1," ");

        TotalAmountDueRs=wx.StaticText(panel,-1,"Total Amount Due Rs")
        TotalAmountDueRs1=wx.TextCtrl(panel,-1," ");

        DueDate=wx.StaticText(panel,-1,"Due Date")
        DueDate1=wx.TextCtrl(panel,-1," ");

        AmountAfterRs=wx.StaticText(panel,-1,"Amount After Due Date Rs")
        AmountAfterRs1=wx.TextCtrl(panel,-1," ");


        Remark=wx.StaticText(panel,-1,"  ")
        Remark1=wx.TextCtrl(panel,-1," ");



        saveBtn = wx.Button(panel, -1, "Save")
        cancelBtn = wx.Button(panel, -1, "Cancel")
        nextBtn = wx.Button(panel, -1, "Next")
        PvsBtn = wx.Button(panel, -1, "Previous")

        # Now do the layout.

        # mainSizer is the top-level one that manages everything
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(topLbl, 0, wx.CENTER, 5)
        mainSizer.Add(middleLbl,0,wx.CENTER,5)
        mainSizer.Add(lastLbl,0,wx.CENTER,5)
        mainSizer.Add(wx.StaticLine(panel), 0,
                wx.EXPAND|wx.TOP|wx.BOTTOM, 5)

        # addrSizer is a grid that holds all of the address info
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)

        addrSizer.Add(nameLbl, 0,
                wx.ALIGN_LEFT,wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(name, 0,wx.ALIGN_LEFT,wx.SHAPED|wx.EXPAND)

        addrSizer.Add(addrLbl, 0,wx.ALIGN_LEFT,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(addr1, 0, wx.EXPAND)

        addrSizer.Add((10,10)) # some empty space
        addrSizer.Add(addr2, 0, wx.EXPAND)

        addrSizer.Add(BillDate, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)

        # the city, state, zip fields are in a sub-sizer
        cstSizer = wx.BoxSizer(wx.HORIZONTAL)
        cstSizer.Add(Day, 1)
        cstSizer.Add(Month, 0, wx.LEFT|wx.RIGHT, 5)
        cstSizer.Add(Year)
        addrSizer.Add(cstSizer, 0, wx.EXPAND)

        addrSizer.Add(MeterNo, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(MeterNo1, 0, wx.EXPAND)

        #4Meter Reading Box
        addrSizer.Add(MeterReading, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(Previous, 0, wx.EXPAND)

        addrSizer.Add((10,10)) # some empty space
        addrSizer.Add(Current, 0, wx.EXPAND)

        #5total units
        addrSizer.Add(TotalUnits, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(TotalUnits1, 0, wx.EXPAND)

        #6Rate_units
        addrSizer.Add(Rate_Units, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(Rate_Units1, 0, wx.EXPAND)

        #7Amount
        addrSizer.Add(Amount, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(Amount1, 0, wx.EXPAND)

        #8FixedCharges

        cstSizer.Add(Load, 1)
        cstSizer.Add(Rate_Rs, 0, wx.LEFT|wx.RIGHT, 5)
        #cstSizer.Add(Amount_Rs,0,wx.LEFT|wx.RIGHT,10)
        cstSizer.Add(Amount_Rs)
        addrSizer.Add(cstSizer, 0, wx.EXPAND)

        #9TotalRs
        addrSizer.Add(TotalRs, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(TotalRs1, 0, wx.EXPAND)

        #10Maintaine
        addrSizer.Add(MaintainceRs, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(MaintainceRs1, 0, wx.EXPAND)

        #11GrandTotal
        addrSizer.Add(GrandTotalRs, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(GrandTotalRs1, 0, wx.EXPAND)

        #12Previous_Due_RS
        addrSizer.Add(PreviousDueRs, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(PreviousDueRs1, 0, wx.EXPAND)

        #13Payment_REc_RS
        addrSizer.Add(PaymentRecRs, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(PaymentRecRs1, 0, wx.EXPAND)

        #14CurrentChargesRs
        addrSizer.Add(CurrentChrRs, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(CurrentChrRs1, 0, wx.EXPAND)

        #15TotalAmountRs
        addrSizer.Add(TotalAmountDueRs, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(TotalAmountDueRs1, 0, wx.EXPAND)

        #16DueDate
        addrSizer.Add(DueDate, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(DueDate1, 0, wx.EXPAND)


        #17AmountAfterRS
        addrSizer.Add(AmountAfterRs, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(AmountAfterRs1, 0, wx.EXPAND)

        #18Remark
        addrSizer.Add(Remark, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(Remark1, 0, wx.EXPAND)









        # now add the addrSizer to the mainSizer
        mainSizer.Add(addrSizer, 0, wx.EXPAND|wx.ALL, 10)

        # The buttons sizer will put them in a row with resizeable
        # gaps between and on either side of the buttons
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(saveBtn)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(cancelBtn)
        btnSizer.Add((20,20), 1)

        mainSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)

        panel.SetSizer(mainSizer)

        # Fit the frame to the needs of the sizer.  The frame will
        # automatically resize the panel as needed.  Also prevent the
        # frame from getting smaller than this size.
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)


app = wx.PySimpleApp()
TestFrame().Show()
app.MainLoop()
