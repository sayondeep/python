import requests as req
def getAns(city, maxcost):
  url = "https://jsonmock.hackerrank.com/api/food_outlets?city="+city+"&page=1"
  res = req.get(url).json()

  total = res['total_pages']
  per_page = res['per_page']
  ans = []

  for i in range(1, total+1):
    url = "https://jsonmock.hackerrank.com/api/food_outlets?city="+city+"&page="+str(i)
    res = req.get(url).json()
  
    for j in range(per_page):
      cost = int(res['data'][j]['estimated_cost'])
      if(cost <= maxcost):
        ans.append(res['data'][j]['name'])

  return ans


if(__name__ == "__main__"):
  maxcost = 2000
  city = "Houston"
  ans = getAns(city, maxcost)
  for i in ans:
    print(i)
