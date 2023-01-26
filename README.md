# EC Skelton with Django
---
本プログラムはECサイトのスケルトンになります。

決済機能以外の機能が搭載されています。<br />
決済機能は『Stripe』を利用する想定で開発してあります。

## Environment
Python 3.9.5

## How to use
1. `pip instal -r requirements.txt`
1. `python manage.py makemigrations`
1. `python manage.py migrate`
1. `python manage.py runserver`

## Attention
staticフォルダが見つからない時があります。<br />
その場合は、以下の順でコマンドを試してみて下さい。<br />
1. `python manage.py findstatic .`
1. `python manage.py collectstatic`
1. `python manage.py findstatic .`

以上
