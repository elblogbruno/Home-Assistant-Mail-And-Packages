DOMAIN = "mail_and_packages"
DOMAIN_DATA = "{}_data".format(DOMAIN)
VERSION = "0.3.0-b9"
ISSUE_URL = "http://github.com/moralmunky/Home-Assistant-Mail-And-Packages"
PLATFORM = "sensor"
DATA = "data"
COORDINATOR = "coordinator_mail"

# Attributes
ATTR_COUNT = "count"
ATTR_CODE = "code"
ATTR_ORDER = "order"
ATTR_TRACKING = "tracking"
ATTR_TRACKING_NUM = "tracking_#"
ATTR_IMAGE = "image"
ATTR_SERVER = "server"
ATTR_IMAGE_NAME = "image_name"
ATTR_EMAIL = "email"
ATTR_SUBJECT = "subject"
ATTR_BODY = "body"
ATTR_PATTERN = "pattern"

# Configuration Properties
CONF_FOLDER = "folder"
CONF_PATH = "image_path"
CONF_DURATION = "gif_duration"
CONF_SCAN_INTERVAL = "scan_interval"
CONF_IMAGE_SECURITY = "image_security"
CONF_GENERATE_MP4 = "generate_mp4"
CONF_AMAZON_FWDS = "amazon_fwds"

# Defaults
DEFAULT_NAME = "Mail And Packages"
DEFAULT_PORT = "993"
DEFAULT_FOLDER = '"INBOX"'
DEFAULT_PATH = "/images/mail_and_packages/"
DEFAULT_IMAGE_SECURITY = True
DEFAULT_GIF_DURATION = 5
DEFAULT_SCAN_INTERVAL = 5
DEFAULT_GIF_FILE_NAME = "mail_today.gif"
DEFAULT_AMAZON_FWDS = '""'

# USPS
USPS_Mail_Email = [
    "USPSInformedDelivery@usps.gov",
    "USPSInformeddelivery@informeddelivery.usps.com",
]
USPS_Mail_Subject = "Your Daily Digest"
USPS_Packages_Email = "auto-reply@usps.com"
USPS_Delivering_Subject = "Expected Delivery on"
USPS_Delivered_Subject = "Item Delivered"
USPS_Body_Text = "Your item is out for delivery"

USPS_DELIVERED = "usps_delivered"
USPS_DELIVERING = "usps_delivering"
USPS_PACKAGES = "usps_packages"
USPS_TRACKING = "usps_tracking"
USPS_MAIL = "usps_mail"

USPS_TRACKING_PATTERN = "9[234]\\d{15,22}"

# UPS
UPS_Email = "mcinfo@ups.com"
UPS_Delivering_Subject = "UPS Update: Package Scheduled for Delivery Today"
UPS_Delivering_Subject_2 = "UPS Update: Follow Your Delivery on a Live Map"
UPS_Delivered_Subject = "Your UPS Package was delivered"
UPS_Delivered_Subject_2 = "Your UPS Packages were delivered"
UPS_Body_Text = "Tracking Number"

UPS_DELIVERED = "ups_delivered"
UPS_DELIVERING = "ups_delivering"
UPS_PACKAGES = "ups_packages"
UPS_TRACKING = "ups_tracking"

UPS_TRACKING_PATTERN = "(1Z ?[0-9A-Z]{3} ?[0-9A-Z]{3} ?[0-9A-Z]{2} ?[0-9A-Z]{4} ?[0-9A-Z]{3} ?[0-9A-Z]|[\\dT]\\d\\d\\d ?\\d\\d\\d\\d ?\\d\\d\\d)$"

# FedEx
FEDEX_Email = ["TrackingUpdates@fedex.com", "fedexcanada@fedex.com"]
FEDEX_Delivering_Subject = "Delivery scheduled for today"
FEDEX_Delivering_Subject_2 = "Your package is scheduled for delivery today"
FEDEX_Delivered_Subject = "Your package has been delivered"

FEDEX_DELIVERED = "fedex_delivered"
FEDEX_DELIVERING = "fedex_delivering"
FEDEX_PACKAGES = "fedex_packages"
FEDEX_TRACKING = "fedex_tracking"

FEDEX_TRACKING_PATTERN = "\\d{12,14,20,34}"

