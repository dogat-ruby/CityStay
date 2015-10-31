
import httplib2, gc, sys
import json

try:
  import Tkinter              
  import ttk
except ImportError:
  import tkinter as Tkinter   
  import tkinter.ttk as ttk

def fetchDataFromAPI(client, data_type):
    url = 'http://webapi.legistar.com/v1/%s/%s' % (client, data_type)
    mGui = Tkinter.Tk()
    mGui.geometry('300x40')
    mGui.title('Download Progress')
    mpb = ttk.Progressbar(mGui,orient ="horizontal", length = 200, mode ="determinate")
    mpb.pack(padx = 10, pady = 10)
    mystr = str()
    try:
        import urllib.request as urllib2
    except ImportError:
        import urllib2
    try:  
        f = urllib2.urlopen(url)
        chunksize = 16 * 1024
        h = f.info()
        totalsize = int(h["Content-Length"])
        chunkcount = (totalsize // chunksize) + 1
        mpb["maximum"] = chunkcount
        ctr = 0
        for chunk in iter(lambda: f.read(chunksize), ''):
            if not chunk:
                break
            ctr +=1
            mpb["value"] = ctr
            #mystr+=str(chunk)
            chunkStr = str(chunk)
            chunkStr = chunkStr[2:len(chunkStr)-1]
            mystr+=chunkStr
            mpb.update()
        mGui.destroy()
        gc.collect()    
    except urllib2.HTTPError as e:
        return str(e.code)
    except urllib2.URLError as e:
        return str(e.reason)
    except Exception:
        import traceback
        return str(traceback.format_exc())
        
    # Replacing "escape" chars    
    newStr = mystr.replace("\\'", "")
    newStr = newStr.replace('\\"', '"')
    newStr = newStr.replace("\\x", "")
    # Convert to dictionary
    dictStr = json.loads(newStr)
    return dictStr

if __name__ == "__main__":
    fetchDataFromAPI("seattle", "matters")
    print("Seattle: Success")
    fetchDataFromAPI("chicago", "matters")
    print("Chicago: Success")
    fetchDataFromAPI("pittsburgh", "matters")
    print("Pittsburgh: Success")
