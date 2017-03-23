import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,ID=-1,label="",pos=wx.DefaultPosition,size=(100,25)):
        wx.Frame.__init__(self, None, -1,pos,size,wx.RAISED_BORDER,"Software")
        panel = wx.Panel(self)
        self.CreateStatusBar()
        menuBar = wx.MenuBar()
        new = wx.Menu()
        simple=new.Append(-1 ,"File", "New")
        exit=new.Append(-1,"Exit","Exited")
        new.AppendSeparator()
        self.Bind(wx.EVT_MENU,self.OnFile,simple)
        self.Bind(wx.EVT_MENU,self.OnExit,exit)
        menuBar.Append(new,"New")
        self.SetMenuBar(menuBar)
        edit = wx.Menu()
        new.AppendSeparator()
        Edit1=edit.Append(-1,"&cut\tCtrl-X")
        edit.AppendSeparator()
        Edit2=edit.Append(-1,"&copy\tCtrl-C")
        edit.AppendSeparator()
        Edit3=edit.Append(-1,"&Paste\tCtrl-V")
        edit.AppendSeparator()
        Edit4=edit.Append(-1,"&Redo\tCtrl-R")
        edit.AppendSeparator()
        Edit5=edit.Append(-1,"&Undo\tCtrl-U")
        edit.AppendSeparator()
        self.Bind(wx.EVT_MENU,self.OnCut,Edit1)
        self.Bind(wx.EVT_MENU,self.OnCopy,Edit2)
        self.Bind(wx.EVT_MENU,self.OnPaste,Edit3)
        self.Bind(wx.EVT_MENU,self.OnRedo,Edit4)
        self.Bind(wx.EVT_MENU,self.OnUndo,Edit5)
        menuBar.Append(edit,"Edit")
        self.SetMenuBar(menuBar)
        view = wx.Menu()
        view1=view.Append(-1,"Print Preview")
        self.Bind(wx.EVT_MENU,self.OnPrintPreview,view1)
        menuBar.Append(view, "View")
        self.SetMenuBar(menuBar)
        help = wx.Menu()
        menuBar.Append(help, "help")
        self.SetMenuBar(menuBar)

        acceltbl=wx.AcceleratorTable([(wx.ACCEL_CTRL,ord('Q'),exit.GetId())])
        self.SetAcceleratorTable(acceltbl)
        #######################################################################################################
        #This is the middle portion of the Gui/Body portion####################################################
        #######################################################################################################
        first1=wx.StaticText(panel,-1,"First Name")
        first2=wx.TextCtrl(panel,-1," ")
        middle1=wx.StaticText(panel,-1,"Middle Name")
        middle2=wx.TextCtrl(panel,-1," ")
        last1=wx.StaticText(panel,-1,"Last Name")
        last2=wx.TextCtrl(panel,-1," ")

        address1=wx.StaticText(panel,-1,"Address")
        address2=wx.TextCtrl(panel,-1," ")

        meter1=wx.StaticText(panel,-1,"Meter Number")
        meter2=wx.TextCtrl(panel,-1," ")

        bill1=wx.StaticText(panel,-1,"Bill Number")
        bill2=wx.TextCtrl(panel,-1," ")

        billingCycle1=wx.StaticText(panel,-1,"Billing Cycle")
        billingCycle2=wx.TextCtrl(panel,-1," ")

        billDate1=wx.StaticText(panel,-1,"Bill Date")
        billDate2=wx.TextCtrl(panel,-1," ")

        meterReading=wx.StaticText(panel,-1,"Meter Reading")
        pvsmeterReading=wx.StaticText(panel,-1,"Previous")
        pvsmeterReading2=wx.TextCtrl(panel,-1," ")
        currmeterReading=wx.StaticText(panel,-1,"Current")
        currmeterReading2=wx.TextCtrl(panel,-1," ")

        totalReading=wx.StaticText(panel,-1,"Total")
        totalReading2=wx.TextCtrl(panel,-1," ")

        Rate_Units=wx.StaticText(panel,-1,"Rate/unit")
        Rate_Units1=wx.TextCtrl(panel,-1," ")

        amount=wx.StaticText(panel,-1,"Amount(*)")
        amount1=wx.TextCtrl(panel,-1," ")


        fixedCharges=wx.StaticText(panel,-1,"Fixed Charges")
        load=wx.StaticText(panel,-1,"load")
        load1=wx.TextCtrl(panel,-1," ")
        rate=wx.StaticText(panel,-1,"Rate Rs")
        rate1=wx.TextCtrl(panel,-1," ")
        amountRs=wx.StaticText(panel,-1,"Amount unit")
        amountRs1=wx.TextCtrl(panel,-1," ")

        TotalRs=wx.StaticText(panel,-1,"Total Rs")
        TotalRs1=wx.TextCtrl(panel,-1," ")

        maintainceRs=wx.StaticText(panel,-1,"Maintenance Rs")
        maintainceRs1=wx.TextCtrl(panel,-1," ")

        OtherRs=wx.StaticText(panel,-1,"Other Rs")
        OtherRs1=wx.TextCtrl(panel,-1," ")
        TotalRs=wx.StaticText(panel,-1," ")
        TotalRs1=wx.TextCtrl(panel,-1," ")

        GrandTotalRs=wx.StaticText(panel,-1,"Grand Total Rs")
        GrandTotalRs1=wx.TextCtrl(panel,-1," ")

        PreviousDueRs=wx.StaticText(panel,-1,"Previous Due Rs")
        PreviousDueRs1=wx.TextCtrl(panel,-1," ")

        PaymentRecRs=wx.StaticText(panel,-1,"Payment Received Rs")
        panelaymentRecRs1=wx.TextCtrl(panel,-1," ")

        CurrentChrRs=wx.StaticText(panel,-1,"Current Charges Rs")
        CurrentChrRs1=wx.TextCtrl(panel,-1," ")

        TotalAmountDueRs=wx.StaticText(panel,-1,"Total Amount Due Rs")
        TotalAmountDueRs1=wx.TextCtrl(panel,-1," ")

        DueDate=wx.StaticText(panel,-1,"Due Date")
        DueDate1=wx.TextCtrl(panel,-1," ")

        AmountAfterRs=wx.StaticText(panel,-1,"Amount After Due Date Rs")
        AmountAfterRs1=wx.TextCtrl(panel,-1," ")



















    def OnFile(self,event):
        wx.MessageBox("You have selected New file")

    def OnExit(self,event):
        self.Close()

    def OnCut(self,event):pass

    def OnPaste(self,event):pass

    def OnCopy(self,event):pass

    def OnRedo(self,event):pass

    def OnUndo(self,event):pass

    def OnPrintPreview(self,event):pass








#if __name__ == "__main__":
app = wx.PySimpleApp()
frame = MyFrame()
frame.Show()
app.MainLoop()


