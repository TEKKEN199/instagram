import requests, os

username = input("username:")
r = requests.Session()
def report():
    try:
        url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "ar,en-US;q=0.9,en;q=0.8,es;q=0.7",
            "content-length": "84",
            "content-type": "application/x-www-form-urlencoded",
            'cookie': 'ig_did=611CDA13-CB10-4F7F-AEBE-625FE59F64E5; mid=YAkaVAALAAE0r-Fu61BIbmNCb7u6; ig_nrcb=1; shbid=11168; rur=FTW; shbts=1611816278.0011039; csrftoken=875JYxnA3PNeRt0t93KP82f6hjwUkrDs; urlgen="{\"188.52.48.203\": 25019}:1l52Eo:_sMiDTZAa7xB3ndEShKAcVJxBG4"',
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/accounts/password/reset/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
            "x-csrftoken": "875JYxnA3PNeRt0t93KP82f6hjwUkrDs",
            "x-ig-app-id": "936619743392459",
            "x-ig-www-claim": "hmac.AR2sB6N6VVUaigFDtzwU8_CBU9xqi-87B5VgiAFMAWDEfIgl",
            "x-instagram-ajax": "5f4886947dbe",
            "x-requested-with": "XMLHttpRequest"}
        data = {
            "email_or_username": username,
            "recaptcha_challenge_field": "",
            "flow": "",
            "app_id": "",
            "source_account_id": ""
        }
        INPUT = input("email/photo You will send a message to him, are you sure : y/n >>")
        report = r.post(url, headers=headers, data=data).text
        if ('"message":"Please wait a few minutes before you try again."') in report:
            print("ERROR")
            input()
        elif INPUT == "y":
            xx = str(report.split('"{"title":"Email Sent","body":"We sent an email to "'))
            xxx = str(xx.split(
                ' with a link to get back into your account.","can_recover_with_code":false,"contact_point":"')[1])
            xxxx = xxx.split("'")[0]
            DATA = xxxx.split('","status":"ok"}')[0]
            print("email/iphone:" + DATA)
            input()
        else:
            print("ERROR")
            input()
    except:
        print("ERROR")
report()
