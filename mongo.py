from pymongo import MongoClient
client = MongoClient("homer.stuy.edu")
db = client.test
collection = db.restaurants

def borough(x):
    return collection.find({"borough" : x})
def zipcode(x):
    return collection.find({'address.zipcode' : x})

def zipgrade(x,g):
    return collection.find({'address.zipcode' : x, 'grades.grade' : g})
    
def zipscore(x,s):
    return collection.find({'address.zipcode' : x, 'grades.0.score' : {'$lt' : s}})

def bzgs(x,z,g,s):
    return collection.find({"borough" : x, 'address.zipcode' : z, 'grades.grade' : g, 'grades.0.score' : {'$lt' : s}})
def p(x):
    for i in x:
	print d['name']
        
p(borough("Bronx"))
p(zipcode("11214"))
p(zipgrade("11214", "A"))
p(zidscore("11214", 10))

