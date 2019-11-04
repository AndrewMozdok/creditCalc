#Объявляем переменные
totalPurchase = 0 #Общая стоимость покупки
freeDelivery = 0 #Бесплатная доставка
Delivery = 10 #Стоимость доставки

totalPurchase = float(input('Сумма вашей покупки:'))
if totalPurchase < 50:
    print('Общая сумма с доставкой:' ,Delivery + totalPurchase )
else:
    print('Общая сумма:' , totalPurchase )
    print('Поздравлем! У вас халявная доставка!')
