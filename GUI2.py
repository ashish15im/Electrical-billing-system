import wx


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Real World Test")


        panel = wx.Panel(self)

        # First create the controls
        topLbl = wx.StaticText(panel, -1, "NEBSARAI EXTN. AREA WELFARE SOCIETY ",style=wx.ALIGN_CENTER)
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

        #middle/BODY/Portions
        nameLbl = wx.StaticText(panel, -1, "Name:")
        name = wx.TextCtrl(panel, -1, "");

        addrLbl = wx.StaticText(panel, -1, "Address:")
        addr1 = wx.TextCtrl(panel, -1, "");
        addr2 = wx.TextCtrl(panel, -1, "");

        cstLbl = wx.StaticText(panel, -1, "ENTER: DAY/MONTH/YEAR in the format dd/mm/yy")
        city  = wx.TextCtrl(panel, -1, "", size=(150,-1));
        state = wx.TextCtrl(panel, -1, "", size=(50,-1));
        zip   = wx.TextCtrl(panel, -1, "", size=(70,-1));

        phoneLbl = wx.StaticText(panel, -1, "Meter No.:")
        phone = wx.TextCtrl(panel, -1, "");

        emailLbl = wx.StaticText(panel, -1, "Billing Cycle:")
        email = wx.TextCtrl(panel, -1, "");

        billNoLbl = wx.StaticText(panel, -1, "Bill No.:")
        billNo = wx.TextCtrl(panel, -1, "");

        cst1Lbl = wx.StaticText(panel, -1, "Meter Reading=ENTER: Previous and Current Reading")
        pvsReading  = wx.TextCtrl(panel, -1, "", size=(150,-1));
        currReading = wx.TextCtrl(panel, -1, "", size=(50,-1));
        #zip   = wx.TextCtrl(panel, -1, "", size=(70,-1));


        totalUnitsLbl = wx.StaticText(panel, -1, "Total Units:")
        totalUnits = wx.TextCtrl(panel, -1, "");

        ratePerUnitsLbl = wx.StaticText(panel, -1, "Amount Units:")
        ratePerUnits = wx.TextCtrl(panel, -1, "");

        amountUnitsLbl = wx.StaticText(panel, -1, "Amount Units(*)")
        amountUnits = wx.TextCtrl(panel, -1, "");

        totalRsLbl = wx.StaticText(panel, -1, "Total Rs")
        totalRs = wx.TextCtrl(panel, -1, "");

        remarkLbl = wx.StaticText(panel, -1, "Remark")
        remark = wx.TextCtrl(panel, -1, "",size=(100,100));

        maintenanceLbl = wx.StaticText(panel, -1, "Maintenece Rs.")
        maintenance = wx.TextCtrl(panel, -1, "");

        othersLbl = wx.StaticText(panel, -1, "Others Rs.")
        others = wx.TextCtrl(panel, -1, "");

        grandTotalLbl = wx.StaticText(panel, -1, "Grand Total Rs.")
        grandTotal = wx.TextCtrl(panel, -1, "");


        pvsDueLbl = wx.StaticText(panel, -1, "Previous Dues Rs.(1)")
        pvsDue = wx.TextCtrl(panel, -1, "");

        paymentRecLbl = wx.StaticText(panel, -1, "Payment Received Rs.(2)")
        paymentRec = wx.TextCtrl(panel, -1, "");

        currLbl = wx.StaticText(panel, -1, "Current Charges Rs.(3)")
        curr = wx.TextCtrl(panel, -1, "");

        totalDueLbl = wx.StaticText(panel, -1, "Total Amount Dues Rs.(4)")
        totalDue = wx.TextCtrl(panel, -1, "");

        dueDateLbl = wx.StaticText(panel, -1, "Dues date in dd(5)")
        dueDate = wx.TextCtrl(panel, -1, "");

        amountAfterDueDateLbl = wx.StaticText(panel, -1, "Amount After Due Date(6)")
        amountAfterDueDate = wx.TextCtrl(panel, -1, "");














        saveBtn = wx.Button(panel, -1, "Save")
        cancelBtn = wx.Button(panel, -1, "Cancel")

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
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(name, 0, wx.EXPAND)
        addrSizer.Add(addrLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(addr1, 0, wx.EXPAND)
        addrSizer.Add((10,10)) # some empty space
        addrSizer.Add(addr2, 0, wx.EXPAND)

        addrSizer.Add(cstLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)

        # the city, state, zip fields are in a sub-sizer
        cstSizer = wx.BoxSizer(wx.HORIZONTAL)
        cstSizer.Add(city, 0)
        cstSizer.Add(state, 0, wx.LEFT|wx.RIGHT, 5)
        cstSizer.Add(zip)
        addrSizer.Add(cstSizer, 0, wx.EXPAND)

        addrSizer.Add(phoneLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(phone, 0, wx.EXPAND)

        addrSizer.Add(emailLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(email, 0, wx.EXPAND)

        addrSizer.Add(billNoLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(billNo, 0, wx.EXPAND)

        addrSizer.Add(cst1Lbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)

        # the city, state, zip fields are in a sub-sizer
        cst1Sizer = wx.BoxSizer(wx.HORIZONTAL)
        cst1Sizer.Add(pvsReading, 0)
        cstSizer.Add(currReading
                     , 0, wx.LEFT|wx.RIGHT, 5)
        #cstSizer.Add(zip)
        addrSizer.Add(cst1Sizer, 0, wx.EXPAND)


        addrSizer.Add(totalUnitsLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(totalUnits, 0, wx.EXPAND)

        addrSizer.Add(ratePerUnitsLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(ratePerUnits, 0, wx.EXPAND)

        addrSizer.Add(amountUnitsLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(amountUnits, 0, wx.EXPAND)

        addrSizer.Add(totalRsLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(totalRs, 0, wx.EXPAND)

        addrSizer.Add(remarkLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(remark, 0,wx.EXPAND)

        addrSizer.Add(maintenanceLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(maintenance, 0,wx.EXPAND)

        addrSizer.Add(othersLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(others, 0,wx.EXPAND)

        addrSizer.Add(grandTotalLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(grandTotal, 0,wx.EXPAND)

        addrSizer.Add(pvsDueLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(pvsDue, 0,wx.EXPAND)

        addrSizer.Add(paymentRecLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(paymentRec, 0,wx.EXPAND)

        addrSizer.Add(currLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(curr, 0,wx.EXPAND)

        addrSizer.Add(totalDueLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(totalDue, 0,wx.EXPAND)

        addrSizer.Add(dueDateLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(dueDate, 0,wx.EXPAND)

        addrSizer.Add(amountAfterDueDateLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(amountAfterDueDate, 0,wx.EXPAND)
























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
