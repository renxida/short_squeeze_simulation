---
title: Simulating Short Squeezes
author: Xida Ren
date: July 27, 2019
---


# Short Squeeze Simulator

This project aims to recreate short squeezes in a simulated market using agent-based modeling.

## What is a short squeeze

A short squeeze is a rapid increase in the price of a stock that occurs when there is a lack of supply and an excess of demand for the stock.

Short squeezes result when short sellers cover their positions on a stock, resulting in buying volume that drives the stock price up. This can occur if the price has risen to a point where short sellers must make margin calls, or more loosely if short sellers simply decide to cut their losses and get out. This may happen in an automated manner for example if the short sellers had previously placed stop-loss orders with their brokers to prepare for this possibility. Since covering their positions involves buying shares, the short squeeze causes an ever further rise in the stock's price, which in turn may trigger additional margin calls and short covering.

Short squeezes are more likely to occur in stocks with small market capitalization and small floats, although can involve large stocks and billions of dollars, as happened in October 2008 when a short squeeze temporarily drove the shares of Volkswagen on the Xetra DAX from €210.85 to over €1000 in less than two days, briefly making it the most valuable company in the world. Short squeezes may also be more likely to occur when a large percentage of a stock's float is short.

The opposite of a short squeeze is the less common long squeeze.

This can also apply to futures contracts.

-- Wikipedia

## The goal of this project

... is to create a simulated microcosmic market that exhibits the phenomenon of short-squeezing, likely using agent-based modeling.

## Relevant Ideas

## Financial
- Short Squeezes: the phenomenon of interst
- The stock trading process: clearing vs settlement
- Prime brokerage: what do prime brokers do in the market
- Post-financial crisis regulations
    - the settlement deadline
    - this partly explains why the stock-loan business exists, and how the loan-supply of stocks is limited
- Algorithmic trading
- Market-making

## Technical
- Agent-based modeling
- The Mesa Python library for Agent-based modeling
- Khalman Filter
    - may be used to implement market making agents, which attempt to make a bid-ask spread and supply liquidity to the market
- Limit Order Book
    - implement in python
- Priority Queues
- Feedback Loops
- Reflexivity
    - mix of negative and positive feedback & shifting from one to the other
    - see George Soros' lecture on this from a very philosophical POV: https://www.youtube.com/watch?v=oCaCrWzFPYY&t=2093s
