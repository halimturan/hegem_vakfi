from django.shortcuts import render


def make_payment(request):
    """
    <CC5Request>
        <Name>hegemadmin</Name>
        <Password>TRNO4598</Password>
        <ClientId>700679591149</ClientId>
        <Type>Auth</Type>
        <TransId>İşlem Numarası</TransId>
        <Total>2500</Total>
        <Currency>949</Currency>
        <Number>Kredi Kartı Numarası</Number>
        <Expires>Kredi Kartı Son Kullanam Tarihi<Expires>
        <Cvv2Val>Kredi Kartının Güvenlik Numarası</Cvv2Val>
    </CC5Request>
    """
    return render(request, 'payment/make_payment.html')
