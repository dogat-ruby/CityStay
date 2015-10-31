
import httplib2, gc, sys
import json, yaml, ast

try:
  import Tkinter              
  import ttk
except ImportError:
  import tkinter as Tkinter   
  import tkinter.ttk as ttk

#def __init__(self, mystr=str()):
#   self.mystr = mystr

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
        with open(str(client) + '_' + str(data_type), 'w') as file:
            for chunk in iter(lambda: f.read(chunksize), ''):
                if not chunk:
                    break
                ctr +=1
                mpb["value"] = ctr
                #mystr+=str(chunk)
                chunkStr = str(chunk)
                chunkStr = chunkStr[2:len(chunkStr)-1]
                mystr+=chunkStr
                #~ if ctr == 1:
                    #~ print(chunkStr)
                #~ elif ctr ==2:
                    #~ print(chunkStr)
                #file.write(str(chunk))
                mpb.update()
                #json.dump(mystr, file)
        mGui.destroy()
        #mGui.mainloop()
        f.close()
        gc.collect()    
    except urllib2.HTTPError as e:
        return str(e.code)
    except urllib2.URLError as e:
        return str(e.reason)
    except Exception:
        import traceback
        return str(traceback.format_exc())
        
    #dictStr = ast.literal_eval(mystr)
    newStr = mystr.replace("\\'", "")
    newStr = newStr.replace('\\"', '"')
    #dictStr = yaml.load(newStr)
    #partStr = newStr[111800:112000]
    #partStr = newStr[863180:863200]
    #print(partStr)
    #dictStr = dict(newStr)
    #dictStr = yaml.load(newStr)
    dictStr = json.loads(newStr)
    #print(dictStr)
    return dictStr

if __name__ == "__main__":
    print("Hello")
    fetchDataFromAPI("chicago", "matters")
