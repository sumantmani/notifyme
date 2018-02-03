
import falcon

import notifyme.api.resources as r
import notifyme.database.core as db
import notifyme.api.api_logging

from notifyme.api.middleware import MyMiddleware

db.init_db_if_needed()
app = application = falcon.API(middleware=[MyMiddleware()])

root = r.Root()
user = r.User()

product = r.Product()
add_product = r.AddProduct()

subscriber = r.Subscriber()
unsubscriber = r.Unsubscriber()

app.add_route('/', root)

app.add_route('/user', user)

app.add_route('/product', add_product)

app.add_route('/subscribe', subscriber)
app.add_route('/unsubscribe', unsubscriber)

app.add_route('/priceDataPoint', product)



