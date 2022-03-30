#### Generate Metadata for each Image    
import json

f = open('./2-all.json',) 
data = json.load(f)

# Changes this IMAGES_BASE_URL to yours 
IMAGES_BASE_URL = "ipfs://QmV7qf3ca4g1roEfobCM94YTnXixFmcvogMBpyFpMLhGwy/"
PROJECT_NAME = "NFT_CREATOR"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }

j = 10

for i in data:
    token_id = i['tokenId']
    token = {
        "title": "Super Founder #" + str(j),
        "description": "500 Scorpion NFT Fighters on the Binance Smart Chain. 1st PVP game on BSC",
        "type": "video",
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