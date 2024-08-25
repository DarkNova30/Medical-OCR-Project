from fastapi import FastAPI
from enum import Enum
app = FastAPI()

# @app.get("/hello/{name}")   # entry point
# async def hello(name):
#     return f"hi welcome to my webpage {name}"


class AvailableCuisine (str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"


food_items = {
    "indian": ["samosa", "dosa"],
    "american": ["hot dog", "pie"],
    "italian": ["pizza", "pasta"]
}

coupon_code = {
    1: "10%",
    2: "20%",
    3: "30%"
}


@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisine): # type hint
    return food_items.get(cuisine)


@app.get("/get_coupon/{code}")
async def get_coupon(code: int):
    return ("Discount applied: ", coupon_code.get(code))


    # try:
    #     items = food_items[cuisine]
    #     return [i for i in items]       # this alsp works
    # except:
    #     return "Cuisine note found"

