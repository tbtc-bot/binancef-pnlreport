# binance-futures-pnlreport

## Deploy Futures PnlReport in Prod Env
```bash
helm upgrade -i --set image.tag=0.0.1 --atomic --namespace bot-binance-prod -f ./helm/futures-pnlreport/values-prod.yaml futures-pnlreport ./helm/futures-pnlreport/
```

## Deploy Futures PnlReport in Quality Assurance Env
```bash
helm upgrade -i --set image.tag=0.0.1 --atomic --namespace bot-binance-qa -f ./helm/futures-pnlreport/values-qa.yaml futures-pnlreport ./helm/futures-pnlreport/
```

## Test Helm
```bash
helm template futures-pnlreport ./helm/futures-pnlreport/ --set image.tag=0.0.1 -f ./helm/futures-pnlreport/values-qa.yaml
```

## Initial Setup
```bash
python3 -m venv .venv
pip install -r requirements.txt
```

## Test API Call
```bash
curl -X POST http://localhost:8080/bot-stats -H 'Content-Type: application/json' -d '{"start_date":"2021-10-08","end_date":"2021-10-08","api_key":"XXX","api_secret":"YY"}'
curl -X POST http://futures-pnlreport.bot-binance-lab:8080/bot-stats -H 'Content-Type: application/json' -d '{"start_date":"2021-10-08","end_date":"2021-10-08","api_key":"XXX","api_secret":"YY"}'
```