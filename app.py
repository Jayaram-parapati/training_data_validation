# mongodb mix-entities > load one by one >
# document > text, entities > spacy docbin > try: document["docbin"]=True except: document["docbin"]=False
import pymongo,spacy
from spacy.tokens import DocBin 


client = pymongo.MongoClient("mongodb://localhost:27017")
training_db= client["training_db_080923"]




for obj in mix_entities_list:
        text = obj["text"]
        entities = obj["entities"]
        doc = nlp(text)
        valid_ents = []
        try:
            for start,end,label in entities:
                span = doc.char_span(start,end,label=label)
                if span is None or (span.text.startswith(" ")) or (span.text.endswith(" ")):
                    print("span error")

                else:
                    valid_ents.append([start,end,label])
            doc.ents = valid_ents
            db.add(doc.ents)


        except Exception as F:
            print("exception : ",F)


# db.to_disk("D:\\python\\training_data_validation\\spacyfiles\\traindata.spacy")





    








    