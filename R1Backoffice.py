import unittest
from selenium import webdriver
import time

# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys


class TestScripts(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        
        inst.driver = webdriver.Chrome()
        inst.driver.maximize_window()
        # navigate to the application home page
        
        inst.driver.get("http://your url.com")
        inst.driver.title

    def test_01_loginpage(self):
        "Step 1: Click on Dropdown input box and Select R1 backoffice Step 2: Click on username and enter various valid and invalid username      Step 3: Click on Password and enter various valid and invalid password      Step 4: Click on Sign in button"  
        
        self.driver.find_element_by_id("brandtype").send_keys("R1 Backoffice")
        li = ['kartik', 'ajit', 'arman','ahgdh','ashish']
        li1 = ['asdjf', '12345', '123784','dasnvdsvhdsb','1234']
        length1 =len(li)
#         length2 = len(li1)
        for i in range(length1):
                self.driver.find_element_by_id('loginname_1').clear()
                self.driver.find_element_by_id('password').clear()

                self.driver.find_element_by_id('loginname_1').send_keys(li[i])
    
                time.sleep(1)
                self.driver.find_element_by_id('password').send_keys(li1[i])
                time.sleep(1)
                self.driver.find_element_by_id('loginbtn1').click()
                time.sleep(1)
                try:
                    pageSource = self.driver.page_source
                    self.assertTrue("Game Report" in pageSource)   
#                     print("Successfully login")
                except: 
#                     print("Wrong loginID")
                    continue
    def test_02_accounts_accountledger(self):  
        "Step 1: Click on Account Report Step 2: Click on Agent Ledger Step 3: Click on Agent name and select input field for all agent and enter name ajit Step 4: Select From date Step 5: Select To date Step 6: Click on submit button"
        
        self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
        self.select_field.click() 
        time.sleep(2)       
        self.driver.find_element_by_xpath(".//*[@id='lbo_input_agentmyledger.php?description=Agent Ledger&menucode=493']").click()
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent"))
        self.driver.find_element_by_id("agentdata").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='dialog-table']/div[2]/label[1]/span").click()
        time.sleep(1)
        self.driver.find_element_by_id("searchData").send_keys("aji")
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='Ajit Agency,AA13,ajit']/u").click()
        time.sleep(1) 
        self.driver.find_element_by_id("fromdate").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()   
        time.sleep(1)
        self.driver.find_element_by_id("todate").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()   
        time.sleep(1)
        self.driver.find_element_by_name("submit").click()
        time.sleep(4)
             
             
    def test_03_accounts_agentwisebalance(self):  
        "Step 1: Click on Account Report Step 2: Click on Agent wise report Step 3: Select any Sale date Step 4: Click on radio box of any alphabet Step 5:Click on View Step 6:Click on Generate Excel"
            
        self.driver.switch_to_default_content()
        self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
        self.select_field.click() 
        time.sleep(2)       
        self.driver.find_element_by_xpath(".//*[@id='lbo_agentwisebalance.php?description=Agentwise Balance&menucode=181']").click()
        time.sleep(2)
        self.driver.find_element_by_class_name("ui-icon-close").click()
        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent1"))
        self.driver.find_element_by_id("saledate").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
        time.sleep(1) 
        for i in range(1,2): 
            self.driver.find_element_by_xpath("html/body/form[2]/center/table/tbody/tr[2]/td/label["+str(i)+"]/span").click()
            self.driver.find_element_by_id("send").click()
            time.sleep(2)
            self.driver.find_element_by_id("excel").click()
            time.sleep(2)
        self.driver.switch_to_default_content()
    
    def test_04_accounts_accountcollection(self):
        "Step 1: Click on Account Report Step 2: Click on Collection Step 3: Click on Date from Step 4:Click on submit button"
        
        self.driver.switch_to_default_content()
        self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
        self.select_field.click() 
        time.sleep(2)       
        self.driver.find_element_by_xpath(".//*[@id='lbo_collectionReport.php?description=Collection&menucode=182']").click()
        time.sleep(2)       
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent1"))
        self.driver.find_element_by_id("from").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
        time.sleep(1)
        self.driver.find_element_by_id("submitButton").click()
        time.sleep(1)
        self.driver.switch_to_default_content()
    
            
    def test_05_accounts_debitcreditnote(self):
        "Step 1: Click on Account Report Step 2: Click on Debit/Credit note Step 3: Click on cross button of other tab Step 4: Click on From and Select any date Step 5: Click on Submit button"
        
        self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
        self.select_field.click() 
        time.sleep(2)       
        self.driver.find_element_by_xpath(".//*[@id='lbo_debitcreditnote.php?description=Debit/Credit Note&menucode=183']").click()
        time.sleep(2)       
        self.driver.find_element_by_class_name("ui-icon-close").click()
        time.sleep(1) 
        self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent2"))
        self.driver.find_element_by_id("from").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
        time.sleep(1)
        self.driver.find_element_by_id("submitButton").click()
        time.sleep(1)
        self.driver.switch_to_default_content()
    
    def test_06_accounts_pwt(self):
        "Step 1: Click on Account Report Step 2: Click on Pwt Step 3: Click on From date and select any date Step 4: Click on Show button Step 5: Click on Excel button Step 6: Click on back button"    
        
        self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
        self.select_field.click() 
        time.sleep(2)       
        self.driver.find_element_by_xpath(".//*[@id='lbo_excess_pwtreport.php?description=Pwt&menucode=471']").click()
        time.sleep(2)       
        self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent2"))
        self.driver.find_element_by_id("fromdate").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
        time.sleep(1)
        self.driver.find_element_by_id("showall").click()
        time.sleep(1)
        self.driver.find_element_by_id("excel").click()
        time.sleep(1)
        self.driver.find_element_by_class_name("button--rayen").click()
        time.sleep(1)
        self.driver.switch_to_default_content()
         
    def test_07_accounts_pwtgovernmentwise(self):
        "Step 1: Click on Account Report Step 2: Click on Pwt Governmentwise Step 3: Click on From date and Select any date Step 4: Click on Govt name and select all Step 5 :Click on show Step 6: Click on excel Step 7: Click on back button" 
        
        self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
        self.select_field.click() 
        time.sleep(2)       
        self.driver.find_element_by_xpath(".//*[@id='pwd_govtwisesale.php?description=Pwt Governmentwise&menucode=545']").click()
        time.sleep(2)       
        self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent3"))
        self.driver.find_element_by_id("fromdate").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
        time.sleep(1)
        self.search_class = self.driver.find_element_by_id("govtcode").send_keys("ALL")
        self.driver.find_element_by_id("showall").click()
        time.sleep(1)
        self.driver.find_element_by_id("excel").click()
        time.sleep(1)
        self.driver.find_element_by_class_name("button--rayen").click()
        time.sleep(1)
        self.driver.switch_to_default_content()
    
    def test_08_accounts_agentreceiptreport(self):
        "Step 1: Click on Account Report Step 2: Click on Agent Receipt Report Step 3: Click on From date and Select any date Step 4: Click on To date and select any date Step 5:Click on Show button"          
           
        self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
        self.select_field.click() 
        time.sleep(2)       
        self.driver.find_element_by_xpath(".//*[@id='AgentReceiptReport.php?description=Agent Receipt Report&menucode=667']").click()
        time.sleep(2)       
        self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent4"))
        self.driver.find_element_by_id("fromdate").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()   
        time.sleep(1)
        self.driver.find_element_by_id("todate").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()   
        time.sleep(1)
        self.driver.find_element_by_id("show").click()
        time.sleep(1)
        self.driver.switch_to_default_content()
    
