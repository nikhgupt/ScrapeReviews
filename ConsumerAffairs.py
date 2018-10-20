
import bs4
import csv

from bs4 import BeautifulSoup as soup
import requests

#defining lists for reviews

Reviewer_Name=[]
Review_Date=[]
Customer_Review=[]
CL_Reply_Date=[]
CL_Reply=[]

#creating excel file

f = open('dataoutput1.csv','w', newline = "")
writer = csv.writer(f)
writer.writerow(['Reviewer Name', 'Review Date', 'Customer Review', 'CL Reply_Date','CL Reply'])

#url of the page
#myurl = "https://www.consumeraffairs.com/cell_phones/centurylink.html?page=5" 


# opening up connection, grabbing the page
pages =[]
for i in range(1,3):
    url= "https://www.consumeraffairs.com/cell_phones/centurylink.html?page=" + str(i)
    print(url)
    pages.append(url)
    

for item in pages:
    print(item)
    page=requests.get(item)
    page_html=page.content

#html parsing
    page_soup = soup(page_html, "html.parser")

#grab each product
#containers = page_soup.findAll("div", {"class" : "rvw-aut__inf"})

#print(containers)

    for reviewer in page_soup.findAll("div", {"class" : "rvw js-rvw"}):
        rev_name = reviewer.find("strong", {"class" : "rvw-aut__inf-nm"}).contents[0]
        Rviewer_Name = str(rev_name)
        print ("Reviewer Name: " + Rviewer_Name)
        Reviewer_Name.append(Rviewer_Name)
    
 #   rev_rating = reviewer.find("div", {"class" : "rvw__hdr-stat"}, id="img data-rating")
 #   print ("Rating :" + str(rev_rating))
 
        rev_date = reviewer.find("span", {"class" : "ca-txt-cpt ca-txt--clr-gray"}).contents[0]
        Rvw_Date = str(rev_date)
#    print ("Review Date: " + Rvw_Date)
        Review_Date.append(Rvw_Date)
    
        rev_review = reviewer.find("div", {"class" :"rvw-bd ca-txt-bd-2"}).findAll('p')
        print("Review Comment of User")
        for p in rev_review[1:]:
            Cstmr_Review=p.text
        #        print (Cstmr_Review)
            Customer_Review.append(str(Cstmr_Review))

        try: 
            
            cl_replydate = reviewer.find("div", {"class" :"rvw-comp-resp__aut"}).time.text
            CL_Rply_Date = str(cl_replydate)
#    print ("CL Reply Date: " + CL_Rply_Date)
            CL_Reply_Date.append(CL_Rply_Date)
    
            cl_reply = reviewer.find("div", {"class" :"rvw-comp-resp__txt ca-txt-bd-2"}).findAll('p')
            print("CenturyLink Reply")
            for p in cl_reply:
                CL_Rply = p.text
#        print (CL_Rply)
                CL_Reply.append(CL_Rply)
        except:
            CL_Rply_Date = None
            CL_Reply_Date.append(CL_Rply_Date)
            CL_Rply = None
            CL_Reply.append(CL_Rply)
       
        writer.writerow([Rviewer_Name, Rvw_Date,'.'.join(Customer_Review), CL_Rply_Date, CL_Rply])
        Customer_Review.clear()
