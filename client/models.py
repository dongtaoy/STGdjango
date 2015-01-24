from django.db import models
from hr.models import Employee
from system.models import Label

NATIONALITY = (("AF", "Afghanistan"), ("AL", "Albania"), ("DZ", "Algeria"), ("AS", "American Samoa"), ("AD", "Andorra"),
               ("AO", "Angola"), ("AI", "Anguilla"), ("AR", "Argentina"), ("AM", "Armenia"), ("AW", "Aruba"),
               ("AU", "Australia"), ("AT", "Austria"), ("AZ", "Azerbaijan"), ("BS", "Bahamas"), ("BH", "Bahrain"),
               ("BD", "Bangladesh"), ("BB", "Barbados"), ("BY", "Belarus"), ("BE", "Belgium"), ("BZ", "Belize"),
               ("BJ", "Benin"), ("BM", "Bermuda"), ("BT", "Bhutan"), ("BO", "Bolivia"),
               ("BA", "Bosnia and Herzegowina"), ("BW", "Botswana"), ("BV", "Bouvet Island"), ("BR", "Brazil"),
               ("IO", "British Indian Ocean Territory"), ("BN", "Brunei Darussalam"), ("BG", "Bulgaria"),
               ("BF", "Burkina Faso"), ("BI", "Burundi"), ("KH", "Cambodia"), ("CM", "Cameroon"), ("CA", "Canada"),
               ("CV", "Cape Verde"), ("KY", "Cayman Islands"), ("CF", "Central African Republic"), ("TD", "Chad"),
               ("CL", "Chile"), ("CN", "China"), ("CX", "Christmas Island"), ("CC", "Cocos (Keeling) Islands"),
               ("CO", "Colombia"), ("KM", "Comoros"), ("CG", "Congo"), ("CD", "Congo, the Democratic Republic of the"),
               ("CK", "Cook Islands"), ("CR", "Costa Rica"), ("CI", "Cote d'Ivoire"), ("HR", "Croatia (Hrvatska)"),
               ("CU", "Cuba"), ("CY", "Cyprus"), ("CZ", "Czech Republic"), ("DK", "Denmark"), ("DJ", "Djibouti"),
               ("DM", "Dominica"), ("DO", "Dominican Republic"), ("EC", "Ecuador"), ("EG", "Egypt"),
               ("SV", "El Salvador"), ("GQ", "Equatorial Guinea"), ("ER", "Eritrea"), ("EE", "Estonia"),
               ("ET", "Ethiopia"), ("FK", "Falkland Islands (Malvinas)"), ("FO", "Faroe Islands"), ("FJ", "Fiji"),
               ("FI", "Finland"), ("FR", "France"), ("GF", "French Guiana"), ("PF", "French Polynesia"),
               ("TF", "French Southern Territories"), ("GA", "Gabon"), ("GM", "Gambia"), ("GE", "Georgia"),
               ("DE", "Germany"), ("GH", "Ghana"), ("GI", "Gibraltar"), ("GR", "Greece"), ("GL", "Greenland"),
               ("GD", "Grenada"), ("GP", "Guadeloupe"), ("GU", "Guam"), ("GT", "Guatemala"), ("GN", "Guinea"),
               ("GW", "Guinea-Bissau"), ("GY", "Guyana"), ("HT", "Haiti"), ("HM", "Heard and Mc Donald Islands"),
               ("VA", "Holy See (Vatican City State)"), ("HN", "Honduras"), ("HK", "Hong Kong"), ("HU", "Hungary"),
               ("IS", "Iceland"), ("IN", "India"), ("ID", "Indonesia"), ("IR", "Iran (Islamic Republic of)"),
               ("IQ", "Iraq"), ("IE", "Ireland"), ("IL", "Israel"), ("IT", "Italy"), ("JM", "Jamaica"), ("JP", "Japan"),
               ("JO", "Jordan"), ("KZ", "Kazakhstan"), ("KE", "Kenya"), ("KI", "Kiribati"),
               ("KP", "Korea, Democratic People's Republic of"), ("KR", "Korea, Republic of"), ("KW", "Kuwait"),
               ("KG", "Kyrgyzstan"), ("LA", "Lao People's Democratic Republic"), ("LV", "Latvia"), ("LB", "Lebanon"),
               ("LS", "Lesotho"), ("LR", "Liberia"), ("LY", "Libyan Arab Jamahiriya"), ("LI", "Liechtenstein"),
               ("LT", "Lithuania"), ("LU", "Luxembourg"), ("MO", "Macau"),
               ("MK", "Macedonia, The Former Yugoslav Republic of"), ("MG", "Madagascar"), ("MW", "Malawi"),
               ("MY", "Malaysia"), ("MV", "Maldives"), ("ML", "Mali"), ("MT", "Malta"), ("MH", "Marshall Islands"),
               ("MQ", "Martinique"), ("MR", "Mauritania"), ("MU", "Mauritius"), ("YT", "Mayotte"), ("MX", "Mexico"),
               ("FM", "Micronesia, Federated States of"), ("MD", "Moldova, Republic of"), ("MC", "Monaco"),
               ("MN", "Mongolia"), ("MS", "Montserrat"), ("MA", "Morocco"), ("MZ", "Mozambique"), ("MM", "Myanmar"),
               ("NA", "Namibia"), ("NR", "Nauru"), ("NP", "Nepal"), ("NL", "Netherlands"),
               ("AN", "Netherlands Antilles"), ("NC", "New Caledonia"), ("NZ", "New Zealand"), ("NI", "Nicaragua"),
               ("NE", "Niger"), ("NG", "Nigeria"), ("NU", "Niue"), ("NF", "Norfolk Island"),
               ("MP", "Northern Mariana Islands"), ("NO", "Norway"), ("OM", "Oman"), ("PK", "Pakistan"),
               ("PW", "Palau"), ("PA", "Panama"), ("PG", "Papua New Guinea"), ("PY", "Paraguay"), ("PE", "Peru"),
               ("PH", "Philippines"), ("PN", "Pitcairn"), ("PL", "Poland"), ("PT", "Portugal"), ("PR", "Puerto Rico"),
               ("QA", "Qatar"), ("RE", "Reunion"), ("RO", "Romania"), ("RU", "Russian Federation"), ("RW", "Rwanda"),
               ("KN", "Saint Kitts and Nevis"), ("LC", "Saint LUCIA"), ("VC", "Saint Vincent and the Grenadines"),
               ("WS", "Samoa"), ("SM", "San Marino"), ("ST", "Sao Tome and Principe"), ("SA", "Saudi Arabia"),
               ("SN", "Senegal"), ("SC", "Seychelles"), ("SL", "Sierra Leone"), ("SG", "Singapore"),
               ("SK", "Slovakia (Slovak Republic)"), ("SI", "Slovenia"), ("SB", "Solomon Islands"), ("SO", "Somalia"),
               ("ZA", "South Africa"), ("GS", "South Georgia and the South Sandwich Islands"), ("ES", "Spain"),
               ("LK", "Sri Lanka"), ("SH", "St. Helena"), ("PM", "St. Pierre and Miquelon"), ("SD", "Sudan"),
               ("SR", "Suriname"), ("SJ", "Svalbard and Jan Mayen Islands"), ("SZ", "Swaziland"), ("SE", "Sweden"),
               ("CH", "Switzerland"), ("SY", "Syrian Arab Republic"), ("TW", "Taiwan, Province of China"),
               ("TJ", "Tajikistan"), ("TZ", "Tanzania, United Republic of"), ("TH", "Thailand"), ("TG", "Togo"),
               ("TK", "Tokelau"), ("TO", "Tonga"), ("TT", "Trinidad and Tobago"), ("TN", "Tunisia"), ("TR", "Turkey"),
               ("TM", "Turkmenistan"), ("TC", "Turks and Caicos Islands"), ("TV", "Tuvalu"), ("UG", "Uganda"),
               ("UA", "Ukraine"), ("AE", "United Arab Emirates"), ("GB", "United Kingdom"), ("US", "United States"),
               ("UM", "United States Minor Outlying Islands"), ("UY", "Uruguay"), ("UZ", "Uzbekistan"),
               ("VU", "Vanuatu"), ("VE", "Venezuela"), ("VN", "Viet Nam"), ("VG", "Virgin Islands (British)"),
               ("VI", "Virgin Islands (U.S.)"), ("WF", "Wallis and Futuna Islands"), ("EH", "Western Sahara"),
               ("YE", "Yemen"), ("ZM", "Zambia"), ("ZW", "Zimbabwe"))