#     def test_09_accounts_paymentledger(self):
#       
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)       
#         self.driver.find_element_by_xpath(".//*[@id='lbo_paymentLedger.php?description=Payment Ledger&menucode=184']").click()
#         time.sleep(2)       
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent5"))
#         self.driver.find_element_by_id("from").click()
#         time.sleep(1)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()   
#         time.sleep(1)
#         self.driver.find_element_by_id("to").click()
#         time.sleep(1)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()   
#         time.sleep(1)
#         self.driver.find_element_by_id("findInput").click()
#         time.sleep(1)
#         self.driver.find_element_by_id("searchData").send_keys("aji")
#         time.sleep(1)
#         self.driver.find_element_by_xpath(".//*[@id='Ajit Agency,AA13,ajit']/u").click()   
#         time.sleep(1)
#         self.driver.find_element_by_id("submitButton").click()
#         time.sleep(1)
#         self.driver.switch_to_default_content()
#    
#                                
#     def test_10_accounts_pwtgovtaprilmayjune(self):
#             
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)       
#         self.driver.find_element_by_xpath(".//*[@id='old/pwt_sale.php?description=Pwt Govt. April.May.June.16&menucode=658']").click()
#         time.sleep(2)       
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent6"))
#         self.driver.find_element_by_id("fromdate").click()
#         time.sleep(1)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()   
#         time.sleep(1)
#         self.driver.find_element_by_id("todate").click()
#         time.sleep(1)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()   
#         time.sleep(1)
#         self.search_class = self.driver.find_element_by_id("govtcode").send_keys("ALL")
#         self.driver.find_element_by_id("submit").click()
#         time.sleep(1)
#         self.driver.switch_to_default_content()
#    
#     def test_11_Sale_Gamewisesalereport(self):
#            
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)       
#         self.driver.find_element_by_xpath(".//*[@id='lbo_gamewisesalereport.php?description=Gamewise Sale Report&menucode=388']").click()
#         time.sleep(2)       
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent7"))
#         self.driver.find_element_by_id("gameid").send_keys("ALL")
#         time.sleep(1)
#         self.driver.find_element_by_id("txtDate").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("ui-datepicker-month").send_keys("Jun")
#         time.sleep(1)
#         self.driver.find_element_by_id("generateexcel").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(1)
#         self.driver.switch_to_default_content()
#    
#     def test_12_Sale_MRPSale(self):
#     
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)       
#         self.driver.find_element_by_xpath(".//*[@id='old/input_agent.php3?description=MRP Sale&menucode=399']").click()
#         time.sleep(2)       
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent8"))
#         self.driver.find_element_by_id("agentdata").click()
#         time.sleep(1)
#         self.driver.find_element_by_id("searchData").send_keys("aji")
#         time.sleep(1)
#         self.driver.find_element_by_xpath(".//*[@id='Ajit Agency,AA13,ajit']/u").click()   
#         time.sleep(1)
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(1)
#         self.driver.find_element_by_id("cmbgame").send_keys("All Game")
#         time.sleep(1)
#         self.driver.find_element_by_id("retcode").send_keys("All Retailer")
#         time.sleep(1)
#         self.driver.find_element_by_id("fromdate").click()
#         time.sleep(1)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()   
#         time.sleep(1)
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("button--border-thick").click()
#         time.sleep(1)
#         self.driver.switch_to_default_content()
#     
#     def test_13_Sale_Nosalecounter(self):
#              
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)       
#         self.driver.find_element_by_xpath(".//*[@id='lbo_nosalereport.php?description=No Sale Counters&menucode=174']").click()
#         time.sleep(2)       
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent8"))
#         self.driver.find_element_by_id("fromdate").click()
#         time.sleep(1)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()   
#         time.sleep(1)
#         self.driver.find_element_by_id("agcode").send_keys("All counters")
#         self.driver.find_element_by_id("send").click()
#         time.sleep(5)
#         self.driver.switch_to_default_content()
#     
#     def test_14_Sale_Zonewisesalereport(self):
#             
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_zonewisesalereport.php?description=Zonewise Sale Report&menucode=389']").click()
#         time.sleep(2)       
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent9"))
#         self.driver.find_element_by_id("typeid").send_keys("Both")
#         time.sleep(1)
#         self.driver.find_element_by_id("generateexcel").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(1)
#         self.driver.switch_to_default_content()
#        
#         
#     def test_15_Agt_agentvoice(self):
#             
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_ag_input_invoice.php?description=Agent Invoice&menucode=382']").click()
#         time.sleep(2)       
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent10"))
#         self.driver.find_element_by_id("fromdate").click()
#         time.sleep(1)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()   
#         time.sleep(1)
#         self.driver.find_element_by_id("todate").click()
#         time.sleep(1)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()   
#         time.sleep(1)
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(1)
#         self.driver.switch_to_default_content()
#          
#          
#     def test_16_Agt_backofficeoptionrights(self):
#          
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_bousermasterrightreport.php?description=Backoffice Options Rights&menucode=302']").click()
#         time.sleep(2)       
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent11"))
#         self.driver.find_element_by_name("flag").click()
#         time.sleep(2)
#         self.driver.switch_to_default_content()
# 
#          
#          
#     def test_17_Agt_datewiseretailerstatus(self):
#         
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_blockedretailers_datewise.php?description=Date Wise Retailer Status&menucode=483']").click()
#         time.sleep(2)       
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent12"))
#         self.driver.find_element_by_id("fdate").click()
#         time.sleep(2)               
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
#         time.sleep(2)              
#         self.driver.find_element_by_id("show").click()
#         time.sleep(2)       
#         self.driver.find_element_by_id("generate").click()
#         time.sleep(2)       
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(2)       
#         self.driver.switch_to_default_content()
#       
#     def test_18_Agt_deleteloginreport(self):
#         
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_logindeletereport.php?description=Delete Login (R-POS) Report&menucode=266']").click()
#         time.sleep(2)       
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent13"))
#         self.driver.find_element_by_id("fdate").click()
#         time.sleep(2)               
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
#         time.sleep(2)              
#         self.driver.find_element_by_id("show").click()
#         time.sleep(2)       
#         self.driver.find_element_by_id("excel").click()
#         time.sleep(2)       
#         self.driver.switch_to_default_content()
# 
#         
#         
#     def test_19_Agt_invoice(self):
#        
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_input_invoice.php?description=Invoice&menucode=171']").click()
#         time.sleep(2)       
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent14"))
#         self.driver.find_element_by_id("fromdate").click()
#         time.sleep(2)       
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
#         time.sleep(2)              
#         self.driver.find_element_by_xpath("tr[2]/td[2]/a").click()
#         time.sleep(2)              
# 
#         
#     def test_20_Agt_invoice(self):
        
        
        
   
#     def test_16_utility_MDNNowisedetail(self):
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_mdnwiserecord.php?description=MDN No wise detail&menucode=492']").click()
#         time.sleep(2)       
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent11"))
#         self.driver.find_element_by_id("tbox_searchmdn").send_keys("11234555")
#         time.sleep(1)
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(1)
#         self.driver.find_element_by_id("popup_ok").click()
#         time.sleep(1)
#         self.driver.switch_to_default_content()
#    
#        
#     def test_17_utility_paperroll(self):
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_paperrollreport.php?description=Paper Roll&menucode=292']").click()
#         time.sleep(2)    
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)   
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent12"))
#         self.driver.find_element_by_id("rollength").send_keys("10")
#         time.sleep(2)       
#         self.driver.find_element_by_id("tktlength").send_keys("10")
#         time.sleep(2)               
#         self.driver.find_element_by_id("fromdate").click()
#         time.sleep(2)       
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
#         time.sleep(2)               
#         self.driver.find_element_by_id("todate").click()
#         time.sleep(2)       
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
#         time.sleep(2)       
#         self.driver.find_element_by_id("generateexcel").click()
#         time.sleep(2)       
#         self.driver.switch_to_default_content()
#   
#     def test_18_utility_phonecapturing(self):
#   
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_phonedurationcapture.php?description=Phone Capturing Duration&menucode=264']").click()
#         time.sleep(2)    
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent12"))
#         for rows in range(1,6):
#             for cols in range(1,8):
#                 time.sleep(1)
#                 self.driver.find_element_by_id("date").click()
#                 try:
#                     self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr["+str(rows)+"]/td["+str(cols)+"]/a").click()
#                     self.driver.find_element_by_id("submit").click()
#                 except NoSuchElementException:
#                     continue
# #                 self.driver.find_element_by_id("submit").click()
#         time.sleep(3)       
#   
#         self.driver.switch_to_default_content()
#   
#     def test_19_utility_phonecapturingretwise(self):
#       
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_phonedurationcapture_retwise.php?description=Phone Capturing Duration (Ret. Wise)&menucode=265']").click()
#         time.sleep(2)    
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent13"))
#         self.driver.find_element_by_id("tbox_searchretailer").click()
#         time.sleep(1)
#         self.driver.find_element_by_id("searchData").send_keys("ajit")
#         time.sleep(1)
#         self.driver.find_element_by_xpath(".//*[@id='Ajit Enterprise45031,45031,R10402179']/u").click()
#         time.sleep(1)
# #         for rows in range(1,6):
# #             for cols in range(1,8):
# #                 time.sleep(1)
#         self.driver.find_element_by_id("fdate").click()
# #                 try:
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
#         self.driver.find_element_by_name("show").click()
# #                 except NoSuchElementException:
# #                     continue
# # #                 self.driver.find_element_by_id("submit").click()
#         time.sleep(3)       
#   
#         self.driver.switch_to_default_content()
#   
#     def test_20_utility_retaileripcheck(self):
#           
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='old/retaileripcheck.php?description=Retailer IP Check&menucode=263']").click()
#         time.sleep(2)    
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent14"))
#         self.driver.find_element_by_id("agentdata").click()
#         time.sleep(2)    
#         self.driver.find_element_by_id("searchData").send_keys("ajit")
#         time.sleep(2)    
#         self.driver.find_element_by_xpath(".//*[@id='AJIT SHARMA13713,13713,0309112']/u").click()
#         time.sleep(2)    
#         self.driver.find_element_by_name("submit").click()
#         time.sleep(2)    
#         self.driver.switch_to_default_content()
#      
#   
#     def test_21_utility_vpncapturingduration(self):
#           
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='datewisevpndetails.php?description=VPN Capturing Duration&menucode=521']").click()
#         time.sleep(2)    
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent15"))
#         self.driver.find_element_by_id("month").send_keys("june")
#         time.sleep(2)
#         self.driver.find_element_by_id("year").send_keys("2017")
#         time.sleep(2)
#         self.driver.find_element_by_id("excel").click()
#         time.sleep(2)
#         self.driver.switch_to_default_content()
#    
#     def test_22_govtreport_detailedgovtreport(self):
#           
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='old/input_govtreport.php3?description=Detailed Govt Report&menucode=177']").click()
#         time.sleep(2)    
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent16"))
#         self.driver.find_element_by_id("gamename").send_keys("All")
#         time.sleep(2)   
#         self.driver.find_element_by_xpath(".//*[@id='d2']/table/tbody/tr[2]/td/label[1]/span").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("fromdate").click()
#         time.sleep(2)   
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[1]").send_keys("Jun") 
#         time.sleep(2)   
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click() 
#         time.sleep(2)   
#         self.driver.find_element_by_name("submit").click()
#         time.sleep(2)    
#         self.driver.switch_to_default_content()
#      
#     def test_23_govtreport_govtwinnerdetails(self):
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='govtwinner_brandwise_report.php?description=Govt Winners Details&menucode=392']").click()
#         time.sleep(2)
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
#         self.driver.find_element_by_class_name("ui-icon-close").click()
#         time.sleep(1)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent17"))
#         time.sleep(2)
#         self.driver.find_element_by_id("fromdate").click()
#         time.sleep(2)   
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click() 
#         time.sleep(2)        
#         self.driver.find_element_by_id("todate").click()
#         time.sleep(2)   
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click() 
#         time.sleep(2)   
#         self.driver.find_element_by_id("gamecode").send_keys("online")
#         time.sleep(2)   
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(1)
#         self.driver.switch_to_default_content()
#     
#     def test_24_govtreport_govtwisesalereport(self):
#         
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='old/govtwisesale.php3?description=GOVTWISE SALE REPORT&menucode=336']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent18"))
#         time.sleep(2)
#         self.driver.find_element_by_id("fromdate").click()
#         time.sleep(2)   
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click() 
#         time.sleep(2) 
#         self.driver.find_element_by_id("todate").click()
#         time.sleep(2)   
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click() 
#         time.sleep(2)
#         self.driver.find_element_by_id("govtcode").send_keys("All")
#         time.sleep(2)   
#         self.driver.find_element_by_id("submit").click()
#         time.sleep(2)   
#         self.driver.switch_to_default_content()
# 
#      
#     
#     def test_25_govtreport_purchasesalesummarydatewise(self):
#         
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='purchaseSaleSummeryDatewise.php?description=Purchase Sale Summary Datewise&menucode=562']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent19"))
#         time.sleep(2)
#         self.driver.find_element_by_id("fromdate").click()
#         time.sleep(2)   
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click() 
#         time.sleep(2) 
#         self.driver.find_element_by_id("todate").click()
#         time.sleep(2)   
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click() 
#         time.sleep(2)
#         self.driver.find_element_by_id("govttype").send_keys("Govt. of sikkim")
#         time.sleep(2)
#         self.driver.find_element_by_id("rate1").send_keys("10")
#         time.sleep(2)
#         self.driver.find_element_by_id("rate2").send_keys("10")
#         time.sleep(2)
#         self.driver.find_element_by_name("excel").click()
#         time.sleep(2)    
#         self.driver.switch_to_default_content()
#     
#     def test_26_govtreport_purchasesalesummarydrawdatewise(self):
#         
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='purchaseSaleSummery.php?description=Purchase Sale Summary Drawdate Wise&menucode=516']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent20"))
#         time.sleep(2)
#         self.driver.find_element_by_id("fromdate").click()
#         time.sleep(2)   
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click() 
#         time.sleep(2) 
#         self.driver.find_element_by_id("todate").click()
#         time.sleep(2)   
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click() 
#         time.sleep(2)
#         self.driver.find_element_by_id("govttype").send_keys("Govt. of sikkim")
#         time.sleep(2)
#         self.driver.find_element_by_id("rate1").send_keys("10")
#         time.sleep(2)
#         self.driver.find_element_by_id("rate2").send_keys("10")
#         time.sleep(2)
#         self.driver.find_element_by_name("excel").click()
#         time.sleep(2)    
#         self.driver.switch_to_default_content()
#     
#     
#     def test_27_govtreport_winover10k(self):
#   
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='govtwinover5k.php?description=Win Over 10K&menucode=317']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent21"))
#         time.sleep(2)
#         self.driver.find_element_by_id("game").send_keys("Online")
#         time.sleep(2)   
#         self.driver.find_element_by_id("govtname").send_keys("All")
#         time.sleep(2)   
#         self.driver.find_element_by_id("fdate").click()
#         time.sleep(2)   
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[1]").click()
#         time.sleep(2) 
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[2]/a").click()
#         time.sleep(2)     
#         self.driver.find_element_by_name("submit").click()
#         time.sleep(3)
#         self.driver.find_element_by_id("excel").click()
#         time.sleep(2)   
#         self.driver.switch_to_default_content()
#       
#     
#     def test_28_otherreport_agentwiselimit(self):
#         
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='old/agentwisecrlimit.php3?description=Agent Wise Limit&menucode=271']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent22"))
#         time.sleep(2)
#         for i in range(1,2): 
#             self.driver.find_element_by_xpath("html/body/form/table[1]/tbody/tr[2]/td/label["+str(i)+"]/span").click()
#             self.driver.find_element_by_class_name("button--rayen").click()
#             time.sleep(2)
#             self.driver.find_element_by_id("excel").click()
#             time.sleep(2)
#         self.driver.switch_to_default_content()
# 
#     def test_29_otherreport_agentwiseuserloginstatus(self):
#         
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_userloginstatusreport.php?description=Agent Wise User Login Status&menucode=270']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent23"))
#         time.sleep(2)
#         self.driver.find_element_by_xpath("html/body/form/div/table/tbody/tr/td[1]/label[1]/span").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("btnFind").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("excel").click()
#         time.sleep(2)
#         self.driver.switch_to_default_content()
#   
#     def test_30_otherreport_loginmonitor(self):
#     
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_loginMonitor.php?description=Login Monitor&menucode=286']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent24"))
#         time.sleep(2)
#         for i in range(1,2): 
#             self.driver.find_element_by_xpath(".//*[@id='table2']/tbody/tr[2]/td["+str(i)+"]/span").click()
#             self.driver.find_element_by_id("show").click()
#             time.sleep(2)
#             self.driver.find_element_by_id("excel").click()
#             time.sleep(2)       
#         self.driver.switch_to_default_content()
#   
#      
#     def test_31_otherreport_mrpwisetransaction(self):
#          
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_mrpwisetransaction.php?description=MRP WIse Transaction&menucode=275']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent25"))
#         time.sleep(2)
#         self.driver.find_element_by_id("gamecode").send_keys("Online")
#         time.sleep(2)
#         self.driver.find_element_by_id("date").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[6]/a").click()
#         time.sleep(2)
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("excel").click()
#         time.sleep(2)
#         self.driver.find_element_by_name("back").click()
#         time.sleep(2)
#         self.driver.switch_to_default_content()
# 
#     def test_32_otherreport_mrpwisetransactioncombine(self):
#         
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_mrpwisetransaction_combine.php?description=MRP WIse Transaction ( Combine )&menucode=649']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent26"))
#         time.sleep(2)
#         self.driver.find_element_by_id("gamecode").send_keys("Online")
#         time.sleep(2)
#         self.driver.find_element_by_id("date").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[6]/a").click()
#         time.sleep(2)
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("excel").click()
#         time.sleep(2)
#         self.driver.find_element_by_name("back").click()
#         time.sleep(2)
#         self.driver.switch_to_default_content()
# 
# 
#     def test_33_otherreport_mumbaiincentive(self):
#         
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='MumbaiIncentiveScheme.php?description=Mumbai Incentive Scheme&menucode=657']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent27"))
#         time.sleep(2)
#         self.driver.find_element_by_id("search").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("searchData").send_keys("ajit")
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='Ajit Agency,AA13,ajit']/u").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("excel").click()
#         time.sleep(2)
#         self.driver.switch_to_default_content()
# 
#     
#     def test_34_otherreport_newretailerlist(self):
# 
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='newcounters.php?description=New Retailers List&menucode=291']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent28"))
#         time.sleep(2)
#         self.driver.find_element_by_name("noofdays").send_keys("5")
#         time.sleep(2)
#         self.driver.find_element_by_name("submit").click()
#         time.sleep(2)
#         self.driver.switch_to_default_content()
# 
#     
#     def test_35_otherreport_retailercurrentstatus(self):
#         
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='old/input_agent.php3?description=Retailer Current Status&menucode=283']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent29"))
#         time.sleep(2)
#         self.driver.find_element_by_id("search").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("searchData").send_keys("ajit")
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='Ajit Agency,AA13,ajit']/u").click()
#         time.sleep(2)
#         self.driver.find_element_by_name("submitq").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("excel").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath("html/body/form[2]/button[1]").click()
#         time.sleep(2)
#         self.driver.switch_to_default_content()
# 
#     
#     def test_36_otherreport_retailertransfer(self):
#         
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_transferretailerreport_ui.php?description=Retailer Transfer&menucode=273']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent30"))
#         time.sleep(2)
#         self.driver.find_element_by_id("sdate").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[7]/a").click()
#         self.driver.find_element_by_id("search").click()
#         time.sleep(2)
#         self.driver.find_element_by_name("submit").click()
#         time.sleep(2)
#         self.driver.find_element_by_name("excel").click()
#         time.sleep(2)
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(2)
#         self.driver.switch_to_default_content()
#         
#     def test_37_otherreport_retailerlistscheme(self):
# 
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_retailerslistscheme.php?description=Retailers List Scheme&menucode=268']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent31"))
#         time.sleep(2)
#         self.driver.find_element_by_id("fdate").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[7]/a").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("tdate").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[2]/a").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("fromamt").send_keys("500")
#         time.sleep(2)
#         self.driver.find_element_by_id("toamt").send_keys("500")
#         time.sleep(2)
#         self.driver.find_element_by_id("show").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("generate").click()
#         time.sleep(2)
#                             
#     def test_38_otherreport_transactiondetails(self):
#     
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='old/input_agent.php3?description=Transaction Details&menucode=290']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent32"))
#         time.sleep(2)
#         self.driver.find_element_by_id("agentdata").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("searchData").send_keys("ajit")
#         time.sleep(2)
#         self.driver.find_element_by_name("submitq").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("cmbret").send_keys("Divya Online(07214)")
#         time.sleep(2)
#         self.driver.find_element_by_id("cmbgame").send_keys("Online")
#         time.sleep(2)
#         self.driver.find_element_by_name("submit1").click()
#         time.sleep(2)
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(2)
#         self.driver.switch_to_default_content()
#         
#     def test_39_otherreport_workingterminal(self):
#    
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='old/workingterminal.php3?description=Working Terminal&menucode=287']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent33"))
#         time.sleep(2)
#         self.driver.find_element_by_id("drawdate").click()
#         time.sleep(2)
#         self.driver.find_element_by_name("total").send_keys("5")
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[7]/a").click()
#         time.sleep(2)
#         self.driver.find_element_by_name("sub").click()
#         time.sleep(2)
#         
#     def test_40_register_salesummary(self):
#         
#         self.select_field = self.driver.find_element_by_xpath(".//*[@id='97']")
#         self.select_field.click() 
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='lbo_saleSummary.php?description=Sale Summary&menucode=179']").click()
#         time.sleep(2)
#         self.driver.switch_to.frame(self.driver.find_element_by_id("div_middlecontent34"))
#         time.sleep(2)
#         self.driver.find_element_by_id("from").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[7]/a").click()
#         time.sleep(2)
#         self.driver.find_element_by_id("selectGame").send_keys("All")
#         time.sleep(2)
#         self.driver.find_element_by_id("submitButton").click()
#         time.sleep(2)
#         self.driver.find_element_by_class_name("button--rayen").click()
#         time.sleep(2)
#         self.driver.switch_to_default_content()
#         
#     
#     
    
    
        @classmethod
        def tearDownClass(inst):
        # close the browser window
            inst.driver.quit()
        
        
    
 
if __name__ == '__main__':
    unittest.main()
    
#  text/html; charset=UTF-8   
    
