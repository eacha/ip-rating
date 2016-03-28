class Country(object):
    COUNTRY_CODE = [
        "BD",
        "BE",
        "BF",
        "BG",
        "BA",
        "BN",
        "BO",
        "JP",
        "BI",
        "BJ",
        "BT",
        "JM",
        "BW",
        "BR",
        "BS",
        "BY",
        "BZ",
        "RU",
        "RW",
        "RS",
        "TL",
        "TM",
        "TJ",
        "RO",
        "GW",
        "GT",
        "GR",
        "GQ",
        "GY",
        "GE",
        "GB",
        "GA",
        "GN",
        "GM",
        "GL",
        "GH",
        "OM",
        "TN",
        "JO",
        "HR",
        "HT",
        "HU",
        "HN",
        "PR",
        "PS",
        "PT",
        "PY",
        "PA",
        "PG",
        "PE",
        "PK",
        "PH",
        "PL",
        "ZM",
        "EH",
        "EE",
        "EG",
        "ZA",
        "EC",
        "IT",
        "VN",
        "SB",
        "ET",
        "SO",
        "ZW",
        "ES",
        "ER",
        "ME",
        "MD",
        "MG",
        "MA",
        "UZ",
        "MM",
        "ML",
        "MN",
        "MK",
        "MW",
        "MR",
        "UG",
        "MY",
        "MX",
        "IL",
        "FR",
        "XS",
        "FI",
        "FJ",
        "FK",
        "NI",
        "NL",
        "NO",
        "NA",
        "VU",
        "NC",
        "NE",
        "NG",
        "NZ",
        "NP",
        "XK",
        "CI",
        "CH",
        "CO",
        "CN",
        "CM",
        "CL",
        "XC",
        "CA",
        "CG",
        "CF",
        "CD",
        "CZ",
        "CY",
        "CR",
        "CU",
        "SZ",
        "SY",
        "KG",
        "KE",
        "SS",
        "SR",
        "KH",
        "SV",
        "SK",
        "KR",
        "SI",
        "KP",
        "KW",
        "SN",
        "SL",
        "KZ",
        "SA",
        "SE",
        "SD",
        "DO",
        "DJ",
        "DK",
        "DE",
        "YE",
        "DZ",
        "US",
        "UY",
        "LB",
        "LA",
        "TW",
        "TT",
        "TR",
        "LK",
        "LV",
        "LT",
        "LU",
        "LR",
        "LS",
        "TH",
        "TF",
        "TG",
        "TD",
        "LY",
        "AE",
        "VE",
        "AF",
        "IQ",
        "IS",
        "IR",
        "AM",
        "AL",
        "AO",
        "AR",
        "AU",
        "AT",
        "IN",
        "TZ",
        "AZ",
        "IE",
        "ID",
        "UA",
        "QA",
        "MZ"
    ]

    COUNTRY_NAME = [
        "Bangladesh",
        "Belgium",
        "Burkina Faso",
        "Bulgaria",
        "Bosnia and Herz.",
        "Brunei",
        "Bolivia",
        "Japan",
        "Burundi",
        "Benin",
        "Bhutan",
        "Jamaica",
        "Botswana",
        "Brazil",
        "Bahamas",
        "Belarus",
        "Belize",
        "Russia",
        "Rwanda",
        "Serbia",
        "Timor-Leste",
        "Turkmenistan",
        "Tajikistan",
        "Romania",
        "Guinea-Bissau",
        "Guatemala",
        "Greece",
        "Eq. Guinea",
        "Guyana",
        "Georgia",
        "United Kingdom",
        "Gabon",
        "Guinea",
        "Gambia",
        "Greenland",
        "Ghana",
        "Oman",
        "Tunisia",
        "Jordan",
        "Croatia",
        "Haiti",
        "Hungary",
        "Honduras",
        "Puerto Rico",
        "Palestine",
        "Portugal",
        "Paraguay",
        "Panama",
        "Papua New Guinea",
        "Peru",
        "Pakistan",
        "Philippines",
        "Poland",
        "Zambia",
        "W. Sahara",
        "Estonia",
        "Egypt",
        "South Africa",
        "Ecuador",
        "Italy",
        "Vietnam",
        "Solomon Is.",
        "Ethiopia",
        "Somalia",
        "Zimbabwe",
        "Spain",
        "Eritrea",
        "Montenegro",
        "Moldova",
        "Madagascar",
        "Morocco",
        "Uzbekistan",
        "Myanmar",
        "Mali",
        "Mongolia",
        "Macedonia",
        "Malawi",
        "Mauritania",
        "Uganda",
        "Malaysia",
        "Mexico",
        "Israel",
        "France",
        "Somaliland",
        "Finland",
        "Fiji",
        "Falkland Is.",
        "Nicaragua",
        "Netherlands",
        "Norway",
        "Namibia",
        "Vanuatu",
        "New Caledonia",
        "Niger",
        "Nigeria",
        "New Zealand",
        "Nepal",
        "Kosovo",
        "Cote d'Ivoire",
        "Switzerland",
        "Colombia",
        "China",
        "Cameroon",
        "Chile",
        "N. Cyprus",
        "Canada",
        "Congo",
        "Central African Rep.",
        "Dem. Rep. Congo",
        "Czech Rep.",
        "Cyprus",
        "Costa Rica",
        "Cuba",
        "Swaziland",
        "Syria",
        "Kyrgyzstan",
        "Kenya",
        "S. Sudan",
        "Suriname",
        "Cambodia",
        "El Salvador",
        "Slovakia",
        "Korea",
        "Slovenia",
        "Dem. Rep. Korea",
        "Kuwait",
        "Senegal",
        "Sierra Leone",
        "Kazakhstan",
        "Saudi Arabia",
        "Sweden",
        "Sudan",
        "Dominican Rep.",
        "Djibouti",
        "Denmark",
        "Germany",
        "Yemen",
        "Algeria",
        "United States",
        "Uruguay",
        "Lebanon",
        "Lao PDR",
        "Taiwan",
        "Trinidad and Tobago",
        "Turkey",
        "Sri Lanka",
        "Latvia",
        "Lithuania",
        "Luxembourg",
        "Liberia",
        "Lesotho",
        "Thailand",
        "Fr. S. Antarctic Lands",
        "Togo",
        "Chad",
        "Libya",
        "United Arab Emirates",
        "Venezuela",
        "Afghanistan",
        "Iraq",
        "Iceland",
        "Iran",
        "Armenia",
        "Albania",
        "Angola",
        "Argentina",
        "Australia",
        "Austria",
        "India",
        "Tanzania",
        "Azerbaijan",
        "Ireland",
        "Indonesia",
        "Ukraine",
        "Qatar",
        "Mozambique"
    ]

    def get_name_from_code(self, country_code):
        country_code_index = self.COUNTRY_CODE.index(country_code)
        return self.COUNTRY_NAME[country_code_index]

    def get_code_from_name(self, country_name):
        country_name_index = self.COUNTRY_NAME.index(country_name)
        return self.COUNTRY_CODE[country_name_index]