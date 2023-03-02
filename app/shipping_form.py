from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import DataRequired
from map.map import map

print(map)




class ShippingForm(FlaskForm):
    sender_name = StringField("sender name", validators=[DataRequired()])
    recipient_name = StringField("recipient name", validators=[DataRequired()])
    