# Amazon
Amazon_Domains = "amazon.com,amazon.ca,amazon.co.uk,amazon.in,amazon.de"
AMAZON_Delivered_Subject = "Delivered: Your"
AMAZON_Email = "order-update@"
AMAZON_PACKAGES = "amazon_packages"
AMAZON_ORDER = "amazon_order"
AMAZON_DELIVERED = "amazon_delivered"
AMAZON_IMG_PATTERN = (
    "(https://)([\\w_-]+(?:(?:\\.[\\w_-]+)+))([\\w.,@?^=%&:/~+#-;]*[\\w@?^=%&/~+#-;])?"
)
AMAZON_HUB = "amazon_hub"
AMAZON_HUB_CODE = "amazon_hub_code"
AMAZON_HUB_EMAIL = "thehub@amazon.com"
AMAZON_HUB_SUBJECT = "(You have a package to pick up)(.*)- (\\d{6})"
AMAZON_TIME_PATTERN = (
    "will arrive:,estimated delivery date is:,guaranteed delivery date is:"
)

# Canada Post
CAPost_Email = "donotreply@canadapost.postescanada.ca"
CAPost_Delivered_Subject = "Delivery Notification"

CAPOST_DELIVERED = "capost_delivered"
CAPOST_DELIVERING = "capost_delivering"
CAPOST_PACKAGES = "capost_packages"

# DHL
DHL_Email = ["donotreply_odd@dhl.com", "NoReply.ODD@dhl.com", "noreply@dhl.de"]
DHL_Delivering_Subject = "DHL On Demand Delivery"
DHL_Delivering_Subject_2 = "paket kommt heute"  # Germany deliveries
DHL_Delivered_Subject = "DHL On Demand Delivery"
DHL_Body_Text = "scheduled for delivery TODAY"
DHL_Body_Text_2 = "has been delivered"

DHL_DELIVERED = "dhl_delivered"
DHL_DELIVERING = "dhl_delivering"
DHL_PACKAGES = "dhl_packages"
DHL_TRACKING = "dhl_tracking"

DHL_TRACKING_PATTERN = "number \\d{10} from"

# Hermes (UK)
HERMES_EMAIL = ["donotreply@myhermes.co.uk"]
HERMES_DELIVERING_SUBJECT = "parcel is now with your local Hermes courier"
HERMES_DELIVERED_SUBJECT = "Hermes has successfully delivered your"

HERMES_DELIVERING = "hermes_delivering"
HERMES_DELIVERED = "hermes_delivered"
HERMES_PACKAGES = "hermes_packages"
HERMES_TRACKING = "hermes_tracking"

HERMES_TRACKING_PATTERN = "\\d{16}"

# Royal Mail (UK)
ROYAL_EMAIL = ["no-reply@royalmail.com"]
ROYAL_DELIVERING_SUBJECT = "is on its way"
ROYAL_DELIVERED_SUBJECT = "has been delivered"

ROYAL_DELIVERING = "royal_delivering"
ROYAL_DELIVERED = "royal_delivered"
ROYAL_PACKAGES = "royal_packages"
ROYAL_TRACKING = "royal_tracking"

ROYAL_TRACKING_PATTERN = "[A-Za-z]{2}[0-9]{9}GB"

# Sensor Data
SENSOR_DATA = {
    "usps_delivered": {
        "email": ["auto-reply@usps.com"],
        "subject": ["Item Delivered"],
    },
    "usps_delivering": {
        "email": ["auto-reply@usps.com"],
        "subject": ["Expected Delivery on"],
        "body": ["Your item is out for delivery"],
    },
    "usps_packages": {},
    "usps_tracking": {"pattern": ["9[234]\\d{15,22}"]},
    "usps_mail": {"email": ["mcinfo@ups.com"], "subject": ["Your Daily Digest"],},
    "ups_delivered": {
        "email": ["mcinfo@ups.com"],
        "subject": [
            "Your UPS Package was delivered",
            "Your UPS Packages were delivered",
        ],
    },
    "ups_delivering": {
        "email": ["mcinfo@ups.com"],
        "subject": [
            "UPS Update: Package Scheduled for Delivery Today",
            "UPS Update: Follow Your Delivery on a Live Map",
        ],
        "body": ["Tracking Number"],
    },
    "ups_packages": {},
    "ups_tracking": {
        "pattern": [
            "(1Z ?[0-9A-Z]{3} ?[0-9A-Z]{3} ?[0-9A-Z]{2} ?[0-9A-Z]{4} ?[0-9A-Z]{3} ?[0-9A-Z]|[\\dT]\\d\\d\\d ?\\d\\d\\d\\d ?\\d\\d\\d)$"
        ]
    },
    "fedex_delivered": {
        "email": ["TrackingUpdates@fedex.com", "fedexcanada@fedex.com"],
        "subject": ["Your package has been delivered",],
    },
    "fedex_delivering": {
        "email": ["TrackingUpdates@fedex.com", "fedexcanada@fedex.com"],
        "subject": [
            "Delivery scheduled for today",
            "Your package is scheduled for delivery today",
        ],
    },
    "fedex_packages": {},
    "fedex_tracking": {"pattern": ["\\d{12,14,20,34}"]},
    "capost_delivered": {
        "email": ["donotreply@canadapost.postescanada.ca"],
        "subject": ["Delivery Notification",],
    },
    "capost_delivering": {},
    "capost_packages": {},
    "capost_tracking": {},
    "dhl_delivered": {
        "email": ["donotreply_odd@dhl.com", "NoReply.ODD@dhl.com", "noreply@dhl.de"],
        "subject": ["DHL On Demand Delivery",],
        "body": ["has been delivered"],
    },
    "dhl_delivering": {
        "email": ["donotreply_odd@dhl.com", "NoReply.ODD@dhl.com", "noreply@dhl.de"],
        "subject": ["DHL On Demand Delivery", "paket kommt heute",],
        "body": ["scheduled for delivery TODAY"],
    },
    "dhl_packages": {},
    "dhl_tracking": {"pattern": ["number \\d{10} from"]},
    "hermes_delivered": {
        "email": ["donotreply@myhermes.co.uk"],
        "subject": ["Hermes has successfully delivered your"],
    },
    "hermes_delivering": {
        "email": ["donotreply@myhermes.co.uk"],
        "subject": ["parcel is now with your local Hermes courier"],
    },
    "hermes_packages": {},
    "hermes_tracking": {"pattern": ["\\d{16}"]},
    "royal_delivered": {
        "email": ["no-reply@royalmail.com"],
        "subject": ["has been delivered"],
    },
    "royal_delivering": {
        "email": ["donotreply@myhermes.co.uk"],
        "subject": ["is on its way"],
    },
    "royal_packages": {},
    "royal_tracking": {"pattern": ["[A-Za-z]{2}[0-9]{9}GB"]},
}

