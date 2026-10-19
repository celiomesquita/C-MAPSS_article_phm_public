# Congelamento do protocolo principal: 18/10/2026

- **Protocolo congelado:** `protocolo_principal_congelado.md` (somente leitura).
- **Emendas:** `emendas.md` (vazio no congelamento).
- **Hashes:** `manifest_hashes.json`; hash do manifesto em `manifest_hashes.sha256`.
- **Ambiente:** Python 3.14.0; pacotes relevantes: joblib==1.5.3, lightgbm==4.6.0, matplotlib==3.10.8, numpy==2.4.0, pandas==2.3.3, scikit-learn==1.8.0, scipy==1.17.1, threadpoolctl==3.6.0, xgboost==3.2.0; pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025). Lista completa em `environment_full_freeze.txt`.
- **Dados:** hashes de FD001 e FD003 (treino, teste e RUL) calculados no congelamento; hashes de FD002 e FD004 **copiados do inventário R00.1** (`experiments/artifacts/inventory/inventory.json`), sem reabrir os arquivos.
- **Integridade:** todos os manifestos de pilotos anteriores foram conferidos antes do congelamento e estavam íntegros.
- **Não coberto:** verificação bibliográfica, periódico-alvo e o código de confirmação (ainda não escrito).
