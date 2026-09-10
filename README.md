# MidKnighttechport — Financial ML & Data Analytics Portfolio

Applied data science and machine learning work spanning quantitative finance, fraud detection, and business intelligence — by [Allwell Godwin](https://www.linkedin.com/in/allwell-godwin-mba-808853241/), MBA (AI), MSc Financial Engineering candidate (WorldQuant University).

More context: [portfolio site](https://knightallwell.github.io/allwelltechport.github.io/) · [Audit2Alpha](https://www.youtube.com/@audit2alpha) · [August Marathon Analytics](https://github.com/knightallwell)

---

## Projects

### Multivariate Portfolio Risk Analysis
`Quantitative Finance/Portfolio Analysis/`

**Problem:** Diversifying a multi-asset portfolio (equities, crypto, oil, FX, international names) requires understanding how the assets are statistically linked and how that structure shifts across market regimes.
**Method:** An end-to-end pipeline — data cleaning and returns, multicollinearity (VIF) and correlation, stationarity (ADF), a conditional Granger-causality network over a VAR model, Markov-switching regime detection, GARCH volatility forecasting, and Monte Carlo portfolio simulation with weight optimization, Value at Risk (VaR) and Expected Shortfall (CVaR), plus time-ordered out-of-sample validation and scenario-based Monte Carlo.
**Result:** A miniature portfolio risk-management system. See [`Portfolio analysis.ipynb`](<Quantitative Finance/Portfolio Analysis/Portfolio analysis.ipynb>).

### AI Algorithmic Trading — Deep Reinforcement Learning (PPO)
`Quantitative Finance/Algorithimic Trading/`

**Problem:** Manual trading decisions don't scale and lag fast-moving markets.
**Method:** A Proximal Policy Optimization (PPO) agent trained on the top-10 S&P 500 tickers, using historical price data and technical features to learn buy/sell/hold decisions.
**Result:** Trained agent evaluated on cumulative return, Sharpe ratio, and drawdown against a buy-and-hold baseline. See the [project write-up](<Quantitative Finance/Algorithimic Trading/Readme.md/README.md>) for training details and evaluation charts.
**Notebooks:** [`Algorithimic_Trading_(Deep_Reinforcement_Learning)_ (1).ipynb`](<Quantitative Finance/Algorithimic Trading/Algorithimic_Trading_(Deep_Reinforcement_Learning)_ (1).ipynb>), [`Top_10_companies_listed_on_sp500_mar_2024.ipynb`](<Quantitative Finance/Algorithimic Trading/Top_10_companies_listed_on_sp500_mar_2024.ipynb>)

### Stock Market Prediction — LSTM
`Quantitative Finance/Stock market prediction/`

**Problem:** Forecasting near-term stock price direction from historical price action.
**Method:** LSTM sequence model trained on price history enriched with Moving Average, RSI, and MACD indicators.
**Result:** See [`Stock_market_prediction_.ipynb`](<Quantitative Finance/Stock market prediction/Stock_market_prediction_.ipynb>) for model architecture, training curves, and forecast accuracy.

### Fraud Detection
`Financial Technology/fraud detection/`

**Problem:** Detecting fraudulent transactions in imbalanced financial data.
**Method:** Classification pipeline with feature engineering and anomaly detection (Isolation Forest).
**Result:** 94% accuracy, with a 25% improvement in incident response time over the prior manual process. See [`Fraud_detection (1).ipynb`](<Financial Technology/fraud detection/Fraud_detection (1).ipynb>).

### AI Building Evaluation — Computer Vision
`AI related/pytorch AI capstone/`

**Problem:** Manual structural crack inspection is slow and inconsistent.
**Method:** PyTorch, transfer learning on ResNet-18, to classify building images for crack detection.
**Result:** IBM AI Engineering capstone project. See the notebook sequence starting at [`1 0_load_and_display_data.ipynb`](<AI related/pytorch AI capstone/1 0_load_and_display_data.ipynb>) through [`4 1_resnet18_PyTorch (2).ipynb`](<AI related/pytorch AI capstone/4 1_resnet18_PyTorch (2).ipynb>).

### Predictive Launch-Outcome Analysis — IBM Applied Data Science Capstone
`Business intelligence/Resource Optimization/`

**Problem:** Predicting SpaceX first-stage landing success from launch data, as a full data science lifecycle exercise.
**Method:** Data collection (API + web scraping), wrangling, EDA, visualization, and predictive modeling across the `collection/`, `Data wrangling/`, `Analysis/`, `Landing site visualization/`, and `prediction/` subfolders.
**Result:** Completed capstone for the IBM Data Science Professional Certificate.

### Credit Risk Analysis
`Financial Technology/Credit risk analysis/`

**Problem:** Assessing borrower default risk from financial and demographic features.
**Method:** Exploratory analysis and classification modeling on credit application data.
**Result:** See [`Credit risk analysis.ipynb`](<Financial Technology/Credit risk analysis/Credit risk analysis.ipynb>).

### US GDP Prediction
`Financial Technology/US GDP Prediction/`

**Method:** Time-series modeling of macroeconomic indicators to forecast US GDP.
**Result:** See [`GDP_PREDICTION.ipynb`](<Financial Technology/US GDP Prediction/GDP_PREDICTION.ipynb>).

### Business Intelligence & Causal Prediction
`Business intelligence/`, `Causal prediction/`

Churn analysis (PowerCo), inventory management (Cognizant), house price prediction, and classification case studies (Titanic, SUV purchase prediction, government debt) — course and self-directed projects applying EDA, feature engineering, and classical ML (KNN, Naive Bayes, SVC).

### SQL Data Manipulation
`SQL 2/`

Query-based data cleaning, transformation, and analysis over retail and person-record datasets.

### Python Visualization & Dashboards
`Python visualization/`

Interactive dashboards (Plotly Dash) and static visualizations (IBM course project) turning raw data into business-facing charts.

---

## Stack

Python · PyTorch · scikit-learn · pandas / NumPy · SQL · Power BI · Plotly Dash · Jupyter

## Contact

[allwellgodwin37@gmail.com](mailto:allwellgodwin37@gmail.com) · [LinkedIn](https://www.linkedin.com/in/allwell-godwin-mba-808853241/) · [Portfolio](https://knightallwell.github.io/allwelltechport.github.io/)
