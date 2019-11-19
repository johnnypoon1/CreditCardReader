from datetime import date, datetime
from .models import CreditCard
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CCSerializer

import re


"""class CCSerializer(serializers.Serializer):
	ccnumber = serializers.CharField(max_length=16)
	name = serializers.CharField(max_length=200)
	expire = serializers.DateField(validators=[date_check])
	CVV = serializers.DecimalField(max_digits=4)
	
	def date_check(expire_date):
	today = date.today()
	day = datetime.date(expire_date.year,expire_date.month,expire_date.day)
	if day > today:  # compare today and expiration day
		raise serializers.ValidationError("Card is expired")
	return true"""

class CreditCardView(APIView):

    def addDecimal(self, dig):
        if dig < 10:
            return dig

        sum = dig % 10 + dig // 10
        return sum

    def validatecc(self, cc):
        """
........Validate credit card number using Luhn
........
........Attributes
        cc : str
........    credit card number"""

        cc_num = cc[::-1]

        # Add number validation here
        cc_num = [int(x) for x in cc_num]

        # double every second digit
        doubled_digits = list()
        digits = list(enumerate(cc_num, start=1))
        for (index, digit) in digits:
            if index % 2 == 0:
                doubled_digits.append(digit * 2)
            else:
                doubled_digits.append(digit)

        # add the digits if number > 9
        doubled_digits = [self.addDecimal(x) for x in doubled_digits]

        # adding all digits up
        lumSun = sum(doubled_digits)

        return lumSun % 10 == 0

    def getCardType(self, cc):
        """
........Take the credit card number and identify the type
........
........Attributes
........cc : str
........    credit card number
........"""

        # Identify the format of each card type
        CardTypes = {
            'Visa': re.compile(r"^4[0-9]{12}(?:[0-9]{3})?$"),
            'AmericanEx': re.compile(r"^3[47][0-9]{13}$"),
            'Master': re.compile(r"^5[1-5][0-9]{14}$"),
            'Discovery': re.compile(r"^6(?:011|5[0-9]{2})[0-9]{12}$"),
            }

        # Match card number with card type format
        for (type, identifier) in CardTypes.items():
            if identifier.match(str(cc)):
                return type
        return None

    def get(self, request):

        # TODO: Generate card number here

        return Response({'Card Number': 'Card number generator in process'
                        })

    def post(self, request):

        # Get the input
        card = request.POST['_content']

        if card is not None:
            # TODO: validate card number here

            # Create an object for output
            cc = {'ccNumber': card, 'Type': '', 'ValidCard': False}

            # Validate Credit Card
            if len(card) > 0 and self.validatecc(card):
                cc['ValidCard'] = True
                cc['Type'] = self.getCardType(card)

            return Response(cc)
        return Response({'Result': 'Unaccepted input'})
