### 商品クラス
import pandas as pd
import datetime
import eel


class Item: # 商品情報
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.ordering_party_list = []
        self.item_order_list=[] # 商品コードのリスト
        self.item_quantity_list = [] # 注文数量のリスト
        self.item_master=item_master # Itemのリスト
    
    
    def add_ordering_party(self,ordering_party): # 注文する人の名前
        self.ordering_party_list.append(ordering_party)
    
    
    def add_item_order(self,item_code): # 商品コードのリストにコードを追加
        self.item_order_list.append(item_code)
        
    def add_quantity_order(self,item_quantity): # 注文数量のリストに注文数を追加
        self.item_quantity_list.append(item_quantity)
    
    
    def view_item_list(self, item_dict, deposit_amount): 
        for order, quantity in zip(self.item_order_list, self.item_quantity_list):
            price = int(item_dict[order][1])*int(quantity)
            change = int(deposit_amount) - price
            return "商品コード:{}が{}個で{}円になります。お預かりしている金額は{}円なので{}円お返しいたします".format(order,quantity,price,deposit_amount,change)
            
    
        
    

    
    
### メイン処理
def main():
    # マスタ登録

    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))
    
    # 標準入力でユーザから注文内容を聞き取る
    ordering_party = input('お名前をお願いします:')
    item_code = input('購入予定商品の商品コードの入力をしてください。例：002:')
    item_quantity = input('欲しい個数を入力してください。例：2')
    deposit_amount = input('入金額を入力してください:')

    
    # マスタ登録されている商品を、商品名:価格のdictに変換
    item_dict = {item.item_code: [item.item_name, item.price] for item in item_master}
    
    print(f'商品コード{item_code}は{item_dict[item_code][0]}で{item_dict[item_code][1]}円です')
    
    codes = []
    product_names = []
    prices = []
    
    for item in item_master:
        codes.append(item.item_code)
        product_names.append(item.item_name)
        prices.append(item.price)
        
    csv_data = {
        'code': codes,
        'name': product_names,
        'price': prices,
    }
    
    # 商品マスタをcsv形式のファイルに保存
    df = pd.DataFrame(csv_data)
    df.to_csv('/Users/toguchitaichi/Desktop/study-04-pos-system-01-master/masta.csv', encoding='utf-8')
    
    
    # オーダー登録
    order=Order(item_master)
    order.add_ordering_party(ordering_party)
    order.add_item_order(item_code)
    order.add_quantity_order(item_quantity)
    
    
    # オーダー表示
    dt_now = datetime.datetime.now()
    dt_now = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
    with open(dt_now + '.txt', mode='w') as f:
        f.write(order.view_item_list(item_dict, deposit_amount))
        
    
main()