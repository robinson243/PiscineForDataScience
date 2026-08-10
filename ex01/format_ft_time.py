from datetime import datetime
from decimal import Decimal

dt = datetime.now()
# epoch_time = datetime(1970, 1, 1)

sec = dt.timestamp()


finalDate = dt.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {sec:,.3f} or {sec:e} in scientific notation")
print(finalDate)