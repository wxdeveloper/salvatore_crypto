# a = [2387471, 40698843302, 0, 0, 1047269, 100, 0, 10500000, 999900, 999900, 146527, 3551897, 196973109, 0, 999900, 100, 1, 1, 0, 9999, 0, 0, 5533437903, 0, 2434196779, 71994900, 999900, 9999, 237988200, 981333176, 4999500, 5866111356, 55494250, 0, 300000000, 1004484050, 0, 2000000, 416000000, 0, 6611328666085, 100, 95862, 0, 100000000, 1219944000, 4999500, 9999, 2608770000, 502665388, 999900, 0, 0, 100, 34727542, 0, 1195000000, 999, 9999000, 100, 0, 17200000, 31650085, 21457382, 10000000, 400000000, 500000000003, 555100000, 6199500, 41087400, 49995000, 396916543, 7019, 0, 0, 0, 0, 380000000, 699930, 6000000, 100, 999900, 15000000, 100, 107489250, 169000000, 371, 100, 200000000, 1414979, 999900, 0, 999, 1003600000, 0, 0, 4411791, 999, 0, 198362663]

# import httpx
# import asyncio

# b = []

# async def test():
#     async with httpx.AsyncClient() as cleint:
#         res = await cleint.get('https://stargaze-api.testovi.ch/cosmos/staking/v1beta1/validators/starsvaloper1tnx3z8ke9za65v32qxhu65mav2282jru8989a6/delegations?height13956928&pagination.key=FHRcl429nVDcrMoi7QZ2IWGfM9ABFFzNER7ZKLuqMioBr81TfWKUdUh8')

#         json = res.json()['delegation_responses']

#         for i in json:
#             b.append(int(i['balance']['amount']))
        
#         c = sum(b)
#         d = sum(a)
#         y = c + d
#         print(y)
    

# import urllib.parse

# url = "https://stargaze-api.testovi.ch/cosmos/staking/v1beta1/validators/starsvaloper1tnx3z8ke9za65v32qxhu65mav2282jru8989a6/delegations?height=13956928&pagination.key=FOW4jLo+Y3Q9YMrJUdY/HEVxiRSMFJXm/fVwq1BPGL+1dxeRODU3a2Rc"

# encoded_url = urllib.parse.quote(url, safe=':/?&=')
# print(encoded_url)



# # if __name__ == '__main__':
# #     asyncio.run(test())


a = [_ for _ in range(1, 30)]

print(a)