class Visa(models.Model):
    subClass = models.IntegerField(max_length=3)
    description = models.TextField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return str(self.subClass)


class Stage(models.Model):
    order = models.IntegerField(max_length=10)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return "Stage %d - %s" % (self.order, self.title)


class Client(models.Model):
    # Personal Information
    firstName = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, default="")
    preferredName = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True, choices=NATIONALITY)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    onshore = models.BooleanField(default=True)

    # Visa Information
    visa = models.ForeignKey(Visa, blank=True, null=True)
    expire = models.DateField(blank=True, null=True)

    # Service Information
    STATUS_CHOICES = (
        ("Ongoing", "Ongoing"),
        ("Existing", "Existing"),
        ("Close", "Close")
    )
    status = models.CharField(max_length=10, blank=True, null=True, choices=STATUS_CHOICES,
                              default="Ongoing")  ## ChoiceField todo
    referal = models.ForeignKey(Employee, blank=True, null=True, related_name="ref")  # todo
    consultant = models.ForeignKey(Employee, blank=True, null=True, related_name="con")  # todo
    clientManager = models.ForeignKey(Employee, blank=True, null=True, related_name="cm")  # todo
    stage = models.ForeignKey(Stage, null=True, blank=True)
    serviceFee = models.FloatField(blank=True, null=True)
    thirdPartyFeeReceived = models.FloatField(blank=True, null=True)
    thirdPartyFeePaid = models.FloatField(blank=True, null=True)

    # Others
    note = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.firstName, self.surname)


