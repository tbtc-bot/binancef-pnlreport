#!/bin/bash
docker build -t asia-northeast1-docker.pkg.dev/tbtc-terrabot-prod/terrabot/binance-futures-pnlreport:0.0.3 .
docker push asia-northeast1-docker.pkg.dev/tbtc-terrabot-prod/terrabot/binance-futures-pnlreport:0.0.3
