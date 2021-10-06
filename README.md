# binance-futures-pnlreport

## Deploy Futures PnlReport in Prod Env
```bash
helm upgrade -i --set image.tag=0.0.1 --atomic --namespace bot-binance-prod -f ./helm/futures-pnlreport/values-prod.yaml futures-pnlreport ./helm/futures-pnlreport/
```

## Deploy Futures PnlReport in Quality Assurance Env
```bash
helm upgrade -i --set image.tag=0.0.1 --atomic --namespace bot-binance-qa -f ./helm/futures-pnlreport/values-qa.yaml futures-pnlreport ./helm/futures-pnlreport/
```

## Test
```bash
helm template futures-pnlreport ./helm/futures-pnlreport/ --set image.tag=0.0.1 -f ./helm/futures-pnlreport/values-qa.yaml
```
