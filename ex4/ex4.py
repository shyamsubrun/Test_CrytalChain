import requests
import json


def getTopicCount(s):
    url ="https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=pizza"
    
    rep= requests.get(url)
    #stock url
    if rep.status_code == 200:      #si le lien est valide
        data= json.loads(rep.text)  # on stocke tout le texte dans un fichier json
       
        text = data['parse']['text']['*']   # on le met sous format
        #soup = BeautifulSoup(response.text, 'html.parser')
        count = text.count(s)           # on compte le nombre dapparitions
        print(count)
    else:
        print("pror")
        
        
getTopicCount("pizza")