#### Generate Metadata for each Image    
import json

f = open('./7-all.json',) 
data = json.load(f)

# Changes this IMAGES_BASE_URL to yours 
IMAGES_BASE_URL = "ipfs://QmbnUHZG2DPF1AhFL45cUHdq3N6qiEyCY4nZ2WEmZW7ypP/"
PROJECT_NAME = "NFT_CREATOR"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }

j = 237

for i in data:
    token_id = i['tokenId']
    token = {
        "title": "Limited Edition #" + str(j),
        "description": "500 Scorpion NFT Fighters on the Binance Smart Chain. 1st PVP game on BSC",
        "type": "video",
        "image": IMAGES_BASE_URL + str(token_id),
        "tokenId": j,
        "attributes": [],
        "compiler": "HashLips Art Engine"
    }
    token["attributes"].append(getAttribute("Type", "Limited Edition"))
    token["attributes"].append(getAttribute("Rarity", "Common"))
    token["attributes"].append(getAttribute("Lives", "10"))

    with open('./' + str(j) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)
    j = j + 1
f.close()