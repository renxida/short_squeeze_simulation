# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import numbers

# %%
isinstance("3.14", numbers.Number)

# %%
import heapq

# %%
from functools import total_ordering

@total_ordering # https://portingguide.readthedocs.io/en/latest/comparisons.html
class Order:
    def __init__(self, price, direction="detect"):
        """
        Create a new Order object.
        
        No quantities. Each price is atomic.
        This may change when we upscale.
        
        We encode the direction of the order with the sign of the price.
        
        Since heapq puts the least (most negative) element on top,
        we set negative prices to represent buy (bid) orders,
        such that the most negative buy order is the one with the highest price,
        and set positive prices to represent sell (ask / put) orders,
        such that the most negative sell order is the one with the lowest price.
        
        Best buy order has the highest absolute value (actual price),
        and best sell order has the lowest absolute value (actual price).
        """
        if price == 0:
                raise ValueError("Price cannot be zero")
        if direction == "detect":
            self.price = price
        else:
            if price <0:
                raise ValueError("Price cannot be negative when direction fixed")
            if direction in {"bid", "buy", "long"}:
                self.price = -price
            elif direction in {"ask", "sell", "put", "short"}:
                self.price = price
            else:
                raise ValueError
                
    @property
    def direction(self):
        if self.price > 0:
            return "ask"
        elif self.price < 0:
            return "bid"
        else:
            raise ValueError("Price cannot be zero")
            
    def __abs__(self):
        return abs(self.price)
        
    def __repr__(self):
        return f"{type(self).__name__}(price={self.price}, direction='{self.direction}')"
    
    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            # enable comparison with numerical types
            return self.price == other
        return self.price == other.price
    
    def __ne__(self, other):
        if isinstance(other, numbers.Number):
            # enable comparison with numerical types
            return self.price != other
        return self.price != other.price
    
    def __lt__(self, other):
        if isinstance(other, numbers.Number):
            # enable comparison with numerical types
            return self.price <= other
        return self.price < other.price


# %%
class OrderBook:
    def __init__(self, asks=None, bids=None):
        if asks is None:
            asks = []
        if bids is None:
            bids = []
        self.asks = asks
        self.bids = bids
    
    def add(self, order):
        if order > 0: # ask
            heapq.heappush(self.asks, order)
        elif order < 0:
            heapq.heappush(self.bids, order)
        self._execute()
            
    def fok(self, order):
        """
        Fill or kill an order.
        
        Args:
            order (int or Order): an order to f-o-k
        Returns:
            True if filled,
            False if killed
        """
        raise NotImplementedError
    
    @property
    def top_bid(self):
        if len(self.bids) > 0:
            return self.bids[0]
        else:
            return None
    
    @property
    def top_ask(self):
        if len(self.asks) > 0:
            return self.asks[0]
        else:
            return None
        
    @property
    def mid_price(self):
        best_ask_price = abs(self.asks[0])
        best_bid_price = abs(self.bids[0])
        return (best_ask + best_bid)/2
            
    def _record_execution(self,ask, bid):
        """
        Record execution of order.
        """
        pass
    
    def _execute(self):
        """
        
        """
        while self.top_bid and self.top_ask and abs(self.asks[0]) <= abs(self.bids[0]):
            ask = heapq.heappop(self.asks)
            bid = heapq.heappop(self.bids)
            self._record_execution(ask, bid)
            
    def __repr__(self):
        return f"OrderBook(asks={self.asks}, bids={self.bids})"


# %%
b = OrderBook()

# %%
b.add(Order(3))

# %%
b

# %%
b.add(-5)

# %%
b
