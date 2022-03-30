#### Generate Metadata for each Image    
import json

f = open('./1-all.json',) 
data = json.load(f)

# Changes this IMAGES_BASE_URL to yours 
IMAGES_BASE_URL = "ipfs://QmbbFbG5Cp9ALwE1bQCbYpMidhi4zvry645bC5WR1m8JWq/"
PROJECT_NAME = "NFT_CREATOR"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }

j = 0

for i in data:
    token_id = i['tokenId']
    token = {
        "title": "Super Founder #" + str(j),
        "description": "500 Scorpion NFT Fighters on the Binance Smart Chain. 1st PVP game on BSC",
        "type": "image",
        "image": IMAGES_BASE_URL + str(token_id),
        "tokenId": j,
        "attributes": [],
        "compiler": "HashLips Art Engine"
    }
    token["attributes"].append(getAttribute("Type", "Super Founder"))
    token["attributes"].append(getAttribute("Rarity", "Legendary"))
    token["attributes"].append(getAttribute("Lives", "500"))

    with open('./' + str(j) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)
    j = j + 1
f.close()