class Institution(models.Model):
    name = models.CharField(max_length=100)
    label = models.ForeignKey(Label, null=True, blank=True)
    commissionRate = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Coe(models.Model):
    client = models.ForeignKey(Client, related_name="coes")
    institution = models.ForeignKey(Institution, blank=True, null=True)
    coeNumber = models.CharField(max_length=30, blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    totalTuitionFee = models.FloatField(blank=True, null=True)
    bonus = models.FloatField(blank=True, null=True)
    referalCommission = models.FloatField(blank=True, null=True)
    consultantCommission = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    documents = models.ManyToManyField(Stage, through='Document', through_fields=('coe', 'stage'), null=True,
                                       blank=True)

    def __unicode__(self):
        return "%s - COE %d" % (self.client.name, self.id)


class Payment(models.Model):
    coe = models.ForeignKey(Coe, related_name="payments")
    previousPayment = models.ForeignKey('self',blank=True, null=True,  related_name="nextPayment")
    receivedAmount = models.FloatField(blank=True, null=True)
    receivedDate = models.DateField(blank=True, null=True)
    paidAmount = models.FloatField(blank=True, null=True)
    paidDate = models.DateField(blank=True, null=True)
    commssionClaimed = models.FloatField(blank=True, null=True)
    commssionRecevied = models.FloatField(blank=True, null=True)
    nextDueDate = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return "%s - %s - Payment %d" % (self.coe.client.name, self.coe.coeNumber, self.id)


def rename_file(instance, filename):
    return "%s/%s/%s/%s" % (instance.coe.client.id, instance.coe.id, instance.stage.id, filename )


class Document(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to=rename_file)
    coe = models.ForeignKey(Coe, related_name="files")
    stage = models.ForeignKey(Stage)


class Invoice(models.Model):
    coe = models.ForeignKey(Coe, related_name="invoices", blank=True, null=True)
    number = models.CharField(max_length=20)
    issueDate = models.DateField(blank=True, null=True)
    payments = models.ManyToManyField(Payment)
    employee = models.ForeignKey(Employee)


