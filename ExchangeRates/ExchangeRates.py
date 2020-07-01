# Name : Robin Garg
# Roll No : 19092
# Group : 2

import datetime
import urllib.request

def getLatestRates():
        """ Returns: a JSON string that is a response to a latest rates query.
        
        The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
        """
        
        url = urllib.request.urlopen( "https://api.exchangeratesapi.io/latest" )
        data = url.read()
        data=data.decode()
        return data
        
def changeBase(amount, currency, desiredCurrency, date):
        """ Outputs: a float value f.
        Given: date:valid dates and string of format yyyy-mm-dd

        """
        
        urldate="https://api.exchangeratesapi.io/"+date
        url=urllib.request.urlopen(urldate)
        data = url.read()
        data=data.decode()
        x=data.find(currency)
        x2=data.find(desiredCurrency)
        
        
        if currency=='EUR':
                y=1
        else:
                if (data.index('},"',x)-x)<12:
                                z=data.index('}',x)
                else:
                                z=data.index(',"',x)
                y=float(data[slice(x+5,z)])
        if desiredCurrency=='EUR':
                y2=1
        else:
                if (data.index('},"',x2)-x2)<12:
                                z2=data.index('}',x2)
                else:
                                z2=data.index(',"',x2)
                y2=float(data[slice(x2+5,z2)])
        amount=amount/y*y2
        return amount
        




        
def printAscending(json):
        """ Output: the sorted order of the Rates 
                You don't have to return anything.
        
        Parameter:
        json: a json string to parse
        """
        a=json.index("}")
        json=json[0:a]+json[a+1:]
        z=9
        curr=[]
        while(z<json.find('base')-13):
                x=json.index('"',z)
                z=x+1      
                x1=json.index('"',z)
                z=x1+2
                x2=json.index(',',z)
                curr.append(float(json[slice(z,x2)]))
                curr.append(json[slice(x+1,x1)])
        for i in range(0,len(curr),2):
                swap=i
                for j in range(i,len(curr),2):
                        if(curr[swap]>curr[j]):
                                swap=j
                (curr[i], curr[swap]) = (curr[swap], curr[i])
                (curr[i+1], curr[swap+1]) = (curr[swap+1], curr[i+1])
                i+=1
        for i in range(0,len(curr),2):
                print("1 Euro = ",curr[i],curr[i+1])
                
        

def extremeFridays(startDate, endDate, currency):
        """ Output: on which friday was currency the strongest and on which was it the weakest.
                You don't have to return anything.
                
        Parameters: 
        stardDate and endDate: Valid dates strings of the form yyyy-mm-dd
        currency: a string representing the currency those extremes you have to determine
        """
        
        urldate="https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate
        url=urllib.request.urlopen(urldate)
        data = url.read()
        data=data.decode()
        
        wd=[]
        pr=[]
        x=data.find(':{"')
        data=data[:x]+"},"+data[x+2:data.find('start')-4]+'},"'+currency
        import datetime
        y=1
        for z in range(len(data)):
                y=data.index('},"',y+10)
                if y+10>len(data):
                        break
                date1=data[slice(y+3,y+14)]
                yy=int(data[slice(y+3,y+7)])
                mm=int(data[slice(y+8,y+10)])
                dd=int(data[slice(y+11,y+13)])
                date = datetime.datetime( yy ,mm , dd )
                if(data.index('},"',y+10)>data.index(currency,y)):
                        wd.append(date.weekday())
                        wd.append(date1)

        for i in range(0,len(wd),2):
                if(wd[i]==4):
                        x=data.find(wd[i+1])
                        y=data.index(currency,x)
                        if (data.index('},"',y)-y)<12:
                                z=data.index('}',y)
                        else:
                                z=data.index(',"',y)
                        r=float(data[slice(y+5,z)])
                        pr.append(r)
                        pr.append(wd[i+1])
        min=0
        max=0
        for i in range(0,len(pr),2):
                if(pr[min]>pr[i]):
                        min=i
                if(pr[max]<pr[i]):
                        max=i
        if len(pr)==0:
                print("No Friday Found in given range")
        else:
                print(currency,'was strongest on',pr[min+1]+'.','1 Euro was equal to ',pr[min],currency)
                print(currency,'was weakest on',pr[max+1]+'.','1 Euro was equal to ',pr[max],currency)

        
def findMissingDates(startDate, endDate):
        """ Output: the dates that are not present when you do a json query from startDate to endDate
                You don't have to return anything.

                Parameters: stardDate and endDate:valid dates strings of the form yyyy-mm-dd
        """
        ds=[]
        date=[]
        begin = datetime.date(int(startDate[slice(0,4)]),int(startDate[slice(5,7)]),int(startDate[slice(8,10)]))
        end = datetime.date(int(endDate[slice(0,4)]),int(endDate[slice(5,7)]),int(endDate[slice(8,10)]))
        next_day = begin
        while True:
                if next_day > end:
                        break
                ds.append(next_day)
                next_day += datetime.timedelta(days=1)
        urldate="https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate
        url=urllib.request.urlopen(urldate)
        data = url.read()
        data=data.decode()
        x=data.find(':{"')
        data=data[:x]+"},"+data[x+2:data.find('start')-1]
        a=1
        for z in range(len(data)):
                if a<((len(data))-400):
                        
                        y=data.index('},"',a)
                        a=y+100
                        date1=data[slice(y+3,y+14)]
                        yy=int(data[slice(y+3,y+7)])
                        mm=int(data[slice(y+8,y+10)])
                        dd=int(data[slice(y+11,y+13)])
                        date.append(datetime.date( yy ,mm , dd ))
                else:
                        break
        s=-1
        print("The Following dates were not present:")
        for z in range(len(ds)):
                for r in range(len(date)):
                        if ds[z]==date[r]:
                                s=z
                if(s!=z):
                        print(ds[z])

                        
        
        
