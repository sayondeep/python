import requests as req

def healthCheckUp(lo, hi):
    url = "https://jsonmock.hackerrank.com/api/medical_records?page=1"
    res = req.get(url).json()
    pages = res['total_pages']
    per_page = res['per_page']
    ans = 0

    for i in range(1, pages+1):
        url = "https://jsonmock.hackerrank.com/api/medical_records?page="+str(i)
        res = req.get(url).json()
        for j in range(per_page):
            try:
                val = int(res['data'][j]['vitals']['bloodPressureDiastole'])
                if(val >= lo and val <= hi):
                    ans+=1
            except:
                pass
    
    return ans


print(healthCheckUp(120, 160))
