本專案使用Python Flask框架開發，提供訂單格式檢查與轉換服務的API。

技術棧

編程語言：Python
框架：Flask
數據驗證：Pydantic
容器技術：Docker
如何運行

克隆倉庫到本地。
在專案目錄中運行docker build -t my-python-app .構建Docker映像。
使用docker run -p 4000:5000 my-python-app啟動應用。
API文檔

端點：POST /api/orders
{
  "id": "A0000001",
  "name": "Melody Holiday Inn",
  "address": {
    "city": "taipei-city",
    "district": "da-an-district",
    "street": "fuxing-south-road"
  },
  "price": 2050,
  "currency": "TWD"
}