# Sensor definitions
# Name, unit of measure, icon
SENSOR_TYPES = {
    "mail_updated": ["Mail Updated", None, "mdi:update"],
    "usps_mail": ["Mail USPS Mail", "piece(s)", "mdi:mailbox-up"],
    "usps_delivered": [
        "Mail USPS Delivered",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    "usps_delivering": ["Mail USPS Delivering", "package(s)", "mdi:truck-delivery"],
    "usps_packages": [
        "Mail USPS Packages",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    "ups_delivered": [
        "Mail UPS Delivered",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    "ups_delivering": ["Mail UPS Delivering", "package(s)", "mdi:truck-delivery"],
    "ups_packages": ["Mail UPS Packages", "package(s)", "mdi:package-variant-closed"],
    "fedex_delivered": [
        "Mail FedEx Delivered",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    "fedex_delivering": ["Mail FedEx Delivering", "package(s)", "mdi:truck-delivery"],
    "fedex_packages": [
        "Mail FedEx Packages",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    "amazon_packages": ["Mail Amazon Packages", "package(s)", "mdi:amazon"],
    "amazon_delivered": [
        "Mail Amazon Packages Delivered",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    "amazon_hub": ["Mail Amazon Hub Packages", "package(s)", "mdi:amazon"],
    "capost_delivered": [
        "Mail Canada Post Delivered",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    "capost_delivering": [
        "Mail Canada Post Delivering",
        "package(s)",
        "mdi:truck-delivery",
    ],
    "capost_packages": [
        "Mail Canada Post Packages",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    "dhl_delivered": [
        "Mail DHL Delivered",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    "dhl_delivering": ["Mail DHL Delivering", "package(s)", "mdi:truck-delivery"],
    "dhl_packages": ["Mail DHL Packages", "package(s)", "mdi:package-variant-closed"],
    "hermes_delivered": [
        "Mail Hermes Delivered",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    "hermes_delivering": ["Mail Hermes Delivering", "package(s)", "mdi:truck-delivery"],
    "hermes_packages": [
        "Mail Hermes Packages",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    "royal_delivered": [
        "Mail Royal Mail Delivered",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    "royal_delivering": [
        "Mail Royal Mail Delivering",
        "package(s)",
        "mdi:truck-delivery",
    ],
    "royal_packages": [
        "Mail Royal Mail Packages",
        "package(s)",
        "mdi:package-variant-closed",
    ],
    ###
    # !!! Insert new sensors above these two !!!
    ###
    "zpackages_delivered": [
        "Mail Packages Delivered",
        "package(s)",
        "mdi:package-variant",
    ],
    "zpackages_transit": [
        "Mail Packages In Transit",
        "package(s)",
        "mdi:truck-delivery",
    ],
}

# Sensor Index
SENSOR_NAME = 0
SENSOR_UNIT = 1
SENSOR_ICON = 2

# For sensors with delivering and delivered statuses
SHIPPERS = ["capost", "dhl", "fedex", "ups", "usps", "hermes", "royal"]
